# Generated by Django 4.2.7 on 2023-11-12 20:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='userdata',
            name='signature_file',
            field=models.ImageField(default='path/to/default/image.jpg', upload_to='user_signatures/'),
        ),
    ]
