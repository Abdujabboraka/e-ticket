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
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='tickets')  
    price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)  

    def __str__(self):
        return f'{self.title} - {self.status}'
