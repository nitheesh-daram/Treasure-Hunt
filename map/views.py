from django.shortcuts import render
from accounts.decorators import unauthenticated_user
# Create your views here.
from game.models import player

@unauthenticated_user
def map_view(request):
       points=player.objects.get(user_name=request.user).points
       access_token='pk.eyJ1IjoibWFkLXRpdGFuIiwiYSI6ImNrZDc5Zm9oZDA4eHAycnBmdDBuc2h6bHgifQ.1o-KQ0TTGjebKAHf1Dm5zQ'
       return render(request,'map/map.html',{"access_token":access_token,"points":points})