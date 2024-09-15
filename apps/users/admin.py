from django.contrib import admin
from .models import *



@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    pass


@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    pass


@admin.register(ActionLog)
class ActionLogAdmin(admin.ModelAdmin):
    pass
