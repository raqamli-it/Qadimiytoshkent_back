from django.db import models
from ckeditor.fields import RichTextField
from django.contrib.auth import get_user_model

User = get_user_model()


class Archaeology(models.Model):
    title = models.CharField(max_length=60)
    context = RichTextField(blank=True, null=True)
    image = models.FileField(upload_to='image', blank=True, null=True)
    video = models.FileField(upload_to='videos/', blank=True, null=True)
    pasport = models.FileField(upload_to='pasport/', blank=True, null=True)
    video_link = models.URLField(blank=True, null=True)
    link = models.URLField(blank=True, null=True)
    view_count = models.PositiveIntegerField(default=0, blank=True, null=True)
    create = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Archaeology'
        verbose_name_plural = 'Archaeology'

    def __str__(self):
        return self.title_uz


class ArchaeologyPicture(models.Model):
    title = models.CharField(max_length=200)
    image = models.FileField(upload_to='image', blank=True, null=True)
    link = models.URLField(verbose_name='link', blank=True, null=True)
    name = models.ForeignKey(Archaeology, on_delete=models.CASCADE, related_name='archaeologyPicture',
                             blank=True, null=True)


# class ArchaeologyType(models.Model):
#     title = models.CharField(max_length=60)
#     image = models.FileField(upload_to='image', blank=True, null=True)

#     def __str__(self):
#         return self.title


class Category(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='image/', blank=True, null=True)
    icon = models.ImageField(upload_to='icon/', blank=True, null=True)
    # archaeology_type = models.ForeignKey(ArchaeologyType, null=True, blank=True, on_delete=models.CASCADE)  # Make optional

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name_uz


class Items(models.Model):
    title = models.CharField(max_length=60)
    context = RichTextField(blank=True, null=True)
    video_link = models.URLField(blank=True, null=True)
    link = models.URLField(blank=True, null=True)
    view_count = models.PositiveIntegerField(default=0, blank=True, null=True)
    image = models.FileField(upload_to='image', blank=True, null=True)
    archaeology = models.ForeignKey(Archaeology, on_delete=models.CASCADE, related_name='items_set', blank=True,
                                    null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='items', blank=True, null=True)
    create = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)
    

    class Meta:
        verbose_name = 'Item'
        verbose_name_plural = 'Items'

    def __str__(self):
        return self.title_uz


class ItemsPicture(models.Model):
    image = models.FileField(upload_to='image', blank=True, null=True)
    link = models.URLField(verbose_name='link', blank=True, null=True)
    item = models.ForeignKey(Items, on_delete=models.CASCADE, related_name='picture_items')


class News(models.Model):
    title = models.CharField(max_length=60)
    context = RichTextField(blank=True, null=True)
    image = models.FileField(upload_to='image', blank=True, null=True)
    create = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'New'
        verbose_name_plural = 'News'

    def __str__(self):
        return self.title


class NewsPicture(models.Model):
    image = models.FileField(upload_to='image', blank=True, null=True)
    news = models.ForeignKey(News, on_delete=models.CASCADE, related_name='news_picture', )
