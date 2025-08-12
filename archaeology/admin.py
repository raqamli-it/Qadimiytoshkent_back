from django.contrib import admin
from archaeology.models import (
    News, NewsPicture, Items, ItemsPicture, ArchaeologyPicture,
     Archaeology, Category
)


class PictureInline(admin.TabularInline):
    extra = 1


class NewsPictureInline(PictureInline):
    model = NewsPicture


class ItemsPictureInline(PictureInline):
    model = ItemsPicture


class ArchaeologyPictureInline(PictureInline):
    model = ArchaeologyPicture


@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ('id', 'order','title_uz')
    search_fields = ('title_uz', 'title_en')
    ordering = ['-order']
    inlines = [NewsPictureInline]
    readonly_fields = ('create', 'update')   # ← shu satr muammoni hal qiladi
    fields = ['title_uz', 'title_en', 'order', 'context_uz', 'context_en', 'image', 'create', 'update']


@admin.register(Items)
class ItemsAdmin(admin.ModelAdmin):
    list_display = ('id', 'title_uz', 'archaeology', 'category')
    search_fields = ('title_uz', 'title_en')
    inlines = [ItemsPictureInline]
    fields = ['title_uz', 'title_en', 'context_uz', 'context_en', 'image', 
              'video_link', 'link', 'archaeology', 'category']
    # autocomplete_fields = ['archaeology', 'category', 'archaeology_type']


@admin.register(Archaeology)
class ArchaeologyAdmin(admin.ModelAdmin):
    list_display = ('id', 'title_uz')
    search_fields = ('title_uz', 'title_en')
    inlines = [ArchaeologyPictureInline]
    fields = ['title_uz', 'title_en', 'context_uz', 'context_en', 'image',
              'video', 'pasport', 'video_link', 'link']


# @admin.register(ArchaeologyType)
# class ArchaeologyTypeAdmin(admin.ModelAdmin):
#     list_display = ('id', 'title', 'image')
#     search_fields = ['title']


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name_uz', 'name_en')
    search_fields = ('name_uz', 'name_en')
    fields = ['name_uz', 'name_en', 'image', 'icon']
