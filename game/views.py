from django.shortcuts import redirect, render
from .models import player
from accounts.decorators import unauthenticated_user
from .forms import *
import os


def main_page(request):
       if request.user.is_authenticated and not request.user.is_superuser:
              try:
                     existing = player.objects.get(user_name=request.user)
                     existing_player = existing
                     points = {
                            "points": existing_player.points
                     }
                     # Adding Points to the player!!
                     # existing.points+=10
                     # existing.save()
                     return render(request, 'game/home.html', points)
              except:
                     new_player = player()
                     new_player.user_name = request.user
                     new_player.points = 0
                     points = {
                            "points": new_player.points
                     }
                     new_player.save()
              return render(request, 'game/home.html', points)
       else:
              return render(request, 'game/home.html', {})


@unauthenticated_user
def profile_view(request):
       profile_pic = player.objects.get(user_name=request.user).profile_pic
       player_1 = request.user
       form = profile_edit(instance=player_1)
       if request.POST:
              form = profile_edit(request.POST,request.FILES,instance=player_1)
              print(request.POST.get('profile_pic'))
              if form.is_valid():
                     form.save()
                     return redirect('profile')
       context = {
              "form": form,
              "profile_pic":profile_pic
       }
       return render(request, "game/profile.html", context)



def leader(request):
       data=player.objects.order_by('-points')
       context={
              "data":data
       }
       return render(request,'game/leader.html',context)