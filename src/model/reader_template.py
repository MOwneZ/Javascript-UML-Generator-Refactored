from abc import ABCMeta, abstractmethod


class ReaderTemplate(metaclass=ABCMeta):
    def __init__(self):
        self._file_dir = ""
        self._file_contents = ""
        self._clean_file_contents = ""

    @abstractmethod
    def is_valid_file(self, new_folder_path):
        raise NotImplementedError

    @abstractmethod
    def is_valid_dir(self, new_folder_path):
        raise NotImplementedError

    @abstractmethod
    def _read_file(self):
        raise NotImplementedError

    @abstractmethod
    def _set_file_dir(self, new_dir):
        raise NotImplementedError

    def get_file_contents(self, new_dir):
        self._set_file_dir(new_dir)
        self._read_file()
        return self._clean_file_contents

