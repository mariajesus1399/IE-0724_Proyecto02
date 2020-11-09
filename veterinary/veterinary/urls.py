"""veterinary URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from appointments import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('new_appointment/', views.new_appointment, name='new_appointment'),
    path('show_appointments/', views.show_appointments, name='show_appointments'),
    path('new/', views.new, name='new'),
    path('', views.home, name='home'),
    path('show/', views.show, name='show'),
    path('show_appointments/<int:pk>', views.show_appointments, name='show_appointments'),
    path('show/<int:pk>', views.show, name='show'),
    path('welcome/', views.welcome, name='welcome'),
    path('login/', views.login, name='login'),
    path('register/', views.register, name='register'),
    path('logout/', views.logout, name='logout'),
    path('welcome_admin/', views.welcome_admin, name='welcome_admin'),
    path('login_admin/', views.login_admin, name='login_admin'),
    path('register_admin/', views.register_admin, name='register_admin'),
    path('logout_admin/', views.logout_admin, name='logout_admin'),
    # path('show_appointments/edit/<int:persona_id>', views.edit),
    # path('show_appointments/delete/<int:persona_id>', views.delete),
    path('edit/<int:pk>', views.edit, name='edit'),
    path('delete/<int:pk>', views.delete, name='delete'),


]
