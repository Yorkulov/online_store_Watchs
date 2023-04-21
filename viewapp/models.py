from django.db import models
from django.shortcuts import render
from django.urls import reverse

# Create your models here.


class WatchModel(models.Model):
    title = models.CharField(max_length=150)
    subtitle = models.CharField(max_length=150)
    price = models.IntegerField()
    about = models.TextField()
    image_one = models.ImageField(upload_to="watchs/")
    image_two = models.ImageField(upload_to="watchs/", blank=True)
    image_three = models.ImageField(upload_to="watchs/", blank=True)
    added_time = models.TimeField(auto_now=True)

    def __str__(self):
        return self.title
    
    def get_absolute_url(self, pk):
        return reverse("watch_detail", kwargs={"pk": self.pk})
    

class ContactModel(models.Model):
    first_name = models.CharField(max_length=120, blank=False)
    last_name = models.CharField(max_length=120)
    email = models.EmailField(blank=False)
    phone_number = models.IntegerField(blank=False)
    message = models.TextField()

    def __srt__(self):
        return self.email
    