# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Bill',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('date', models.DateField()),
                ('shop', models.CharField(max_length=64)),
                ('amount', models.DecimalField(decimal_places=6, max_digits=15)),
                ('users', models.ManyToManyField(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Meal',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('cook', models.BooleanField()),
                ('maid', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='MealOccurrence',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('name', models.CharField(max_length=64)),
            ],
        ),
        migrations.CreateModel(
            name='UserPayment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('date', models.DateField()),
                ('amount', models.DecimalField(decimal_places=6, max_digits=15)),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='meal',
            name='meal_occurrence',
            field=models.ForeignKey(to='app.MealOccurrence'),
        ),
        migrations.AddField(
            model_name='meal',
            name='user',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterUniqueTogether(
            name='meal',
            unique_together=set([('meal_occurrence', 'user')]),
        ),
    ]
