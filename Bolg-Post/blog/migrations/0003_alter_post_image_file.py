# Generated by Django 4.2 on 2023-05-07 05:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_post_description_post_image_file'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='image_file',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
    ]