# Generated by Django 3.1.1 on 2021-06-05 20:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0012_department_test'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='department',
            name='test',
        ),
    ]