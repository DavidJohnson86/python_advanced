from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Food(models.Model):
    name = models.CharField(max_length=300)
    energy = models.FloatField()
    amount = models.FloatField()
    unit = models.CharField(max_length=20)
    source = models.CharField(max_length=100)
    protein = models.FloatField()
    carbs = models.FloatField()
    fat = models.FloatField()

    def __str__(self):
        return "{} ({})".format(self.name, self.pk)

class Meal(models.Model):
    name = models.CharField(max_length=20)
    date = models.DateTimeField()
    foods = models.ManyToManyField(Food)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return "{} ({})".format(self.name, self.pk)