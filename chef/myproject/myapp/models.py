from django.db import models

class Food(models.Model):
    name = models.CharField(max_length=255)
    ingredients = models.TextField()
    calories = models.IntegerField()
    serving_size = models.FloatField()

    def __str__(self):
        return self.name

class FoodMenu(models.Model):
    date = models.DateField()
    food_name = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.food_name} - {self.date}"

from django.db import models

class Menu(models.Model):
    date = models.DateField()
    breakfast = models.CharField(max_length=255)
    snack = models.CharField(max_length=255)
    lunch = models.CharField(max_length=255)
    calories = models.IntegerField()

    def __str__(self):
        return f"{self.date} - {self.breakfast}, {self.lunch}"

from django.db import models

class MealMenu(models.Model):
    date = models.DateField()  # Хоолны цэсийн огноо
    meal_name = models.CharField(max_length=255)  # Хоолны нэр
    calories = models.IntegerField()  # Калори
    ingredients = models.TextField()  # Орц
