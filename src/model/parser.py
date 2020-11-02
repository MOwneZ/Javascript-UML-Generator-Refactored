from esprima import parse
from abc import abstractmethod, ABCMeta


class Parser(metaclass=ABCMeta):
    def __init__(self):
        self._file = str()
        self._parsed_file = {}
        self._all_my_classes = []

    def get_classes(self):
        return self._all_my_classes

    def set_file(self, new_file):
        self._file = new_file

    def parse_file(self):
        self._parsed_file = parse(self._file)
        self._set_classes()

    def add_class(self, new_class):
        if new_class not in self._all_my_classes:
            self._all_my_classes.append(new_class)

    def _set_classes(self):
        for key, value in self._parsed_file.items():
            if key == "body":
                for aValue in value:
                    single_class = {"name": (self.__get_class_name(aValue)),
                                    "attributes":
                                        (self.__get_class_attributes(
                                            aValue.body.body)),
                                    "methods":
                                        self.__get_class_methods(
                                            aValue.body.body)}
                    self.add_class(single_class)

    @abstractmethod
    def __get_class_name(self, new_value):
        raise NotImplementedError

    @abstractmethod
    def __get_class_attributes(self, new_class_body):
        raise NotImplementedError

    @abstractmethod
    def __get_class_methods(self, new_class_body):
        raise NotImplementedError
