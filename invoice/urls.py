# urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('', views.InvoiceListAPIView.as_view(), name='order-list'),
    path('create/', views.InvoiceCreateAPIView.as_view(), name='create-order'),
    path('<int:invoice_id>/', views.InvoiceRetrieveUpdateDeleteView.as_view(), name="order_detail"),
]
