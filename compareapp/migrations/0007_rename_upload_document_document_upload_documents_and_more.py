# Generated by Django 5.0.7 on 2024-09-24 06:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('compareapp', '0006_remove_comparisonreport_upload_files_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='document',
            old_name='upload_document',
            new_name='upload_documents',
        ),
        migrations.RemoveField(
            model_name='document',
            name='doc_format',
        ),
        migrations.RemoveField(
            model_name='document',
            name='doc_type',
        ),
    ]
