# Generated by Django 4.2 on 2024-03-04 14:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('marlowecensus', '0005_alter_copy_collated_by_alter_copy_examined_by_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='copy',
            old_name='cen',
            new_name='MC',
        ),
        migrations.AddField(
            model_name='title',
            name='notes',
            field=models.TextField(blank=True, default='', null=True),
        ),
    ]
