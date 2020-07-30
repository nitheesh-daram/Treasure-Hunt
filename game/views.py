from django.shortcuts import render
from .models import player
def main_page(request): 
       if request.user.is_authenticated and not request.user.is_superuser:  
              try:
                     existing=player.objects.get(user_name = request.user)
                     existing_player=existing
                     points={
                            "points":existing_player.points
                     }
                     # Adding Points to the player!!
                            # existing.points+=10
                            # existing.save()
                     return render(request,'game/home.html',points)
              except:
                     new_player=player()
                     new_player.user_name=request.user
                     new_player.points=0
                     points={
                            "points":new_player.points
                     }
                     new_player.save()
                     return render(request,'game/home.html',points)
       else:
            return render(request,'game/home.html',{})
 

