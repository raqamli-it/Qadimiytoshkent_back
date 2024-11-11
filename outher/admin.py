from django.contrib import admin
from .models import About, Muzeylar, Kutubxona, Olimlar


@admin.register(About)
class AboutAdmin(admin.ModelAdmin):
    list_display = ('title_uz',)
    fields = ('title_uz', 'title_en', 'description_uz', 'description_en',)


@admin.register(Olimlar)
class OlimlarAdmin(admin.ModelAdmin):
    list_display = ('fullname_uz',)
    fields = ('fullname_uz', 'fullname_en', 'pasition_uz', 'pasition_en', 'image',)


@admin.register(Muzeylar)
class MuzeylarAdmin(admin.ModelAdmin):
    list_display = ('title_uz',)
    fields = ('title_uz', 'title_en', 'image', 'video', 'video_link', 'link',)


@admin.register(Kutubxona)
class KutubxonaAdmin(admin.ModelAdmin):
    list_display = ('title_uz',)
    fields = ('title_uz', 'title_en', 'image', 'file', 'downloads',)
