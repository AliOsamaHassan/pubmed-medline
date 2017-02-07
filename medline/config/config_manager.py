# author; Ramji Chandrasekaran
# date: 05-Feb-2017
# config file manager

import configparser


class ConfigMgr:

    """Config Manager script to add, delete or modify config entries.
    config entries are used to alter tuning parameters of PubMed clustering, as well as data handling programs.
    config parameters can also be directly edited in the config/default.cfg file"""

    def __init__(self):
        self.cfg_handler = configparser.ConfigParser()

    def create_sections(self, sections):
        for section in sections:
            self.cfg_handler.add_section(section)

    def add_config_entry(self, section, val_dict):
        for key, value in val_dict.items():
            self.cfg_handler.set(section, key, value)

    def save_config_file(self, filename):
        with open(filename, 'w') as file:
            self.cfg_handler.write(file)


if __name__ == "__main__":

    cfg_mgr = ConfigMgr()
    cfg_mgr.create_sections(['input', 'clustering', 'feature-extraction', 'output'])

    cfg_mgr.add_config_entry('input', {'input.file.type': '.txt'})
    cfg_mgr.add_config_entry('input', {'input.filters': 'none'})
    cfg_mgr.add_config_entry('input', {'abstracts.record.separator': "SEGMENTBREAK"})
    cfg_mgr.add_config_entry('input', {'abstracts.parser.content.index': '4'})
    cfg_mgr.add_config_entry('input', {'abstracts.parser.permalink.index': '-2'})
    cfg_mgr.add_config_entry('input', {'abstracts.parser.title.index': '1'})

    cfg_mgr.add_config_entry('clustering', {'clusters.count': '100'})
    cfg_mgr.add_config_entry('clustering', {'iterations.count': '5'})
    cfg_mgr.add_config_entry('clustering', {'cluster.terms.count': '20'})

    cfg_mgr.save_config_file("default.cfg")
