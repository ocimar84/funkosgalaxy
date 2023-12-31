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
    path('subscribe_to_newsletter/', views.subscribe_to_newsletter, name='subscribe_to_newsletter'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('dashboard/products/', views.manage_products, name='manage_products'),
    path('dashboard/create-product/', views.add_product, name='add_product'),
    path('dashboard/edit-product/<int:product_id>/', views.edit_product, name='edit_product'),
    path('dashboard/delete-product/<int:product_id>/', views.delete_product, name='delete_product'),
    path('dashboard/categories/', views.manage_categories, name='manage_categories'),
    path('dashboard/create-category/', views.add_category, name='add_category'),
    path('dashboard/edit-category/<int:category_id>/', views.edit_category, name='edit_category'),
    path('dashboard/delete-category/<int:category_id>/', views.delete_category, name='delete_category'),
    path('dashboard/contacts/', views.view_contacts, name='view_contacts'),

]
