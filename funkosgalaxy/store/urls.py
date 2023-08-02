from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('product_list/', views.product_list, name='product_list'),
    path('product_detail/<int:product_id>/', views.product_detail, name='product_detail'),
    path('process_payment/', views.process_payment, name='process_payment'),
]
