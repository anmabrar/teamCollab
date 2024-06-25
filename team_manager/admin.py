from django.contrib import admin
from . import models

@admin.register(models.User)
class UserAdmin(admin.ModelAdmin):
    list_display = ['username', 'email', 'date_joined']
    search_fields = ['username', 'email']
    list_per_page = 10


@admin.register(models.Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display =['name', 'owner', 'created_at']
    search_fields = ['name', 'owner']
    list_per_page = 10

@admin.register(models.ProjectMember)
class ProjectMemberAdmin(admin.ModelAdmin):
    list_display = ['project', 'user', 'role']
    list_editable = ['role']
    search_fields = ['project', 'user']
    list_per_page = 10


@admin.register(models.Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ['title', 'project', 'status', 'priority', 'assigned_to','created_at', 'due_date']
    list_editable = ['status', 'priority']
    search_fields = ['project', 'status', 'priority']
    list_per_page = 10


@admin.register(models.Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['content', 'user', 'task']
    search_fields = ['content', 'user', 'task']
    list_per_page = 10