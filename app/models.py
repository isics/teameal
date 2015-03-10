"""
Models
"""
from django.contrib.auth.models import User
from django.db import models


class MealOccurrence(models.Model):
    """
    Meal occurrence
    """
    name = models.CharField(max_length=64)

    def __unicode__(self):
        return self.name


class Meal(models.Model):
    """
    Meal: 1 meal for 1 user
    """
    meal_occurrence = models.ForeignKey(MealOccurrence)
    user = models.ForeignKey(User)
    cook = models.BooleanField()
    maid = models.BooleanField()

    class Meta:
        unique_together = ('meal_occurrence', 'user')


class Bill(models.Model):
    """
    Bill
    """
    date = models.DateField()
    shop = models.CharField(max_length=64)
    amount = models.DecimalField(max_digits=15, decimal_places=6)
    users = models.ManyToManyField(User)


class UserPayment(models.Model):
    """
    User payment
    """
    user = models.ForeignKey(User)
    date = models.DateField()
    amount = models.DecimalField(max_digits=15, decimal_places=6)
