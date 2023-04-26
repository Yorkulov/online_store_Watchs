# Generated by Django 4.1.7 on 2023-04-26 03:51

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('viewapp', '0011_delete_contactmodel'),
        ('account', '0003_contactmodel'),
    ]

    operations = [
        migrations.CreateModel(
            name='CommentModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField()),
                ('creted_time', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_commment', to=settings.AUTH_USER_MODEL)),
                ('watch', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='watch_comment', to='viewapp.watchmodel')),
            ],
        ),
    ]