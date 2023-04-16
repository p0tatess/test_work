from django.contrib import admin
from .models import EducationModule


@admin.register(EducationModule)
class EducationModuleAdmin(admin.ModelAdmin):
    list_display = ('number','name',)
    list_editable = ('name',)

