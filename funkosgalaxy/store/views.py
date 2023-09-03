from django.shortcuts import render
from django.http import JsonResponse
from .models import Category, Product
import stripe
from django.conf import settings

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

def showcase_view(request):
    products = Product.objects.all()

    return render(request, 'showcase.html', {'products': products})

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
