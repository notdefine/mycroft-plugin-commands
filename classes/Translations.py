from os.path import basename
import requests
import polib
import zipfile
import glob
import os


class Translations(object):
    lang = "de"
    EXTRACT_DIR = "../extract"

    def __init__(self, lang):
        self.lang = lang

    # Get ZIP File (en-mycroft-skills.zip)
    def get_translations_and_extract(self):
        data = requests.get("https://translate.mycroft.ai/export/?path=/" + self.lang + "/mycroft-skills/")
        path_to_zip_file = self.lang + '-mycroft-skills.zip'
        open(path_to_zip_file, 'wb').write(data.content)

        with zipfile.ZipFile(path_to_zip_file, 'r') as zip_ref:
            zip_ref.extractall(self.EXTRACT_DIR)

        os.remove(path_to_zip_file)

    # get all mycroft PO files from skills
    def load_po_files(self):
        consolidated_commands = {}

        directory_with_po_files = self.EXTRACT_DIR + "/" + self.lang + '-mycroft-skills/' + self.lang + '/mycroft-skills/'
        print('Read po files from directory ' + directory_with_po_files)
        for file in glob.glob(directory_with_po_files + "*.po"):
            plugin_name = basename(file)[0:-3]
            consolidated_commands[plugin_name] = []
            print('Read commands from plugin: ' + plugin_name)
            po = polib.pofile(
                file
            )
            for po_entry in po:
                # print(po_entry.msgid, po_entry.msgstr)
                consolidated_commands[plugin_name].append(po_entry)

        return consolidated_commands
