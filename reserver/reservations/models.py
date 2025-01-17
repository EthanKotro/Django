from django.db import models
from django.contrib.auth.models import User

class Reservation(models.Model):
    # user= models.ForeignKey(User, on_delete=models.CASCADE)
    name= models.CharField(max_length=100)
    date= models.DateField()
    time= models.TimeField()
    table_size=models.IntegerField()
    created_at=models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.name}-{self.date} at {self.time}"