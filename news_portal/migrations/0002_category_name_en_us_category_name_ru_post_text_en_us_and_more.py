# Generated by Django 4.2.7 on 2024-02-22 09:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news_portal', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='name_en_us',
            field=models.CharField(help_text='Имя категории', max_length=40, null=True, unique=True),
        ),
        migrations.AddField(
            model_name='category',
            name='name_ru',
            field=models.CharField(help_text='Имя категории', max_length=40, null=True, unique=True),
        ),
        migrations.AddField(
            model_name='post',
            name='text_en_us',
            field=models.TextField(null=True, verbose_name='Text'),
        ),
        migrations.AddField(
            model_name='post',
            name='text_ru',
            field=models.TextField(null=True, verbose_name='Text'),
        ),
        migrations.AddField(
            model_name='post',
            name='title_en_us',
            field=models.CharField(max_length=255, null=True, verbose_name='Title'),
        ),
        migrations.AddField(
            model_name='post',
            name='title_ru',
            field=models.CharField(max_length=255, null=True, verbose_name='Title'),
        ),
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.CharField(help_text='Имя категории', max_length=40, unique=True),
        ),
    ]