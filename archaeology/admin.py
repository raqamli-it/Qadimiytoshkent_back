from django.contrib import admin

from .models import Archaeology, Items, News, ArchaeologyPicture, \
    NewsPicture, ItemsPicture, Category, ArchaeologyType


class NewsPictureTabularInline(admin.TabularInline):
    model = NewsPicture
    fields = ['image']


@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ('id', 'title_uz',)
    # inlines = [NewsVideoTabularInline, NewsPictureTabularInline]
    inlines = [NewsPictureTabularInline]
    fields = ['title_uz', 'title_en', 'context_uz', 'context_en', 'image', ]


class Items_PictureInline(admin.TabularInline):
    model = ItemsPicture
    extra = 1  # Ko'proq qatorlar yaratish uchun optional


class ArchaeologyPictureInline(admin.TabularInline):
    model = ArchaeologyPicture
    extra = 1


@admin.register(ArchaeologyType)
class ArchaeologyTypeAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'image')
    search_fields = ['title']


@admin.register(Items)
class ItemsAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'archaeology', 'category', 'archaeology_type',)  # Modeldagi asosiy fieldlar
    inlines = [Items_PictureInline]  # Inline modellar qo'shildi
    fields = ('title_uz', 'title_en', 'context_uz', 'context_en', 'image', 'video', 'video_link', 'link', 'archaeology',
              'category', 'archaeology_type',)
    autocomplete_fields = ['archaeology', 'category',
                           'archaeology_type', ]  # ForeignKey bo'lgan maydonlar uchun autocomplete

    def archaeology(self, obj):
        return obj.archaeology

    def category(self, obj):
        return obj.category


@admin.register(Archaeology)
class ArchaeologyAdmin(admin.ModelAdmin):
    list_display = ('id', 'title',)
    search_fields = ('title',)
    inlines = [ArchaeologyPictureInline]  # Inline model qo'shildi
    fields = ['title_uz', 'title_en', 'context_uz', 'context_en', 'image', 'video', 'pasport', 'video_link', 'link']


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name_uz', 'name_en')
    search_fields = ('name_uz', 'name_en')
    fields = ['name_uz', 'name_en', 'image', 'icon', 'archaeology_type']

