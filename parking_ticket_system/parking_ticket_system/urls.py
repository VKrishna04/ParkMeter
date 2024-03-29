"""
URL configuration for parking_ticket_system project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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

# Define the URL patterns for the parking_ticket_system project
urlpatterns = [
    path(
        "", admin.site.urls
    ),  # Develop a landing page here or link it to admin login page.
    path("admin/", admin.site.urls),  # Admin site URL
    path("", include("tickets.urls")),  # Include ticket app URLs (if defined)
    # path("", include("payment.urls")),  # Include payment app URLs (if defined)
]
