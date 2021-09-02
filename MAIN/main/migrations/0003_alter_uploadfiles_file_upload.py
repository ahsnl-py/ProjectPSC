# Generated by Django 3.2.5 on 2021-08-31 22:06

from django.db import migrations, models
import main.utils


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_auto_20210822_1300'),
    ]

    operations = [
        migrations.AlterField(
            model_name='uploadfiles',
            name='file_upload',
            field=models.FileField(blank=True, null=True, upload_to='post_media', validators=[main.utils.validate_file_extension]),
        ),
    ]