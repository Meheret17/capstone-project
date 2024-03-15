# Generated by Django 5.0.3 on 2024-03-15 13:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0006_alter_customuser_options_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='is_author',
            field=models.BooleanField(default=False, verbose_name='is an Author'),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='is_manager',
            field=models.BooleanField(default=False, verbose_name='is a Manager'),
        ),
    ]
