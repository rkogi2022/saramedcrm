# Generated by Django 3.2.19 on 2023-06-29 10:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('payment', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='implementation',
            name='no_of_days',
            field=models.CharField(blank=True, max_length=20),
        ),
    ]
