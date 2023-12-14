# urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('', views.OrderListAPIView.as_view(), name='order-list'),
    path('create/', views.OrderCreateAPIView.as_view(), name='create-order'),
    path('<int:order_id>/', views.OrderRetrieveUpdateDeleteView.as_view(), name="order_detail"),
    path('by_establishment/<int:establishment_id>/', views.OrderListByEstablishmentAPIView.as_view(), name='order-list-by-establishment'),
    path('by_order_number/<str:order_number>/', views.OrderByOrderNumberAPIView.as_view(), name='order-list-by-order_number'),
]
