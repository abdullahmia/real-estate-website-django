# Generated by Django 3.1.2 on 2021-02-02 08:21

import ckeditor_uploader.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Listings', '0003_auto_20210202_1410'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listing',
            name='description',
            field=ckeditor_uploader.fields.RichTextUploadingField(null=True),
        ),
    ]
