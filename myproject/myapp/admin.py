from django.contrib import admin

# Register your models here.

from .models import UserSubmission

admin.site.register(UserSubmission)
# admin.py

from django.contrib import admin
from .models import UserSubmission

class CandidateAdmin(admin.ModelAdmin):
    list_display = ('name', 'resume_link')

    def resume_link(self, obj):
        if obj.resume:
            return f"<a href='{obj.resume.url}' download>Скачать резюме</a>"
        return "Нет файла"
    resume_link.allow_tags = True  # Для старых версий Django (ниже 2.0)
    resume_link.short_description = 'Резюме'

