import importlib

from modules.constants import *

def get_text(text_name):
    lang_module = importlib.import_module(LANG_MODULE + "." + LANG)

    return getattr(lang_module, text_name)