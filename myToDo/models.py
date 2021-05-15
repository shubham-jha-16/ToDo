from django.db import models

# Create your models here.
class ToDo(models.Model):
    todo_text = models.CharField(max_length=200)
    added_on = models.DateTimeField(auto_now_add=True) # first date and time
    updated_on = models.DateTimeField(auto_now=True) # updated date and time
    def __str__(self):
        return self.todo_text


    class Meta :
       ordering = ['-added_on']