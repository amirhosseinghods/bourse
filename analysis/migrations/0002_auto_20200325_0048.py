# Generated by Django 2.2.10 on 2020-03-25 07:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('analysis', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='analyzetag',
            name='posts',
        ),
        migrations.AddField(
            model_name='analyzepost',
            name='tags',
            field=models.ManyToManyField(to='analysis.AnalyzeTag', verbose_name='AnalyzePosts'),
        ),
        migrations.AlterField(
            model_name='analyzecategory',
            name='slug',
            field=models.SlugField(editable=False, max_length=140, verbose_name='Slug'),
        ),
        migrations.AlterField(
            model_name='analyzepost',
            name='height_field',
            field=models.SmallIntegerField(editable=False, verbose_name='Height Field'),
        ),
        migrations.AlterField(
            model_name='analyzepost',
            name='picture',
            field=models.ImageField(height_field=models.SmallIntegerField(editable=False, verbose_name='Height Field'), help_text='picture size: 525x350', max_length=254, upload_to='site/blog', verbose_name='Picture', width_field=models.SmallIntegerField(editable=False, verbose_name='Width Field')),
        ),
        migrations.AlterField(
            model_name='analyzepost',
            name='slug',
            field=models.SlugField(editable=False, max_length=140, verbose_name='Slug'),
        ),
        migrations.AlterField(
            model_name='analyzepost',
            name='width_field',
            field=models.SmallIntegerField(editable=False, verbose_name='Width Field'),
        ),
        migrations.AlterField(
            model_name='analyzetag',
            name='slug',
            field=models.SlugField(editable=False, max_length=140, verbose_name='Slug'),
        ),
    ]
