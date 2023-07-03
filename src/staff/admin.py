from django.contrib import admin
from .models import Profile

class ProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'phone', 'country', 'city', 'index', 'address1', 'address2', 'other']

admin.site.register(Profile, ProfileAdmin)