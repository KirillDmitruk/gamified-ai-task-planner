from django.contrib import admin

from progress.models import UserProgress


@admin.register(UserProgress)
class UserProgressAdmin(admin.ModelAdmin):
    list_display = ('user', 'level', 'current_xp')
    search_fields = ('user',)
    list_filter = ('user', 'level')
