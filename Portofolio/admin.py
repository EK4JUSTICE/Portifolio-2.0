from django.contrib import admin
from .models import Project, Skill, Profile

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'created_at', 'image_preview')
    list_filter = ('category', 'created_at')
    search_fields = ('title', 'description')
    ordering = ['-created_at']
    readonly_fields = ('image_preview',)

    def image_preview(self, obj):
        if obj.image:
            return f'<img src="{obj.image.url}" style="max-height: 50px; max-width: 50px;" />'
        return "No image"
    image_preview.short_description = 'Image Preview'
    image_preview.allow_tags = True

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('name', 'title', 'email', 'profile_image_preview')
    readonly_fields = ('profile_image_preview', 'created_at', 'updated_at')
    fieldsets = (
        ('Personal Information', {
            'fields': ('name', 'title', 'bio', 'email', 'phone', 'location')
        }),
        ('Profile Image', {
            'fields': ('profile_image', 'profile_image_preview')
        }),
        ('Timestamps', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )

    def profile_image_preview(self, obj):
        if obj.profile_image:
            return f'<img src="{obj.profile_image.url}" style="max-height: 100px; max-width: 100px; border-radius: 50%;" />'
        return "No image"
    profile_image_preview.short_description = 'Profile Image Preview'
    profile_image_preview.allow_tags = True

@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'proficiency')
    list_filter = ('category', 'proficiency')
    search_fields = ('name', 'category')
    ordering = ('category', 'name')
