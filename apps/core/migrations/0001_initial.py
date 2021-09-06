# Generated by Django 3.2.7 on 2021-09-06 14:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.DecimalField(decimal_places=2, max_digits=15)),
                ('mark', models.CharField(max_length=255)),
                ('model', models.CharField(max_length=255)),
                ('year_manufactured', models.IntegerField()),
                ('mileage', models.IntegerField()),
            ],
        ),
    ]
