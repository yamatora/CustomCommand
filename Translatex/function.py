#　Functinos to translate en to ja
#   Deep-translator
from deep_translator import GoogleTranslator
def get_translation_google(text:str, source="en", target="ja") -> str:
    return GoogleTranslator(source=source, target=target).translate(text)

#   DeepL
from deepl.translator import Translator
from secret import AUTH_DEEPL
def get_translation_deepl(text:str, target="ja") -> str:
    translator: Translator = Translator(AUTH_DEEPL)
    return translator.translate_text(text, target_lang=target).text