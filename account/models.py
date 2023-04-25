from django.db import models
from django.contrib.auth.models import User
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
