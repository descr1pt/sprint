# Generated by Django 4.2.7 on 2023-11-09 13:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('perevelapp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='images',
            name='image_id',
        ),
        migrations.AddField(
            model_name='images',
            name='image',
            field=models.ImageField(default='Moench_2339.jpg', upload_to=''),
        ),
    ]