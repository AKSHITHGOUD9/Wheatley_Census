# Generated by Django 4.2 on 2024-01-22 14:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('marlowecensus', '0001_initial'),
    ]

    operations = [
        migrations.DeleteModel(
            name='ContactForm',
        ),
        migrations.AlterField(
            model_name='copy',
            name='verification',
            field=models.CharField(choices=[('U', 'Unverified'), ('V', 'Verified'), ('F', 'False')], default='Unverified', max_length=1),
        ),
    ]
