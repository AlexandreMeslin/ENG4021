"""
URL configuration for MeuSite project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
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
from MeuSite import views  # Import the home view
from django.urls.conf import include

app_name = 'MeuSite'

urlpatterns = [
    path("admin/", admin.site.urls),
    path('', views.home, name='home'),  # Map the home view to the root URL
    path('spiff/', views.curriculo_spiff, name='curriculo_spiff'),
    # essa rota pode ser acessada em /spiff/v2/
    path('spiff/v2/', views.curriculo_spiff_v2, name='curriculo_spiff_v2'),
    path('accounts/', include('django.contrib.auth.urls')),  # Include authentication URLs
]
