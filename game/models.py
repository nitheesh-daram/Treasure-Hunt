from django.db import models

class player(models.Model):
    user_name=models.CharField(max_length=50,unique=True)
    points=models.IntegerField()
    
    def earned_points(self):
        return self.points
