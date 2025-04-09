import importlib
import modules.player_prefs as player_prefs

from constants.general import *

def get_text(text_name, current_player_prefs):
    text = ""

    try:
        lang_module = importlib.import_module(LANG_MODULE + current_player_prefs.lang)
        text = getattr(lang_module, text_name)
    except ModuleNotFoundError:
        print(f"Module '{lang_module}' not found.")
    except AttributeError:
        if current_player_prefs.lang != "en":
            print(f"Text '{text_name}' don't exists in  '{current_player_prefs.lang}' language module, using en instead.")
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