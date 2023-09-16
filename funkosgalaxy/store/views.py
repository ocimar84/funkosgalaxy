from django.shortcuts import render
from django.http import JsonResponse
from .models import Category, Product
from django.shortcuts import get_object_or_404
from django.conf import settings
import stripe
import random

stripe.api_key = settings.STRIPE_SECRET_KEY

def home(request):
    categories = Category.objects.all().order_by('id')
    products = Product.objects.all()[:2]

    return render(request, 'home.html', {'categories': categories, 'products': products})

def profile(request):
    return render(request, 'contact.html')

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
    return render(request, 'contact.html')

def privacy_view(request):
    return render(request, 'privacy.html')

def cart_view(request):
    bag = request.session.get('bag', {})
    bag_items = []
    bag_total = 0
    bag_products_count = 0

    products = Product.objects.all()[:3]
    for product in products:
        bag[product.id] = random.randint(1, 4)

    for item_id, item_data in bag.items():
        if isinstance(item_data, int):
            product = get_object_or_404(Product, pk=item_id)
            total = item_data * product.price
            bag_total += total
            bag_products_count += item_data
            bag_items.append({
                'item_id': item_id,
                'quantity': item_data,
                'total': total,
                'product': product,
            })

    return render(request, 'cart.html', { 'items': bag_items, 'total': bag_total, 'count': bag_products_count })

def process_payment(request):
    if request.method == 'POST':
        payment_method_id = request.POST['payment_method_id']

        # Crie uma cobrança usando o método de pagamento do Stripe
        try:
            payment_intent = stripe.PaymentIntent.create(
                amount=1000,  # Valor em centavos (neste exemplo, 10 reais)
                currency='brl',
                payment_method=payment_method_id,
                confirm=True,
            )

            # Se o pagamento for bem-sucedido, você pode atualizar o pedido do cliente ou realizar outras ações necessárias
            return JsonResponse({'success': True})
        except stripe.error.CardError as e:
            # Lidar com erros do cartão de crédito
            return JsonResponse({'error': e.user_message}, status=400)
        except stripe.error.StripeError:
            # Lidar com outros erros do Stripe
            return JsonResponse({'error': 'An error occurred while processing your payment.'}, status=400)
    
    return JsonResponse({'error': 'Invalid request.'}, status=400)
