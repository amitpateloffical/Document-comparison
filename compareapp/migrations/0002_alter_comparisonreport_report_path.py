# Generated by Django 5.0.7 on 2024-08-13 04:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('compareapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comparisonreport',
            name='report_path',
            field=models.TextField(),
        ),
    ]