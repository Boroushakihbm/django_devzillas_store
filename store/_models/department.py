from django.db import models
from django.contrib.auth.models import User


class Department(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(null=True,
                                   blank=True)
    parent_department = models.ForeignKey('self',
                                          on_delete=models.CASCADE,
                                          blank=True,
                                          null=True,
                                          related_name='parent_id',
                                          db_column='parent_department'
                                          )
    insert_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User,
                             on_delete=models.CASCADE)

    def __str__(self):
        return self.title
