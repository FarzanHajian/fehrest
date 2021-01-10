from . import validator
from . import errors
from . import helper
import os
from os import path
from zipfile import ZipFile


class Initializer:
    def __init__(self, *, site_name: str, path: str):
        self.__site_name = site_name
        self.__init_path = path

    def initialize(self):
        if not validator.validate_initialization_path(self.__init_path):
            errors.raise_error(errors.INVALID_INIT_DIR)
        self.__create_scaffold()
        self.__apply_site_settings()
        self.__print_sucess_message()

    def __create_scaffold(self):
        os.makedirs(self.__init_path, exist_ok=True)
        with ZipFile('fehrest/scaffold.zip', 'r') as zip:
            zip.extractall(self.__init_path)

    def __apply_site_settings(self):
        helper.apply_template_values(
            path.join(self.__init_path, 'pelicanconf.py'),
            SiteName=self.__site_name
        )

        helper.apply_template_values(
            path.join(self.__init_path, 'content/pages', 'home.md'),
            add_quotes=False,
            Title=self.__site_name
        )

    def __print_sucess_message(self):
        files_path = path.join(self.__init_path, 'content/files')
        print('The site is initialized sucessfully.')
        print(
            f'Put your files in "{path.normpath(files_path)}" subfolders and')
        print(
            f'   publish your site using fehrest --publish "{path.normpath(self.__init_path)}"')
