# Generated by Django 3.2 on 2021-05-09 11:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('healthcare_app', '0008_bookapptmodel_status'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bookapptmodel',
            name='status',
        ),
    ]
