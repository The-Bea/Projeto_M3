from django.db import models
from django.contrib.auth.models import User


class Book(models.Model):
    title = models.CharField(max_length=200)
<<<<<<< HEAD:bookstore/models.py
    author = models.CharField(max_length=150)

    price = models.DecimalField(max_digits=10, decimal_places=2)
=======
    author = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=5, decimal_places=2)
>>>>>>> f16a1a5 (configurando autenticação):bookstore-api/bookstore/models.py
    edition = models.IntegerField()

    def __str__(self):
        return self.title


class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    
    def __str__(self):
        return f"Order {self.id}"