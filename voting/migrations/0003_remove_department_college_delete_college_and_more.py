# Generated by Django 4.1.7 on 2023-04-20 10:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('voting', '0002_college_department'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='department',
            name='college',
        ),
        migrations.DeleteModel(
            name='College',
        ),
        migrations.DeleteModel(
            name='Department',
        ),
    ]
