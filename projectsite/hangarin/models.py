from django.db import models

class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True, db_index=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

class Priority(BaseModel):
    priority_id = models.IntegerField(primary_key=True)
    priority_name = models.CharField(max_length=150)

    def __str__(self): return self.priority_name

class Category(BaseModel):
    category_id = models.IntegerField(primary_key=True)
    category_name = models.CharField(max_length=150)

    def __str__(self): return self.category_name

class Task(BaseModel):
    task_id = models.IntegerField(primary_key=True)
    task_title = models.CharField(max_length=150)
    task_description = models.TextField(max_length=500)
    task_deadline = models.DateTimeField()
    status = models.CharField(max_length=50,choices=[("Pending", "Pending"),("In Progress ", "In Progress"),("Completed", "Completed"),],default="pending")
    task_category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True, related_name='category')
    task_priority = models.ForeignKey(Priority, on_delete=models.CASCADE, null=True, related_name='priority')

    def __str__(self): return self.task_title

class SubTask(BaseModel):
    subtask_id = models.IntegerField(primary_key=True)
    parent_task_subtask = models.ForeignKey(Task, on_delete=models.CASCADE, related_name='subtasks')
    subtask_title = models.CharField(max_length=255)
    subtask_status = models.CharField(max_length=50,choices=[("Pending", "Pending"),("In Progress ", "In Progress"),("Completed", "Completed"),],default="pending")

    def __str__(self): return self.subtask_title

class Note(BaseModel):
    note_id = models.IntegerField(primary_key=True)
    parent_task_note = models.ForeignKey(Task, on_delete=models.CASCADE, related_name='notes')
    note_content = models.TextField(max_length=500)

    def __str__(self): return self.note_content



