from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class Profile(models.Model):
    username = models.ForeignKey(User, on_delete=models.CASCADE)
    firstname = models.TextField()
    lastname = models.TextField()
    location = models.CharField(max_length=100, blank=True)
    age = models.IntegerField()
    bio = models.TextField(blank=True)


    def __str__(self) -> str:
        return super().__str__()