from deep_translator import MyMemoryTranslator

def english_to_french(english_text):
    """ Translate the text input in English to French and return the French text."""
    french_text = MyMemoryTranslator(source="en", target="fr").translate(text=english_text)
    return french_text

def french_to_english(french_text):
    """ Translate the text input in French to English and return the English text."""
    english_text = MyMemoryTranslator(source="fr", target="en").translate(text=french_text)
    return english_text
