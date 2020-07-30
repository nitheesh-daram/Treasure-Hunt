from django.shortcuts import render

# Create your views here.

def map_view(request):
       access_token='pk.eyJ1IjoibWFkLXRpdGFuIiwiYSI6ImNrZDc5Zm9oZDA4eHAycnBmdDBuc2h6bHgifQ.1o-KQ0TTGjebKAHf1Dm5zQ'
       return render(request,'map/map.html',{"access_token":access_token})