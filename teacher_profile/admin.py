from django.contrib import admin
from .models import Teacher_profile


class Teacher_profileAdmin(admin.ModelAdmin):
        search_fields = ('full_name',)

admin.site.register(Teacher_profile, Teacher_profileAdmin)


