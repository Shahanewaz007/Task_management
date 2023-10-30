from django.db import models

CHOICES = [
    ('low', 'Low'),
    ('medium', 'Medium'),
    ('high', 'High'),
]
class Task(models.Model):    
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=300)
    description = models.TextField()
    due_date = models.DateField()
    priority = models.CharField(max_length=10, choices=CHOICES)
    complete = models.BooleanField(default=False)
    creation_date = models.DateField(auto_now_add=True)
    last_updated = models.DateField(auto_now=True)
    
