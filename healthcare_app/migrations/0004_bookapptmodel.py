# Generated by Django 3.2 on 2021-05-08 09:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('healthcare_app', '0003_auto_20210508_1438'),
    ]

    operations = [
        migrations.CreateModel(
            name='BookapptModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=10)),
                ('contactno', models.CharField(max_length=10)),
                ('appt', models.CharField(max_length=10)),
            ],
        ),
    ]
