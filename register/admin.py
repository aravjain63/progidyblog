from django.contrib import admin
from .models import Profile

#class UserAdmin(admin.ModelAdmin):
admin.site.register(Profile)
# Register your models here.
