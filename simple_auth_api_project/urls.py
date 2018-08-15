"""simple_auth_api_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from django.conf.urls import url, include
from django.contrib import admin
from django.urls import path
from rest_framework import routers

from custom_auth import views as custom_auth_views
from my_account import views as my_account_views


# Routers provide an easy way of automatically determining the URL conf
router = routers.DefaultRouter()
router.register(r'user', custom_auth_views.UserViewSet)
router.register(r'groups', custom_auth_views.GroupViewSet)
router.register(r'address', my_account_views.AddressViewSet)
router.register(r'address', my_account_views.AddressListViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^', include(router.urls)),
    url(r'^o/', include('oauth2_provider.urls', namespace='oauth2_provider')),
]
