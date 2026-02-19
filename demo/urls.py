"""
URL configuration for demo project.

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
from health_check.views import HealthCheckView

urlpatterns = [
    path(
        "",
        HealthCheckView.as_view(
            checks=[
                "health_check.Cache",
                "health_check.Database",
                "health_check.Storage",
                "health_check.contrib.psutil.Disk",
                "health_check.contrib.psutil.Memory",
            ]
        ),
        name="home",
    ),
    path(
        "health/",
        HealthCheckView.as_view(
            checks=[
                "health_check.contrib.psutil.Disk",
                "health_check.contrib.psutil.Memory",
            ]
        ),
        name="health",
    ),
    path("admin/", admin.site.urls),
]
