from .models import Category, Product, Order, OrderItem, Contact
from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from django.conf import settings
from django.contrib import messages
import stripe

def home(request):
    categories = Category.objects.all().order_by('id')
    products = Product.objects.all()[:2]

    return render(request, 'home.html', {'categories': categories, 'products': products})

def profile(request):
    orders = Order.objects.filter(user=request.user).order_by('-created_at')

    for order in orders:
        items = OrderItem.objects.filter(order=order)
        order.temporary_total = sum([item.quantity * item.product.price for item in items])

    return render(request, 'profile.html', { 'orders': orders })

def category_list(request):
    categories = Category.objects.all().order_by('id')

    return render(request, 'category_list.html', {'categories': categories})

def category_detail(request, category_id):
    category = Category.objects.get(id=category_id)
    products = category.products.all()

    return render(request, 'category_detail.html', {'category': category, 'products': products})

def product_list(request):
    products = Product.objects.all()

    return render(request, 'product_list.html', {'products': products})

def product_detail(request, product_id):
    product = Product.objects.get(id=product_id)

    return render(request, 'product_detail.html', {'product': product})

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

def add_to_cart(request, product_id):
    cart = request.session.get('cart', {})
    if product_id in cart:
        cart[product_id] += 1
    else:
        cart[product_id] = 1
    request.session['cart'] = cart
    messages.success(request, 'Product added to cart!')
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

    order = Order.objects.create(user=request.user, status='pending')

    # Adicionar itens ao pedido
    for product_id, quantity in cart.items():
        product = Product.objects.get(id=product_id)
        OrderItem.objects.create(order=order, product=product, quantity=quantity)

    # Limpar o carrinho
    request.session['cart'] = {}

    messages.success(request, 'Order created!')

    return redirect('checkout', order.id)

def checkout(request, order_id):
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
            order.total = total
            order.status = 'paid'
            order.save()

            messages.success(request, 'Order paided!')
        except Exception as e:
            messages.error(request, 'Payment refused!')

        return redirect('checkout', order.id)    

    return render(request, 'checkout.html', { 'order': order, 'items': items, 'total': total, 'stripe_public_key': stripe.public_key })
