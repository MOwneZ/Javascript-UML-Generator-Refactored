from src.model.parser_builder import ParserBuilder
from src.model.parser import Parser


def parser_get_class_attributes(new_class_body):
    attributes = []
    for value in new_class_body:
        if value.type == "MethodDefinition" \
                and value.key.name == "constructor":
            for aValue in value.value.body.body:
                attributes.append(aValue.expression.left.property.name)
    return attributes


def parser_get_class_methods(new_class_body):
    methods = []
    for value in new_class_body:
        methods.append(value.key.name)
    return methods


def parser_get_class_name(new_value):
    return new_value.id.name


class JSParserBuilder(ParserBuilder):

    def set_get_class_attributes(self):
        self.parser.__get_class_attributes = \
            parser_get_class_attributes

    def set_get_class_methods(self):
        self.parser.__get_class_methods = \
            parser_get_class_methods

    def set_get_class_name(self):
        self.parser.__get_class_name = \
            parser_get_class_name

    def get_parser(self):
        return self.parser
