from django.urls import path, include
from . import views
urlpatterns = [
    path('login/', views.loginuser, name="login"),
    path('register/', views.registeruser, name="register"),
]
