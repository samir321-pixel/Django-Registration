"""Django_Registration URL Configuration

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
from account import views
from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView, PasswordChangeView, PasswordChangeDoneView, \
    PasswordResetView, PasswordResetDoneView, PasswordResetConfirmView, PasswordResetCompleteView
from account.views import RegisterView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('account/', views.view, name='account_view'),
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(template_name='authn/login.html'), name='login'),
    path('logout/', LogoutView.as_view(template_name='authn/logged_out.html'), name='logout'),
    path('password_change/done/', PasswordChangeDoneView.as_view(template_name='authn/password_change_done.html'),
         name='password_change_done'),
    path('password_change/', PasswordChangeView.as_view(template_name='authn/password_change_form.html'),
         name='password_change'),
    path('password_reset/done/', PasswordResetDoneView.as_view(template_name='authn/password_reset_done.html'),
         name='password_reset_done'),
    path('password_reset/', PasswordResetView.as_view(template_name='authn/password_reset_form.html'),
         name='password_reset'),
    path('reset/done/', PasswordResetCompleteView.as_view(template_name='authn/password_reset_complete.html'),
         name='password_reset_complete'),
    path('reset/<uidb64>/<token>/', PasswordResetConfirmView.as_view(template_name='authn/password_reset_confirm.html'),
         name='password_reset_confirm'),
]
