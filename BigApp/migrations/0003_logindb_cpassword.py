# Generated by Django 5.0.4 on 2024-05-28 10:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BigApp', '0002_logindb'),
    ]

    operations = [
        migrations.AddField(
            model_name='logindb',
            name='cpassword',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]