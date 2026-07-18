from django.contrib import admin

from app.models import Post


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'email', 'created_at')
    ordering = ('-created_at',)