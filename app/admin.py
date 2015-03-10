"""
Admin
"""
from django.contrib import admin
from django.contrib.auth.models import Group
from app.models import Bill, MealOccurrence, Meal, UserPayment


class BillAdmin(admin.ModelAdmin):
    model = Bill
    list_display = ('date', 'shop', 'amount')


class MealInline(admin.TabularInline):
    model = Meal
    extra = 1


class MealOccurrenceAdmin(admin.ModelAdmin):
    model = MealOccurrence
    list_display = ('name',)
    inlines = (MealInline,)


class UserPaymentAdmin(admin.ModelAdmin):
    model = UserPayment
    list_display = ('date', 'user', 'amount')


admin.site.register(Bill, BillAdmin)
admin.site.register(MealOccurrence, MealOccurrenceAdmin)
admin.site.register(UserPayment, UserPaymentAdmin)

admin.site.unregister(Group)