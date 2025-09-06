"""
URL configuration for fitflow project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from core.views import register, product_detail, forgot_password
from django.views.generic import RedirectView

urlpatterns = [
    path('admin/', admin.site.urls),
    
    # Authentication URLs
    path('', RedirectView.as_view(url='login/'), name='root'),
    path('login/', auth_views.LoginView.as_view(template_name='core/login.html'), name='login'),
    path('forgot-password/', forgot_password, name='forgot_password'),
    path('password-reset/', auth_views.PasswordResetView.as_view(template_name='core/forgot_password.html'), name='password_reset'),
    path('logout/', auth_views.LogoutView.as_view(next_page='login'), name='logout'),
    path('register/', register, name='register'),
    
    # Direct access to product details
    path('product/<slug:slug>/', product_detail, name='product_detail'),
    
    # Main app URLs
    path('app/', include('core.urls')),
]

# Add static and media URLs for development
# if settings.DEBUG:
    # Add static and media URLs
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
