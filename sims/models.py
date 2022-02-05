from django.db import models
from django.forms import CharField

class Simulation(models.Model):
    name = models.CharField(max_length=255)
    def __str__(self) -> str:
        return self.name

class User(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    def __str__(self) -> str:
        return self.name

class Comment(models.Model):
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    simulation = models.ForeignKey(Simulation, on_delete=models.PROTECT)
    user = models.ForeignKey(User, on_delete=models.PROTECT)