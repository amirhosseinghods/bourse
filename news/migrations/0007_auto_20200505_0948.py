# Generated by Django 2.2.10 on 2020-05-05 05:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0006_auto_20200503_0506'),
    ]

    operations = [
        migrations.AddField(
            model_name='newspost',
            name='important',
            field=models.BooleanField(default=False, verbose_name='Important news'),
        ),
        migrations.AddField(
            model_name='newspost',
            name='is_shown',
            field=models.BooleanField(default=False, verbose_name='Show this news'),
        ),
    ]
