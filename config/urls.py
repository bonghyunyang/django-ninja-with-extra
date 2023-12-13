from django.contrib import admin
from django.urls import path
from api.views_for_ninja import api as ninja_api
from api.views_for_ninja_extra import api as ninja_extra_api

urlpatterns = [
    path("admin/", admin.site.urls),
    path("ninja/", ninja_api.urls),
    path("ninja_extra/", ninja_extra_api.urls),
]