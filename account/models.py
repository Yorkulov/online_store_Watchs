from django.db import models
from django.contrib.auth.models import User
from viewapp.models import WatchModel
# Create your models here.

GENDER_CHOISE = (
    ('male', 'male'),
    ('female', 'female'),
)

class Profile(models.Model):
    user = models.OneToOneField(User,
                                on_delete=models.CASCADE,
                                null=True)
    date_of_birth = models.DateField(blank=True, null=True)
    gender = models.CharField(max_length=13, choices=GENDER_CHOISE, default='male')
    image = models.ImageField(upload_to='account/', blank=True, null=True)

    def __str__(self):
        return self.user.username
    

class ContactModel(models.Model):
    first_name = models.CharField(max_length=120, blank=False)
    last_name = models.CharField(max_length=120)
    email = models.EmailField(blank=False)
    phone_number = models.IntegerField(blank=False)
    message = models.TextField()

    def __srt__(self):
        return self.email
    
class CommentModel(models.Model):
    user = models.ForeignKey(User,
                             related_name='comments',
                             on_delete=models.CASCADE)
    watch = models.ForeignKey(WatchModel,
                              related_name='comments',
                              default=0,
                              blank=True,
                              on_delete=models.CASCADE)
    text = models.TextField()
    created_time = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=True)

    class Meta:
        ordering = ['-created_time'] # saralash

    def __str__(self):
        return f"User: {User.username}, Product {WatchModel.title}"
