import json

# key name pairs for all supported langues
languages = {
    'en': 'English'
}

# dictionary of translation dictionaries by language
locales_dict = {};

# ========================================================
# Returns the name of a language, based on code, in that lanuage
# ========================================================
def get_lang_name(code):
    if languages[code] is not None:
        return languages[code]
    else:
        return '<Unkown>'

# ========================================================
# Populates dictionary of language
# ========================================================
def load_locales():
    for key in languages.keys():
        with open(f'locales/{key}.json') as f:
            locales_dict[key] = json.load(f)

# ========================================================
# Returns translated text from dictionary
# ========================================================
def get(lang_code, text_key):
    return locales_dict[lang_code][text_key]