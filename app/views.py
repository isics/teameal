from django.contrib.auth.models import User
from django.db.models import Sum
from django.shortcuts import render_to_response

from app.models import Bill, Meal, UserPayment

def index(request):
    """
    Homepage
    """
    users = User.objects.order_by('username')
    nb_meals = Meal.objects.count()
    expenses = Bill.objects.all().aggregate(Sum('amount'))['amount__sum'] or 0
    receipts = UserPayment.objects.all().aggregate(Sum('amount'))['amount__sum'] or 0
    balance = receipts - expenses

    for user in users:
        user.nb_meals = Meal.objects.filter(user=user).count()
        user.payments = UserPayment.objects.filter(user=user).aggregate(Sum('amount'))['amount__sum'] or 0
        user.part = nb_meals and user.nb_meals / nb_meals * 100 or 0
        user.debt = user.part / 100 * float(expenses)
        user.balance = float(user.payments) - user.debt

    return render_to_response(
        'index.html', {
            'users': users,
            'nb_meals': nb_meals,
            'expenses': expenses,
            'receipts': receipts,
            'balance': balance,
        })