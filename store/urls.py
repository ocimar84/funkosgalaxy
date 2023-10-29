from django.urls import include, path
from . import views

urlpatterns = [
    path('accounts/', include('allauth.urls')),
    path('accounts/profile/', views.profile, name='profile'),
    path('category_list/', views.category_list, name='category_list'),
    path('category_detail/<int:category_id>/', views.category_detail, name='category_detail'),
    path('product_list/', views.product_list, name='product_list'),
    path('product_detail/<int:product_id>/', views.product_detail, name='product_detail'),
    path('contact/', views.contact_view, name='contact'),
    path('privacy/', views.privacy_view, name='privacy'),
    path('terms/', views.terms_view, name='terms'),
    path('cart/', views.cart_view, name='cart'),
    path('add_to_cart/<str:product_id>/', views.add_to_cart, name='add_to_cart'),
    path('update_cart/<str:product_id>/', views.update_cart, name='update_cart'),
    path('remove_from_cart/<str:product_id>/', views.remove_from_cart, name='remove_from_cart'),
    path('clear_cart/', views.clear_cart, name='clear_cart'),
    path('create_order/', views.create_order, name='create_order'),
    path('checkout/<int:order_id>/', views.checkout, name='checkout'),
    path('', views.home, name='home'),
    path('product/<int:product_id>/toggle_favorite/', views.toggle_favorite, name='toggle_favorite'),
    path('favorites/', views.user_favorites, name='user_favorites'),

]
