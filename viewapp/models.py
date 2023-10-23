from django.db import models
from django.shortcuts import render
from django.urls import reverse
from django.contrib.auth.models import User
from django.db.models import Avg
# Create your models here.


class WatchModel(models.Model):
    title = models.CharField(max_length=150)
    subtitle = models.CharField(max_length=150)
    price = models.IntegerField()
    about = models.TextField()
    image_one = models.ImageField(upload_to="watchs/")
    image_two = models.ImageField(upload_to="watchs/", blank=True)
    image_three = models.ImageField(upload_to="watchs/", blank=True)
    added_time = models.DateTimeField(auto_now=True)
    view_count = models.IntegerField(default=0)

    def __str__(self):
        return self.title
    
    def get_absolute_url(self, pk):
        return reverse("watch_detail", kwargs={"pk": self.pk})
    

# class ContactModel(models.Model):
#     first_name = models.CharField(max_length=120, blank=False)
#     last_name = models.CharField(max_length=120)
#     email = models.EmailField(blank=False)
#     phone_number = models.IntegerField(blank=False)
#     message = models.TextField()

#     def __srt__(self):
#         return self.email
    

class WatchRegistrationModel(models.Model):
    user = models.ForeignKey(User, 
                            related_name = "watch_user_register", 
                            on_delete=models.CASCADE)
    watch = models.ForeignKey(WatchModel, 
                            related_name = "watch_register",
                            on_delete=models.CASCADE)
    watch_number = models.SmallIntegerField()
    country = models.CharField(max_length=100)
    address = models.TextField()


    def __srt__(self):
        return self.user.username
    

class WatchBuyModel(models.Model):
    registration = models.ForeignKey(WatchRegistrationModel,
                                     related_name = "watch_buy",
                                     on_delete=models.CASCADE)
    card_number = models.CharField(max_length=16)
    check_code = models.SmallIntegerField()

    def __str__(self):
        return self.registration.user.username
    
