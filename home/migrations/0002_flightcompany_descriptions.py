# Generated by Django 4.2 on 2023-05-09 04:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='flightcompany',
            name='descriptions',
            field=models.TextField(default=''),
        ),
    ]
