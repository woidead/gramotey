# Generated by Django 4.1.7 on 2023-02-24 08:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0006_graduates_student_delete_gallery_and_more'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Graduates',
            new_name='Graduate',
        ),
    ]
