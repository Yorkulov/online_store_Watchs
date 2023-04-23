from django.contrib import admin
from django.contrib.auth.models import User
from .models import WatchModel, ContactModel, WatchRegistrationModel, WatchBuyModel


# Register your models here.

class WatchAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'subtitle', 'price']
admin.site.register(WatchModel, WatchAdmin)

class WatchBuyAdmin(admin.ModelAdmin):
    list_display = ['watch_number', 'country']
admin.site.register(WatchRegistrationModel, WatchBuyAdmin)

admin.site.register(WatchBuyModel)
admin.site.register(ContactModel)