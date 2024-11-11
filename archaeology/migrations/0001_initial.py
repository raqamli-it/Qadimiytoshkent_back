# Generated by Django 5.0.6 on 2024-10-12 10:16

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Archaeology',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=60)),
                ('title_ru', models.CharField(max_length=60, null=True)),
                ('title_uz', models.CharField(max_length=60, null=True)),
                ('title_en', models.CharField(max_length=60, null=True)),
                ('context', ckeditor.fields.RichTextField(blank=True, null=True)),
                ('context_ru', ckeditor.fields.RichTextField(blank=True, null=True)),
                ('context_uz', ckeditor.fields.RichTextField(blank=True, null=True)),
                ('context_en', ckeditor.fields.RichTextField(blank=True, null=True)),
                ('image', models.FileField(blank=True, null=True, upload_to='image')),
                ('video', models.FileField(blank=True, null=True, upload_to='videos/')),
                ('pasport', models.FileField(blank=True, null=True, upload_to='pasport/')),
                ('video_link', models.URLField(blank=True, null=True)),
                ('link', models.URLField(blank=True, null=True)),
                ('view_count', models.PositiveIntegerField(blank=True, default=0, null=True)),
                ('create', models.DateTimeField(auto_now_add=True)),
                ('update', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'Archaeology',
                'verbose_name_plural': 'Archaeology',
            },
        ),
        migrations.CreateModel(
            name='ArchaeologyPicture',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('image', models.FileField(blank=True, null=True, upload_to='image')),
                ('link', models.URLField(blank=True, null=True, verbose_name='link')),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('name_ru', models.CharField(max_length=100, null=True)),
                ('name_uz', models.CharField(max_length=100, null=True)),
                ('name_en', models.CharField(max_length=100, null=True)),
            ],
            options={
                'verbose_name': 'Category',
                'verbose_name_plural': 'Categories',
            },
        ),
        migrations.CreateModel(
            name='Items',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=60)),
                ('title_ru', models.CharField(max_length=60, null=True)),
                ('title_uz', models.CharField(max_length=60, null=True)),
                ('title_en', models.CharField(max_length=60, null=True)),
                ('context', ckeditor.fields.RichTextField(blank=True, null=True)),
                ('context_ru', ckeditor.fields.RichTextField(blank=True, null=True)),
                ('context_uz', ckeditor.fields.RichTextField(blank=True, null=True)),
                ('context_en', ckeditor.fields.RichTextField(blank=True, null=True)),
                ('video', models.FileField(blank=True, null=True, upload_to='videos/')),
                ('video_link', models.URLField(blank=True, null=True)),
                ('link', models.URLField(blank=True, null=True)),
                ('view_count', models.PositiveIntegerField(blank=True, default=0, null=True)),
                ('image', models.FileField(blank=True, null=True, upload_to='image')),
                ('create', models.DateTimeField(auto_now_add=True)),
                ('update', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'Item',
                'verbose_name_plural': 'Items',
            },
        ),
        migrations.CreateModel(
            name='ItemsPicture',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.FileField(blank=True, null=True, upload_to='image')),
                ('link', models.URLField(blank=True, null=True, verbose_name='link')),
            ],
        ),
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=60)),
                ('title_ru', models.CharField(max_length=60, null=True)),
                ('title_uz', models.CharField(max_length=60, null=True)),
                ('title_en', models.CharField(max_length=60, null=True)),
                ('context', ckeditor.fields.RichTextField(blank=True, null=True)),
                ('context_ru', ckeditor.fields.RichTextField(blank=True, null=True)),
                ('context_uz', ckeditor.fields.RichTextField(blank=True, null=True)),
                ('context_en', ckeditor.fields.RichTextField(blank=True, null=True)),
                ('image', models.FileField(blank=True, null=True, upload_to='image')),
                ('create', models.DateTimeField(auto_now_add=True)),
                ('update', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'New',
                'verbose_name_plural': 'News',
            },
        ),
        migrations.CreateModel(
            name='NewsPicture',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.FileField(blank=True, null=True, upload_to='image')),
            ],
        ),
    ]