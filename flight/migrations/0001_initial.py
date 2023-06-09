# Generated by Django 4.2 on 2023-05-07 22:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Airport',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=69)),
            ],
        ),
        migrations.CreateModel(
            name='Cities',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=69)),
            ],
        ),
        migrations.CreateModel(
            name='Flight',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.IntegerField()),
                ('departure', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='departing_flights', to='flight.airport')),
                ('destination', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='arriving_flights', to='flight.airport')),
            ],
        ),
        migrations.AddField(
            model_name='airport',
            name='location',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='airport', to='flight.cities'),
        ),
    ]
