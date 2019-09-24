from django.contrib import admin
from django.contrib import admin
from .models import Post

class PostAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,      {'fields': ['title']}),
        ('text', {'fields': ['text']}), 
        ('Date information', {'fields': ['created_date', 'pub_date'], 'classes': ['collapse']}),
    ]
    list_display = ('title', 'pub_date')
    search_fields = ['title', 'pub_date']
admin.site.register(Post, PostAdmin)

