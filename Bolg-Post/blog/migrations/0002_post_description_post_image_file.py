# Generated by Django 4.2 on 2023-05-07 05:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='description',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='post',
            name='image_file',
            field=models.ImageField(null=True, upload_to='images/'),
        ),
    ]
