# Generated by Django 4.0.4 on 2022-05-16 22:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('email', models.EmailField(max_length=254, null=True, unique=True, verbose_name='Email')),
                ('first_name', models.CharField(max_length=30, unique=True, verbose_name='First name')),
                ('last_name', models.CharField(max_length=30, verbose_name='Last name')),
                ('city', models.CharField(max_length=255, verbose_name='Город')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
