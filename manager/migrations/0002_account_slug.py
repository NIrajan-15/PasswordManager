# Generated by Django 4.0.2 on 2022-02-10 05:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('manager', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='account',
            name='slug',
            field=models.SlugField(default=models.CharField(max_length=50)),
        ),
    ]
