from django.contrib import admin
from .models import Project

class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at')
    list_filter = ('created_at',)
    search_fields = ('title', 'description')
    fieldsets = (
        ('Project Information', {
            'fields': ('title', 'description', 'technologies')
        }),
        ('Media & Links', {
            'fields': ('image', 'link')
        }),
    )

admin.site.register(Project, ProjectAdmin)
