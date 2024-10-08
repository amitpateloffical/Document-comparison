# Generated by Django 5.0.7 on 2024-10-04 12:20

import compareapp.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('compareapp', '0013_alter_document_upload_documents'),
    ]

    operations = [
        migrations.AlterField(
            model_name='document',
            name='upload_documents',
            field=models.FileField(upload_to=compareapp.models.Document.upload_to_path),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='image',
            field=models.ImageField(default='user_images/user.png', upload_to='user_images/'),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='phone_number',
            field=models.CharField(blank=True, max_length=15, null=True),
        ),
    ]
