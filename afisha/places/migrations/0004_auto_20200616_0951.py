# Generated by Django 3.0.7 on 2020-06-16 06:51

from django.db import migrations, models
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('places', '0003_auto_20200615_1136'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='image',
            options={'ordering': ('sort',)},
        ),
        migrations.AlterModelOptions(
            name='place',
            options={},
        ),
        migrations.AlterField(
            model_name='place',
            name='description_long',
            field=tinymce.models.HTMLField(verbose_name='Long description'),
        ),
        migrations.AlterField(
            model_name='place',
            name='description_short',
            field=models.TextField(verbose_name='Short description'),
        ),
    ]
