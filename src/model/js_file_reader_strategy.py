from os import path
from src.model.reader_strategy import ReaderStrategy


class JSFileReader(ReaderStrategy):
    def _read_file(self):
        js_file = open(self.__file_dir)
        self.__file_contents = js_file.readlines()
        for line in self.__file_contents:
            self._clean_file_contents += line
        js_file.close()

    def is_valid_file(self, new_dir):
        if str(new_dir).endswith(".js"):
            return True

    def is_valid_dir(self, new_dir):
        return path.isfile(new_dir)

    def _set_file_dir(self, new_dir):
        self.__file_dir = new_dir
