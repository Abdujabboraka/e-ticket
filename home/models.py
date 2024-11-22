from django.db import models

class Ticket(models.Model):
    title = models.CharField(max_length=200)  
    description = models.TextField() 
    created_at = models.DateTimeField(auto_now_add=True) 
    updated_at = models.DateTimeField(auto_now=True)  
    status_choices = [
        ('open', 'Open'),
        ('closed', 'Closed'),
        ('in_progress', 'In Progress'),
    ]
    status = models.CharField(max_length=20, choices=status_choices, default='open')  
    
    def __str__(self):
        return self.title  
        