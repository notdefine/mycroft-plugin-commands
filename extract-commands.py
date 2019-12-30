from var_dump import var_dump

from classes.Export import Export
from classes.Translations import Translations

export_languages = ["en", "de"]

for language in export_languages:
    extract = Translations(language)
    extract.get_translations_and_extract()
    commands = extract.load_po_files()

    export = Export(commands)
    export.write_to_markdown('COMMANDS-' + language)
