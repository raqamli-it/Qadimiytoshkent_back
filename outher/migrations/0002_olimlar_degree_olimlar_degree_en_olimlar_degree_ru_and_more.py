# Generated by Django 5.2.4 on 2025-07-18 06:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('outher', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='olimlar',
            name='degree',
            field=models.CharField(default=1, max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='olimlar',
            name='degree_en',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='olimlar',
            name='degree_ru',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='olimlar',
            name='degree_uz',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
