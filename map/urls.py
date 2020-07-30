from django.urls import path,include
from . import views
urlpatterns = [
    path('',views.map_view,name="map_view"),
]
