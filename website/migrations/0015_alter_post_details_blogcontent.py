# Generated by Django 4.0.3 on 2022-05-30 06:42

from django.db import migrations
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0014_delete_comment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post_details',
            name='BlogContent',
            field=tinymce.models.HTMLField(),
        ),
    ]
