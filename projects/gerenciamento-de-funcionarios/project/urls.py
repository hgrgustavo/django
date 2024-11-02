from django.contrib import admin
from django.urls import path
from django.urls.conf import include

urlpatterns = [
    # urls app website
    path("", include("website.urls", namespace="webiste")),

    # interface administrativa
    path("admin/", admin.site.urls)
]
