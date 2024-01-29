# Generated by Django 4.2 on 2024-01-22 14:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('marlowecensus', '0002_delete_contactform_alter_copy_verification'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='provenanceownership',
            options={'verbose_name': 'Provenance Record', 'verbose_name_plural': 'Provenance Records'},
        ),
        migrations.AddField(
            model_name='copy',
            name='examined',
            field=models.BooleanField(default=False),
        ),
    ]
