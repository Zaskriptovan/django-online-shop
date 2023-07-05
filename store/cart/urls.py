from django.urls import path

from . import views

urlpatterns = [
    path('', views.CartView.as_view(), name='cart_view'),
    path('add/<int:product_id>/', views.CartAdd.as_view(), name='cart_add'),
]
