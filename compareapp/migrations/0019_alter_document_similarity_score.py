# Generated by Django 5.0.7 on 2024-10-09 06:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('compareapp', '0018_userlogs_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='document',
            name='similarity_score',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]