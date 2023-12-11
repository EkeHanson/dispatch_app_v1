from django.urls import path
from . import views

urlpatterns = [
    path('', views.EstablishmentListAPIView.as_view(), name='establishment-list'),
    path('create/', views.EstablishmentCreateAPIView.as_view(), name='establishment-create'),
    path('<int:establishment_id>/', views.EstablishmentRetrieveUpdateDeleteView.as_view(), name="establishment_detail"),
]
  