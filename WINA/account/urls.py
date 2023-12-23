from django.urls import path
from . import views

urlpatterns = [
    path("join/", views.signup, name="join"),
    path("login/", views.llogin, name="login"),
    path("logout/", views.logout, name="logout"),
]
