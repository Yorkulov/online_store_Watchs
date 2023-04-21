from django.contrib import admin
from .models import WatchModel, ContactModel

# Register your models here.

class WatchAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'subtitle', 'price']

admin.site.register(WatchModel, WatchAdmin)

admin.site.register(ContactModel)