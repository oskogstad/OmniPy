import configparser
import shutil
import os


class Config:
    omni_email = False
    from_email = False
    password = False
    smtp_adr = False
    smtp_port = False

    FOLDER_PATH = os.getenv('LOCALAPPDATA') + '/OmniPy'
    FILE_PATH = '/config'
    if not os.path.exists(FOLDER_PATH):
        os.makedirs(FOLDER_PATH)

    def __init__(self):
        config = configparser.ConfigParser()

        if not os.path.isfile(self.FOLDER_PATH + self.FILE_PATH):
            Config.create_config(config)

        config.read(self.FOLDER_PATH + self.FILE_PATH)

        Config.omni_email = config['config']['omni_email']
        Config.from_email = config['config']['from_email']
        Config.password = config['config']['password']
        Config.smtp_adr = config['config']['smtp_adr']
        Config.smtp_port = config['config']['smtp_port']

    @staticmethod
    def delete_config():
        shutil.rmtree(Config.FOLDER_PATH)

    @staticmethod
    def ait():
        return \
            Config.omni_email and \
            Config.from_email and \
            Config.password and \
            Config.smtp_adr and \
            Config.smtp_port

    @staticmethod
    def create_config(config):
        print('Creating config ...')
        config.add_section('config')
        config['config']['omni_email'] = input('OmniFocus sync email: ')
        config['config']['from_email'] = input('Send from email: ')
        config['config']['password'] = input('Email password (stored as clear text): ')
        config['config']['smtp_adr'] = input('SMTP address: ')
        config['config']['smtp_port'] = input('SMTP port: ')

        with open(Config.FOLDER_PATH + Config.FILE_PATH, 'w') as configfile:
            config.write(configfile)

