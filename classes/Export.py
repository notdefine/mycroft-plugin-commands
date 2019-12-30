from mdutils import MdUtils
from var_dump import var_dump


class Export(object):
    OUTPUT_DIR = "autogenerated/"

    def __init__(self, translations: dict):
        self.translations = translations

    def write_to_markdown(self, filename: str):

        mdFile = MdUtils(
            file_name=self.OUTPUT_DIR + filename,
            title='Mycroft.ai commands (autogenerated from po files)'
        )

        for plugin_name in self.translations:
            mdFile.new_header(level=1, title=plugin_name)
            mdFile.new_line()
            self.add_table(mdFile, self.translations[plugin_name])

        mdFile.create_md_file()

    def add_table(self, md_file: MdUtils, translations):
        table_entries = ["Intention", "Command", "Msg Id"]

        for translation in translations:
            intent = translation.occurrences[0][0] + ":" + translation.occurrences[0][1]

            # print(translation.msgid, translation.msgstr)
            table_entries.extend([intent, translation.msgstr, translation.msgid])

        md_file.new_table(columns=3, rows=len(translations) + 1, text=table_entries, text_align='left')
