# Generated by Django 5.1.3 on 2024-11-17 18:48

import utils.common.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_alter_user_options_alter_user_managers_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='time_zone',
            field=models.CharField(default='UTC', max_length=63, verbose_name='time zone'),
        ),
        migrations.AlterField(
            model_name='user',
            name='avatar',
            field=models.ImageField(blank=True, null=True, upload_to=utils.common.models.BaseModel.get_file_path, verbose_name='大頭貼'),
        ),
    ]
