from modeltranslation.translator import TranslationOptions, register
from outher.models import About, Muzeylar, Kutubxona, Olimlar


@register(About)
class AboutTranslationOptions(TranslationOptions):
    fields = ('title', 'description',)


@register(Olimlar)
class OlimlarTranslationOptions(TranslationOptions):
    fields = ('fullname', 'pasition',)


@register(Kutubxona)
class KutubxonaTranslationOptions(TranslationOptions):
    fields = ('title',)


@register(Muzeylar)
class MuzeylarTranslationOptions(TranslationOptions):
    fields = ('title',)


