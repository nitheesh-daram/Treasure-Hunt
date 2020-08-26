from django.db import models
from django.contrib.auth.models import User
class player(models.Model):
    user_name=models.OneToOneField(User,null=True,on_delete=models.CASCADE)
    points=models.IntegerField()
    profile_pic=models.ImageField( default="profile1.png")
    date_created=models.DateTimeField(auto_now_add=True,null=True)    


    def earned_points(self):
        return self.points
