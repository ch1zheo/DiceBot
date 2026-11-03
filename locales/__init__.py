from . import en, ru

DEFAULT_LANGUAGE = "en"
TRANSLATIONS = {"en": en.TEXTS, "ru": ru.TEXTS}
DICE_BUTTON_TEXTS = frozenset(texts["dice_button"] for texts in TRANSLATIONS.values())


def detect_language(language_code: str | None) -> str:
    code = (language_code or "").split("-")[0].lower()
    return code if code in TRANSLATIONS else DEFAULT_LANGUAGE


def get_text(language_code: str | None, key: str, **kwargs) -> str:
    return TRANSLATIONS[detect_language(language_code)][key].format(**kwargs)
