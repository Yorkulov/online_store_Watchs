from modeltranslation.translator import register, TranslationOptions, translator
from viewapp.models import WatchModel


@register(WatchModel)
class WatchTranslationOptions(TranslationOptions):
    fields = ('title', 'subtitle', 'about')
