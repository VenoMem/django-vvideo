# Generated by Django 4.0.1 on 2022-02-24 12:18

import datetime
import django.core.validators
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('video', '0003_alter_video_date_posted_alter_video_film'),
    ]

    operations = [
        migrations.AlterField(
            model_name='video',
            name='date_posted',
            field=models.DateTimeField(default=datetime.datetime(2022, 2, 24, 12, 18, 39, 362072, tzinfo=utc), editable=False),
        ),
        migrations.AlterField(
            model_name='video',
            name='film',
            field=models.FileField(upload_to='videos/', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['mp4', 'mkv', 'avi', 'webm'])]),
        ),
    ]
