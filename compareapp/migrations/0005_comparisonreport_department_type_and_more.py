# Generated by Django 5.0.7 on 2024-09-24 04:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('compareapp', '0004_comparisonreport_ai_summary_document_ai_summary'),
    ]

    operations = [
        migrations.AddField(
            model_name='comparisonreport',
            name='department_type',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='comparisonreport',
            name='description',
            field=models.TextField(blank=True, max_length=400, null=True),
        ),
        migrations.AddField(
            model_name='comparisonreport',
            name='short_description',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='comparisonreport',
            name='upload_files',
            field=models.FileField(blank=True, null=True, upload_to='all_files'),
        ),
    ]
