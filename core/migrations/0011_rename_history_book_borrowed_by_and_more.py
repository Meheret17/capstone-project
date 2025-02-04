# Generated by Django 5.0.3 on 2024-03-17 10:32

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0010_alter_book_author'),
    ]

    operations = [
        migrations.RenameField(
            model_name='book',
            old_name='history',
            new_name='borrowed_by',
        ),
        migrations.RemoveField(
            model_name='book',
            name='cover_page',
        ),
        migrations.AddField(
            model_name='book',
            name='coverpage',
            field=models.ImageField(null=True, upload_to='coverpages/'),
        ),
        migrations.AlterField(
            model_name='review',
            name='book',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reviews', to='core.book'),
        ),
    ]
