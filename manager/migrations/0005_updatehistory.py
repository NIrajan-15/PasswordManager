# Generated by Django 4.0.1 on 2022-02-21 19:21

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('manager', '0004_remove_account_thumbnail'),
    ]

    operations = [
        migrations.CreateModel(
            name='UpdateHistory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.EmailField(blank=True, max_length=254, null=True)),
                ('updated_column', models.CharField(blank=True, max_length=200, null=True)),
                ('updated_on', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
    ]
