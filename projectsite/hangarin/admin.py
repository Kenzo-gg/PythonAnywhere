from django.contrib import admin

from .models import Task, Priority, Category, Note, SubTask

@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('task_title', 'status', 'task_deadline', 'task_priority', 'task_category', )
    search_fields = ('task_title', 'task_description', )
    list_filter = ('status', 'task_priority', 'task_category', )

@admin.register(Priority)
class PriorityAdmin(admin.ModelAdmin):
    list_display = ('priority_name',)
    search_fields = ('priority_name',)
    
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('category_name',)
    search_fields = ('category_name',)

@admin.register(Note)
class NoteAdmin(admin.ModelAdmin):  
    list_display = ('parent_task_note', 'note_content', 'created_at',)
    search_fields = ('note_content',)
    list_filter = ('created_at',)

@admin.register(SubTask)
class SubTaskAdmin(admin.ModelAdmin):
    list_display = ('subtask_title', 'subtask_status', 'parent_task_subtask',)
    search_fields = ('subtask_title',)