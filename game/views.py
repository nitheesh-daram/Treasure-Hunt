from django.shortcuts import redirect, render
from .models import player, qrcode
from accounts.decorators import unauthenticated_user
from .forms import *
from django.contrib import messages


def main_page(request):
    if request.user.is_authenticated and not request.user.is_superuser:
        try:
            existing = player.objects.get(user_name=request.user)
            existing_player = existing
            points = {
                "points": existing_player.points
            }
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
    points=player.objects.get(user_name=request.user).points
    form = profile_edit(instance=player_1)
    if request.POST:
        form = profile_edit(request.POST, request.FILES, instance=player_1)
        # print(request.POST.get('profile_pic'))
        if form.is_valid():
            form.save()
            return redirect('profile')
    context = {
        "form": form,
        "profile_pic": profile_pic,
        "points":points
    }
    return render(request, "game/profile.html", context)


@unauthenticated_user
def leader(request):
    data = player.objects.order_by('-points')
    points=player.objects.get(user_name=request.user).points
    context = {
        "data": data,
        "points":points
    }
    return render(request, 'game/leader.html', context)


@unauthenticated_user
def game_play(request):
    user = player.objects.get(user_name=request.user)
    user_points = user.points
    if user_points == 0:
        if request.POST:
            user.points += 10
            user.save()
            return redirect('game')
        return render(request, "game/level1.html", {"points":user_points})
    elif user_points == 10:
        data = qrcode.objects.all()
        # if not request.POST.get('location') is None:
        if not request.POST.get('1') is None:
            # print(request.POST)
            # print(data.get(id=8))
            code_1 = data.get(id=request.POST.get('1'))
            code_2 = data.get(id=request.POST.get('2'))
            code_3 = data.get(id=request.POST.get('3'))
            context = {
                "code_1": code_1.code,
                "code_2": code_2.code,
                "code_3": code_3.code,
                "points":user_points
            }
            return render(request, "game/level2-1.html", context)
        if not request.POST.get('location') is None:
            if request.POST.get('location') == "Albert Hall":
                user.points += 20
                user.save()
                return redirect('game')
            else:
                messages.info(request, "location Incorrect")
                return redirect("game")
        return render(request, "game/level2.html", {"points":user_points})
    elif user_points == 30:
        if request.POST:
            if request.POST.get('location') == 'City Palace':
                user.points += 35
                user.save()
                return redirect("game")
            else:
                messages.info(request, "Location is incorrect")
        return render(request, "game/level3.html", {"points":user_points})
    elif user_points == 65:
        if request.POST:
            if request.POST.get('location') == "Jantar Mantar":
                user.points += 50
                user.save()
                return redirect("game")
            else:
                messages.info(request, "Location Incorrect")
        return render(request, "game/level4.html", {"points":user_points})
    elif user_points == 115:
        if request.POST:
            if request.POST.get('location') == "Govind Dev Ji":
                user.points += 65
                user.save()
                return redirect("game")
            else:
                messages.info(request, "Location Incorrect")
        return render(request, "game/level5.html", {"points":user_points})
    elif user_points == 180:
        if request.POST:
            if request.POST.get('location') == "Jal Mahal":
                user.points += 80
                user.save()
                return redirect("game")
            else:
                messages.info(request, "Location Incorrect")
        return render(request, "game/level6.html", {"points":user_points})
    elif user_points == 260:
        if request.POST:
            if request.POST.get('location') == "Amer Fort":
                user.points += 100
                user.save()
                return redirect("game")
            else:
                messages.info(request, "Location Incorrect")
        return render(request, "game/level7.html", {"points":user_points})
    elif user_points == 360:
        if request.POST:
            if request.POST.get('location') == "Nahargarh Museum":
                user.points += 130
                user.save()
                return redirect("game")
            else:
                messages.info(request, "Location Incorrect")
        return render(request, "game/level8.html", {"points":user_points})
    elif user_points == 490:
        if request.POST:
            if request.POST.get('location') == "Kanak Vrindavan":
                user.points += 165
                user.save()
                return redirect("game")
            else:
                messages.info(request, "Location Incorrect")
        return render(request, "game/level9.html", {"points":user_points})
    elif user_points == 655:
        if request.POST:
            if request.POST.get('location') == "Moti Doongri":
                user.points += 190
                user.save()
                return redirect("game")
            else:
                messages.info(request, "Location Incorrect")
        return render(request, "game/level10.html", {"points":user_points})
    elif user_points == 845:
        if request.POST:
            # print(dir(str))
            if request.POST.get('location') == "Jawahar Kala Kendra":
                user.points += 250
                user.save()
                return redirect("game")
            else:
                messages.info(request, "Location Incorrect")
        return render(request, "game/level11.html", {"points":user_points})
    else:
        return render(request, "game/level12.html", {"points":user_points})
