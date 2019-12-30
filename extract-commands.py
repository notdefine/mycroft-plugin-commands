from var_dump import var_dump

from classes.Export import Export
from classes.Translations import Translations

export_languages = [
    "ar", "ast", "bn", "bs", "bg", "ca", "zh_CN", "hr", "cs", "da", "nl", "en", "en_GB", "eo", "fil",
    "fr", "gd", "de", "el", "cnh-mm", "haw", "he", "hi", "hu", "is", "id", "ga", "it", "ja", "kab",
    "ko", "lt", "ml", "mi", "mr", "cnr", "nb", "nn", "oc", "pl", "pt", "pt_BR", "pa", "ro", "ru", "sco",
    "sl", "es_LM", "es", "sv", "te", "templates", "tr", "uk", "vi", "cy", "dha"
]

for language in export_languages:
    extract = Translations(language)
    extract.get_translations_and_extract()
    commands = extract.load_po_files()

    export = Export(commands)
    export.write_to_markdown('COMMANDS-' + language)
