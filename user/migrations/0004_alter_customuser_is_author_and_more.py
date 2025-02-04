# Generated by Django 5.0.3 on 2024-03-14 13:15

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0003_customuser_is_author_customuser_is_manager'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='is_author',
            field=models.BooleanField(default=False, verbose_name='Make User an Author'),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='is_manager',
            field=models.BooleanField(default=False, verbose_name='Make User a Manager'),
        ),
        migrations.AlterField(
            model_name='shelf',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Student'),
        ),
    ]
