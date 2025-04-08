import importlib

from modules.constants.general import *

def get_text(text_name):
    text = ""

    try:
        lang_module = importlib.import_module(LANG_MODULE + LANG)
        text = getattr(lang_module, text_name)
    except ModuleNotFoundError:
        print(f"Module '{lang_module}' not found.")
    except AttributeError:
        if LANG != "en":
            print(f"Text '{text_name}' don't exists in  '{LANG}' language module, using en instead.")
            try :
                en_lang_module = importlib.import_module(LANG_MODULE + "en")
                text = getattr(en_lang_module, text_name)
            except AttributeError :
                text = "ERROR : TEXT NOT FOUND"
                print(f"Text '{text_name}' don't exists in 'en' language module.")
        else :
            text = "ERROR : TEXT NOT FOUND"
            print(f"Text '{text_name}' don't exists in 'en' language module.")

    return text