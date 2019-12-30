from Translations import Translations

extract = Translations("en")
extract.get_translations_and_extract()
extract.load_po_files()
