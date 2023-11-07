from .models import Category, Product, Order, OrderItem, Contact
from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from django.conf import settings
from .models import NewsletterSubscription, Newsletter
from django.contrib import messages
from .forms import ProductForm, CategoryForm
from django.views.decorators.csrf import csrf_exempt
from django.urls import reverse
import stripe
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.utils import timezone
from django.contrib.auth.decorators import login_required

def home(request):
    categories = Category.objects.all().order_by('id')
    products = Product.objects.all()[:2]

    return render(request, 'home.html', {'categories': categories, 'products': products})

@login_required
def profile(request):
    try:
        orders = Order.objects.filter(user=request.user).order_by('-created_at')
        for order in orders:
            items = OrderItem.objects.filter(order=order)
            order.temporary_total = sum([item.quantity * item.product.price for item in items])
        return render(request, 'profile.html', { 'orders': orders })
    except:
        return render(request, 'error/404.html')
    
@login_required
def category_list(request):
    categories = Category.objects.all().order_by('id')

    return render(request, 'category_list.html', {'categories': categories})

@login_required
def category_detail(request, category_id):
    try: 
        category = Category.objects.get(id=category_id)
        products = category.products.all()
        return render(request, 'category_detail.html', {'category': category, 'products': products})

    except:
        return render(request, 'error/404.html')

@login_required
def product_list(request):
    products = Product.objects.all()

    return render(request, 'product_list.html', {'products': products})

def product_detail(request, product_id):
    try:
        product = Product.objects.get(id=product_id)
        is_favorite = product.favorites.filter(id=request.user.id).exists()
        return render(request, 'product_detail.html', {'product': product, 'is_favorite': is_favorite})
    except:
        return render(request, 'error/404.html')

@login_required
def toggle_favorite(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    if product.favorites.filter(id=request.user.id).exists():
        product.favorites.remove(request.user)
    else:
        product.favorites.add(request.user)
    return redirect('product_detail', product_id=product.id)

@login_required
def user_favorites(request):
    try:
        favorited_products = Product.objects.filter(favorites=request.user)
        return render(request, 'user_favorites.html', {'favorited_products': favorited_products})
    except:
        return render(request, 'error/404.html')

def contact_view(request):
    if request.method == 'POST':
        try:
            name = request.POST.get('name')
            email = request.POST.get('email')
            message = request.POST.get('message')

            Contact.objects.create(name=name, email=email, message=message)

            messages.success(request, 'Contact send!')
        except Exception as e:
            messages.error(request, 'Error!')

    return render(request, 'contact.html')

def privacy_view(request):
    return render(request, 'privacy.html')

def terms_view(request):
    return render(request, 'terms.html')

def cart_view(request):
    try:
        cart = request.session.get('cart', {})
        cart_items = []
        cart_total = 0
        cart_count = 0

        for product_id, quantity in cart.items():
            product = Product.objects.get(id=product_id)
            total = quantity * product.price
            cart_count += quantity
            cart_total += total

            cart_items.append({'product': product, 'quantity': quantity, 'total': total})

        return render(request, 'cart.html', { 'items': cart_items, 'total': cart_total, 'count': cart_count })
    except:
        return render(request, 'error/404.html')


def add_to_cart(request, product_id):
    cart = request.session.get('cart', {})
    if product_id in cart:
        cart[product_id] += 1
    else:
        cart[product_id] = 1
    request.session['cart'] = cart
    messages.success(request, 'Product added to cart!')
    return redirect('cart')

def update_cart(request, product_id):
    cart = request.session.get('cart', {})
    if request.method == 'POST':
        quantity = int(request.POST.get('quantity'))
        if quantity > 0:
            cart[product_id] = quantity
        else:
            del cart[product_id]  # Remove o produto se a quantidade for menor ou igual a zero
        request.session['cart'] = cart
    messages.success(request, 'Product quantity updated!')
    return redirect('cart')

def remove_from_cart(request, product_id):
    cart = request.session.get('cart', {})
    if product_id in cart:
        cart[product_id] -= 1
        if cart[product_id] == 0:
            del cart[product_id]
    request.session['cart'] = cart
    messages.success(request, 'Product removed from cart!')
    return redirect('cart')

def clear_cart(request):
    request.session['cart'] = {}
    messages.success(request, 'Cart clear!')
    return redirect('cart')

def create_order(request):
    cart = request.session.get('cart', {})
    if not cart:
        return redirect('cart')
        
    if not request.user.is_authenticated:
        return redirect('/accounts/login/?next=' + request.path)
        
    order = Order.objects.create(user=request.user, status='pending')

    # Adicionar itens ao pedido
    for product_id, quantity in cart.items():
        product = Product.objects.get(id=product_id)
        OrderItem.objects.create(order=order, product=product, quantity=quantity)

    # Limpar o carrinho
    request.session['cart'] = {}

    messages.success(request, 'Order created!')

    return redirect('checkout', order.id)

@login_required
def checkout(request, order_id):
    try:
        order = Order.objects.get(user=request.user, id=order_id)

        items = OrderItem.objects.filter(order=order)
        total = sum([item.quantity * item.product.price for item in items])

        stripe.api_key = settings.STRIPE_SECRET_KEY
        stripe.public_key = settings.STRIPE_PUBLIC_KEY

        if request.method == 'POST':
            try:
                charge = stripe.Charge.create(
                    amount=int(total * 100),  # em centavos
                    currency='eur',
                    description=f'Order #{order.id}',
                    source=request.POST['stripeToken']
                )
                order.street_address = request.POST.get('street_address')
                order.city = request.POST.get('city')
                order.state = request.POST.get('state')
                order.zip_code = request.POST.get('zip_code')
                order.total = total
                order.status = 'paid'
                order.save()

                send_order_confirmation_email(order)

                messages.success(request, 'Order paided!')
            except Exception as e:
                print(e)
                messages.error(request, 'Payment refused!')

            return redirect('checkout', order.id)    

        return render(request, 'checkout.html', { 'order': order, 'items': items, 'total': total, 'stripe_public_key': stripe.public_key })
    except:
        return render(request, 'error/404.html')

#Email Confirmation
def send_order_confirmation_email(order):
    email_to = order.user.email
    subject = render_to_string(
        'checkout/confirmation_email_subject.txt',
        {'order': order}
    ).strip()  # strip to remove any unwanted whitespace
    body = render_to_string(
        'checkout/confirmation_email_body.txt',
        {'order': order, 'contact_email': settings.DEFAULT_FROM_EMAIL}
    )
    recipient_list = [email_to, ]
    send_mail(subject, body, settings.DEFAULT_FROM_EMAIL, recipient_list, fail_silently=False)



@csrf_exempt  # To allow POST requests without CSRF token for simplicity
def subscribe_to_newsletter(request):
    try:
        if request.method == 'POST':
            email = request.POST.get('email')
            if email:
                # Check if the email already exists
                if NewsletterSubscription.objects.filter(email=email).exists():
                    return JsonResponse({'status': 'error', 'message': 'This email is already subscribed.'})

                # Create new subscriber
                NewsletterSubscription.objects.create(email=email)
                return JsonResponse({'status': 'success', 'message': 'Thank you for subscribing to our newsletter.'})

            return JsonResponse({'status': 'error', 'message': 'Email is required.'})

        return JsonResponse({'status': 'error', 'message': 'Invalid request.'})
    except:
        return JsonResponse({'status': 'error', 'message': 'Something worng!'})

@login_required
def dashboard(request):
    if request.user.is_superuser:
        return render(request, 'dashboard/dashboard.html')
    else:
        return render(request, 'error/403.html')

@login_required
def manage_products(request):
    if request.user.is_superuser:
        products = Product.objects.all()
        return render(request, 'dashboard/manage_products.html', {'products': products})
    else:
        return render(request, 'error/403.html')

@login_required
def add_product(request):
    if request.user.is_superuser:
        if request.method == 'POST':
            form = ProductForm(request.POST, request.FILES)
            if form.is_valid():
                new_product = form.save()
                # Assuming you create a newsletter entry when a new product is added.
                newsletter = Newsletter.objects.create(
                    subject= render_to_string('newsletter/new_product_alert_subject.txt', {'product_name': new_product.name}).strip(),
                    message=render_to_string('newsletter/new_product_alert_body.txt', {'product_name': new_product.name,'product_description': new_product.description, 'product_url': request.build_absolute_uri(new_product.get_absolute_url())}),
                    recipients=",".join([subscriber.email for subscriber in NewsletterSubscription.objects.all()]),
                    sent_successfully=""
                )
                if send_newsletter(request, newsletter.id):
                    print("Newsletter sent successfully!")
                else:
                   print( "There was a problem sending the newsletter.")
                return redirect('manage_products')
        else:
            form = ProductForm()
        return render(request, 'dashboard/add_product.html', {'form': form})
    else:
        return render(request, 'error/403.html')

def send_newsletter(request, newsletter_id):
    try:
        newsletter = Newsletter.objects.get(id=newsletter_id)
        subscribers = newsletter.recipients.split(',')  # Assuming subscribers are stored as a comma-separated list.
        
        subject = newsletter.subject
        message = newsletter.message
        
        successfully_sent = []

        # Send email to each subscriber
        for email in subscribers:
            try:
                send_mail(subject, message, settings.EMAIL_HOST_USER, [email], fail_silently=False)
                successfully_sent.append(email)
            except Exception as e:
                # If sending failed, log the error (not shown here)
                continue

        # Update the Newsletter model with the emails that were sent successfully
        newsletter.sent_successfully = ','.join(successfully_sent)  # Overwrite any existing data
        newsletter.sent_date = timezone.now()
        newsletter.save()

        return True
    except Newsletter.DoesNotExist:
        print( "Newsletter does not exist.")
        return False
    except Exception as e:
        print("An error occurred: " + str(e))
        return False

@login_required
def edit_product(request, product_id):
    if request.user.is_superuser:
        product = Product.objects.get(id=product_id)
        if request.method == 'POST':
            form = ProductForm(request.POST, request.FILES, instance=product)
            if form.is_valid():
                form.save()
                return redirect('manage_products')
        else:
            form = ProductForm(instance=product)
        return render(request, 'dashboard/edit_product.html', {'form': form, 'product': product})
    else:
        return render(request, 'error/403.html')

@login_required
def delete_product(request, product_id):
    if request.user.is_superuser:
        product = Product.objects.get(id=product_id)
        product.delete()
        return redirect('manage_products')
    else:
        return render(request, 'error/403.html')

@login_required
def manage_categories(request):
    if request.user.is_superuser:
        categories = Category.objects.all()
        return render(request, 'dashboard/manage_categories.html', {'categories': categories})
    else:
        return render(request, 'error/403.html')

# View for adding a category
@login_required
def add_category(request):
    if request.user.is_superuser:
        if request.method == "POST":
            form = CategoryForm(request.POST, request.FILES)
            if form.is_valid():
                form.save()
                return redirect(reverse('manage_categories'))
        else:
            form = CategoryForm()
        return render(request, 'dashboard/add_category.html', {'form': form})
    else:
        return render(request, 'error/403.html')

# View for editing a category
@login_required
def edit_category(request,  category_id):
    if request.user.is_superuser:
        category = get_object_or_404(Category, id=category_id)
        if request.method == "POST":
            form = CategoryForm(request.POST, request.FILES, instance=category)
            if form.is_valid():
                form.save()
                return redirect(reverse('manage_categories'))
        else:
            form = CategoryForm(instance=category)
        return render(request, 'dashboard/edit_category.html', {'form': form, 'category': category})
    else:
        return render(request, 'error/403.html')

# View for deleting a category
@login_required
def delete_category(request, category_id):
    try:
        if request.user.is_superuser:
            category = Category.objects.get(id=category_id)
            category.delete()
            return redirect('manage_categories')
        else:
            return render(request, 'error/403.html')
    except:
        return render(request, 'error/404.html')
@login_required
def view_contacts(request):
    if request.user.is_superuser:
        contacts = Contact.objects.all()
        return render(request, 'dashboard/view_contacts.html', {'contacts': contacts})
    else:
        return render(request, 'error/403.html')



def error_400_view(request, exception):
    return render(request, 'error/400.html')

def error_403_view(request, exception):
    return render(request, 'error/403.html')

def error_500_view(request):
    return render(request, 'error/500.html')

def error_404_view(request, exception):
    return render(request, 'error/404.html')