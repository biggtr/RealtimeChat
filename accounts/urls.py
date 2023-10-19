from django.urls import include, path
from .views import HomePage

urlpatterns = [
    path("", include("allauth.urls")),
]
