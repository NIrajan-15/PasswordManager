# Generated by Django 4.0.2 on 2022-02-24 20:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('manager', '0006_account_thumbnail'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='thumbnail',
            field=models.ImageField(blank=True, null=True, upload_to='static/images/'),
        ),
    ]
