# Generated by Django 4.0.1 on 2022-03-23 18:26

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('video', '0009_alter_video_date_posted'),
    ]

    operations = [
        migrations.AlterField(
            model_name='video',
            name='date_posted',
            field=models.DateTimeField(default=datetime.datetime(2022, 3, 23, 18, 26, 46, 56771, tzinfo=utc), editable=False),
        ),
    ]
