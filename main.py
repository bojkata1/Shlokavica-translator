import os
from transliterate.base import TranslitLanguagePack, registry
from transliterate import translit


class BulgarianLanguagePack(TranslitLanguagePack):
    language_code = "bg"
    language_name = "bulgarian"
    mapping = (
        u"abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ",
        u"абцдефгхижклмнопярстуввхъзАБЦДЕФГХИЖКЛМНОПЯРСТУВВХЪЗ",
    )
    pre_processor_mapping = {
        u"ch": u"ч",
        u"Ch": u"Ч",
        u"CH": u"Ч",
        u"sh": u"ш",
        u"Sh": u"Ш",
        u"SH": u"Ш",
        u"sht": u"щ",
        u"Sht": u"Щ",
        u"SHT": u"Щ",
        u"yu": u"ю",
        u"Yu": u"Ю",
        u"YU": u"Ю",
        u"iu": u"ю",
        u"Iu": u"ю",
        u"IU": u"ю",
        u"tc": u"ц",
        u"Tc": u"Ц",
        u"TC": u"Ц",
        u"ts": u"ц",
        u"Ts": u"Ц",
        u"TS": u"Ц",
    }


registry.register(BulgarianLanguagePack)
all_files = os.listdir(os.getcwd())
for f in all_files:
    f_no_ext = f.split('.')
    ext = f_no_ext.pop()
    if ext in ["exe", "py"]:
        continue
    f_no_ext = ".".join(f_no_ext)
    if f_no_ext:
        new_name = translit(f_no_ext, "bg") + f".{ext}"
        os.rename(f, new_name)
