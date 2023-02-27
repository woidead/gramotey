# Generated by Django 4.1.7 on 2023-02-23 07:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Фамилия, Имя')),
                ('description', models.CharField(max_length=100, verbose_name='Должность')),
                ('image', models.ImageField(upload_to='', verbose_name='Изображение')),
            ],
        ),
    ]
