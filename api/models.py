from django.db import models

# Create your models here.
class product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.CharField(max_length=20, choices=[
        ('Fruits', 'Fruits'),
        ('Vegetables', 'Vegetables'),
        ('Animals', 'Animals'),
        ("Birds", "Birds")
    ], blank=True, null=True)
    Image = models.ImageField(upload_to='products/',blank=True, null=True)
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
class workers(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    position = models.CharField(max_length=100)
    def __str__(self):
        return f"{self.first_name} {self.last_name}"