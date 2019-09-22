from django.contrib import admin
from .models import Post
# Register your models here.

class PostAdmin(admin.ModelAdmin):
    readonly_fields = ('created','modified')
    search_fields = ('post', 'teacher__full_name',)

admin.site.register(Post,PostAdmin)
