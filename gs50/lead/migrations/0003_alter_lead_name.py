# Generated by Django 3.2.7 on 2021-10-16 07:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lead', '0002_lead_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lead',
            name='Name',
            field=models.CharField(max_length=300),
        ),
    ]