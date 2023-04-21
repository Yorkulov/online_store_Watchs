# Generated by Django 4.1 on 2023-04-21 06:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('viewapp', '0006_alter_contactmodel_email_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contactmodel',
            name='email',
            field=models.EmailField(max_length=254),
        ),
        migrations.AlterField(
            model_name='contactmodel',
            name='first_name',
            field=models.CharField(max_length=120),
        ),
        migrations.AlterField(
            model_name='contactmodel',
            name='phone_number',
            field=models.IntegerField(),
        ),
    ]