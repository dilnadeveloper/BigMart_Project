# Generated by Django 5.0.4 on 2024-05-31 08:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BigApp', '0004_remove_logindb_cpassword_logindb_confirm_password'),
    ]

    operations = [
        migrations.CreateModel(
            name='cartdb',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('usename', models.CharField(blank=True, max_length=100, null=True)),
                ('proname', models.CharField(blank=True, max_length=100, null=True)),
                ('quantity', models.CharField(blank=True, max_length=100, null=True)),
                ('price', models.IntegerField(blank=True, null=True)),
            ],
        ),
    ]
