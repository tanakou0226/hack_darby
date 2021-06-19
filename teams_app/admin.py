from django.contrib import admin

from .models import Teams


@admin.register(Teams)
class UserAdmin(admin.ModelAdmin):
    pass