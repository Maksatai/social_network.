from django.contrib import admin
from .models import Profile

# class ProfileAdmin(admin.ModelAdmin):
#     list_display = ['user','avatar','bio','city', 'birth_date','gender','relationship']

admin.site.register(Profile)
