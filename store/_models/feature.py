from django.db import models
from django.contrib.auth.models import User
from .department import Department


class Feature(models.Model):
    title = models.CharField(max_length=2000)
    description = models.TextField(blank=True, null=True)
    final_price = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    price = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    discount = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    rate = models.FloatField(blank=True, null=True)
    insert_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    department = models.ForeignKey(Department, on_delete=models.CASCADE,
                                   related_name='department_id',
                                   db_column='department')

    def __str__(self):
        return self.title
