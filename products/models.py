from django.db import models


class Products(models.Model):
    latinos_name = models.CharField(max_length=30, null=False, unique=True)
    name = models.CharField(max_length=30, null=False, unique=True)
    description = models.TextField(null=True)
    calories = models.CharField(max_length=63)
    fats = models.CharField(max_length=63)
    carbs = models.CharField(max_length=63)
    proteins = models.CharField(max_length=63)
    unsaturated_fats = models.CharField(max_length=63)
    sugar = models.CharField(max_length=63)
    salt = models.CharField(max_length=63)
    portion = models.CharField(max_length=63)

    def __str__(self):
        return f"{self.name}"
