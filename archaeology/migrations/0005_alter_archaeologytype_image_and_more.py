# Generated by Django 5.0.1 on 2024-10-27 10:00

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('archaeology', '0004_category_archaeology_type_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='archaeologytype',
            name='image',
            field=models.FileField(blank=True, null=True, upload_to='image'),
        ),
        migrations.AlterField(
            model_name='archaeologytype',
            name='title',
            field=models.CharField(max_length=60),
        ),
        migrations.AlterField(
            model_name='category',
            name='archaeology_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='archaeology.archaeologytype'),
        ),
        migrations.AlterField(
            model_name='category',
            name='icon',
            field=models.ImageField(blank=True, null=True, upload_to='icon/'),
        ),
        migrations.AlterField(
            model_name='category',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='image/'),
        ),
    ]