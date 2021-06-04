from django.db import models
from django.contrib.auth.models import User


class AbstractDepartment(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    parent_department = models.ForeignKey('self', on_delete=models.CASCADE, blank=True, null=True)
    insert_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True, blank=True, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
