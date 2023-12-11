
from django.contrib import admin
from django.urls import path
from . import views 

urlpatterns = [
    path('user/create', views.CreateAdminView.as_view(), name="create_user"),
    
    path('admins/', views.ListAdminView.as_view(), name="list_admins"),
    
    path('login/', views.LoginView.as_view(), name='login'),
    
    path('list_admins/<int:user_id>/', views.AdminRetrieveUpdateDeleteView.as_view(), name="admin_detail"),
]
