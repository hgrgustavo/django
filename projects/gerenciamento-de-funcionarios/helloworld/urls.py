from django.urls import path
from django.urls.conf import include
from django.contrib import admin


urlpatterns = [
    path("", include("website.urls", namespace="website")),
    path("admin/", admin.site.urls),


]