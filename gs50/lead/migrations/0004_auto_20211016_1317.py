# Generated by Django 3.2.7 on 2021-10-16 07:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lead', '0003_alter_lead_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='lead',
            name='Name',
        ),
        migrations.AddField(
            model_name='lead',
            name='name',
            field=models.CharField(default=True, max_length=200),
        ),
    ]
