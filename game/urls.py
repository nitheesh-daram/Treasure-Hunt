from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('',views.main_page,name="Home_Page"),
    path('profile/',views.profile_view,name="profile"),
    path('leaderboard/',views.leader,name="leaderboard"),
    path('game/',views.game_play,name='game'),
]
