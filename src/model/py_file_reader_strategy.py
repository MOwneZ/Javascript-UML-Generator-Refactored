from os import path
from src.model.reader_strategy import ReaderStrategy


class PYFileReader(ReaderStrategy):
    def _read_file(self):
        py_file = open(self.__file_dir)
        self.__file_contents = py_file.readlines()
        for line in self.__file_contents:
            self._clean_file_contents += line
        py_file.close()

    def is_valid_file(self, new_dir):
        return str(new_dir).endswith(".py")

    def is_valid_dir(self, new_dir):
        return path.isfile(new_dir)

    def _set_file_dir(self, new_dir):
        self.__file_dir = new_dir
