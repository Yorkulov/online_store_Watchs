# Generated by Django 4.1 on 2023-04-17 04:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('viewapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='UsersModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=150)),
                ('last_name', models.CharField(max_length=150)),
                ('email', models.EmailField(max_length=254)),
                ('phone_number', models.IntegerField()),
                ('message', models.TextField()),
            ],
        ),
    ]
