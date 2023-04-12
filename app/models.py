from django.db import models
from django.contrib.auth.models import User

# Create your models here.

    
class studentnew(models.Model):
    phoneno=models.CharField(max_length=20,null=True)
    age=models.IntegerField(null=True)
    gendermale=0
    genderfemale=1
    genderchoice=[(gendermale,'male'),(genderfemale,'female')]
    gender=models.IntegerField(choices=genderchoice)
    birtdate=models.DateTimeField()
    User = models.OneToOneField(User, on_delete=models.CASCADE)
   
    