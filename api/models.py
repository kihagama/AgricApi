from django.db import models

# Create your models here.
class product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.CharField(max_length=50,choices=[
        ('Fruits', 'Fruits'),
        ('Vegetables', 'Vegetables'),
        ('Animals', 'Animals'),
        ("Birds", "Birds"),
    ]),
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name