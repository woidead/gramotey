# Generated by Django 4.1.7 on 2023-02-25 16:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0007_rename_graduates_graduate'),
    ]

    operations = [
        migrations.CreateModel(
            name='Gallery',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.ImageField(upload_to='', verbose_name='Изображение')),
            ],
        ),
    ]
