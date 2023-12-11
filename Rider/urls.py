# urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('', views.RiderListAPIView.as_view(), name='rider-list'),
    path('create/', views.RiderCreateAPIView.as_view(), name='rider-create'),
    path('<int:rider_id>/', views.RiderRetrieveUpdateDeleteView.as_view(), name="rider_detail"),
]
