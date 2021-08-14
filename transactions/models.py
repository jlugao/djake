from django.db import models
from django.contrib.auth.models import User

# Create your models here
class Category(models.Model):
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.TextField()
    is_expense = models.BooleanField(default=True)


class SubCategory(models.Model):
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.TextField()
    category = models.ForeignKey(
        Category, on_delete=models.CASCADE, related_name="subcategories"
    )
    is_variable = models.BooleanField(default=True)


class Transaction(models.Model):
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.ForeignKey(
        Category, on_delete=models.CASCADE, related_name="transactions"
    )
    sub_category = models.ForeignKey(
        Category, on_delete=models.CASCADE, related_name="transaction_set"
    )
    value = models.DecimalField(max_digits=6, decimal_places=2, default=0)
    description = models.TextField(blank=True)
    date = models.DateField()
