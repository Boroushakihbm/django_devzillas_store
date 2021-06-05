# Generated by Django 3.1.1 on 2021-06-05 05:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0005_auto_20210605_0957'),
    ]

    operations = [
        migrations.AlterField(
            model_name='department',
            name='parent_department',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='store.department'),
        ),
        migrations.AlterField(
            model_name='feature',
            name='department',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='store.department'),
        ),
    ]
