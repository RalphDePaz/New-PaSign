# Generated by Django 4.2.7 on 2023-11-23 01:09

import app.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0007_signaturefile_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='currentsignature',
            name='signature_files',
        ),
        migrations.AlterField(
            model_name='currentsignature',
            name='user_data',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='app.userdata'),
        ),
        migrations.RemoveField(
            model_name='oldsignature',
            name='signature_files',
        ),
        migrations.AlterField(
            model_name='oldsignature',
            name='user_data',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='app.userdata'),
        ),
        migrations.RemoveField(
            model_name='userdata',
            name='signature_files',
        ),
        migrations.DeleteModel(
            name='SignatureFile',
        ),
        migrations.AddField(
            model_name='currentsignature',
            name='signature_files',
            field=models.FileField(blank=True, null=True, upload_to=app.models.get_user_signature_path),
        ),
        migrations.AddField(
            model_name='oldsignature',
            name='signature_files',
            field=models.FileField(blank=True, null=True, upload_to=app.models.get_user_signature_path),
        ),
        migrations.AddField(
            model_name='userdata',
            name='signature_files',
            field=models.FileField(blank=True, null=True, upload_to=app.models.get_user_signature_path),
        ),
    ]
