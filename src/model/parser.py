from esprima import parse
from abc import abstractmethod, ABCMeta


class Parser(metaclass=ABCMeta):
    def __init__(self):
        self.__file = str()
        self.__parsed_file = {}
        self.__all_my_classes = []

    def get_classes(self):
        return self.__all_my_classes

    def set_file(self, new_file):
        self.__file = new_file

    def parse_file(self):
        self.__parsed_file = parse(self.__file)
        self.__set_classes()

    @abstractmethod
    def __set_classes(self):
        ...

    @abstractmethod
    def __get_class_name(self, new_value):
        ...

    @abstractmethod
    def __get_class_attributes(self, new_class_body):
        ...

    @abstractmethod
    def __get_class_methods(self, new_class_body):
        ...

    @abstractmethod
    def __add_class(self, new_class):
        ...
