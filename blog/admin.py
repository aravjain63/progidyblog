from django.contrib import admin
from django.contrib import admin
from .models import Post

class PostAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,      {'fields': ['author_name']}),
        (None,      {'fields': ['title']}),
        ('text', {'fields': ['text']}), 
        ('Date information', {'fields': ['created_date', 'published_date'], 'classes': ['collapse']}),
        
    ]
    list_display = ('title', 'published_date')
    search_fields = ['title', 'published_date']
admin.site.register(Post, PostAdmin)

