"""
URL configuration for MeuSite project.

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
from django.urls import path
from MeuSite import views  # Import the home view
from django.urls import include  # Import include to include app URLs

urlpatterns = [
    path("admin/", admin.site.urls),

    # Add the home view URL pattern
    # Map the home view to the root URL
    path('', views.home, name='home'),  # Map the home view to the root URL
    path('curriculo/', include('curriculo.urls')),  # Include the curriculo app URLs
]
