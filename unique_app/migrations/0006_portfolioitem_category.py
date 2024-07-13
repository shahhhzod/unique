# Generated by Django 5.0.4 on 2024-05-05 07:23

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('unique_app', '0005_portfolioitem'),
    ]

    operations = [
        migrations.AddField(
            model_name='portfolioitem',
            name='category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='unique_app.category'),
        ),
    ]
