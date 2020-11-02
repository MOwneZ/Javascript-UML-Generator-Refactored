from abc import abstractmethod, ABCMeta
from src.model.parser import Parser


class ParserBuilder(metaclass=ABCMeta):
    def __init__(self):
        self.parser = Parser()

    @abstractmethod
    def set_get_class_methods(self):
        raise NotImplementedError

    @abstractmethod
    def set_get_class_attributes(self):
        raise NotImplementedError

    @abstractmethod
    def set_get_class_name(self):
        raise NotImplementedError
