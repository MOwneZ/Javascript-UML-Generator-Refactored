from src.model.parser_builder import ParserBuilder
from ast import parse, walk, ClassDef, Attribute, FunctionDef


class PYParserBuilder(ParserBuilder):
    def parse_file(self):
        self._parsed_file = parse(self._file)
        self._set_classes()

    def _set_classes(self):
        for element in self._parsed_file.body:
            classes = [c for c in walk(element) if
                       isinstance(c, ClassDef)]
            for a_class in classes:
                single_class = {"name": (self._get_class_name(a_class)),
                                "attributes":
                                    (self._get_class_attributes(
                                        a_class)),
                                "methods":
                                    self._get_class_methods(
                                        a_class)}
                self.add_class(single_class)

    def _get_class_attributes(self, new_class_body):
        attributes = []
        body = [c for c in walk(new_class_body) if
                isinstance(c, Attribute)]
        for attribute in body:
            attributes.append(attribute.attr)
        return attributes

    def _get_class_methods(self, new_class_body):
        methods = []
        body = [c for c in walk(new_class_body) if
                isinstance(c, FunctionDef)]
        for method in body:
            methods.append(method.name)
        return methods

    def _get_class_name(self, new_class_body):
        return new_class_body.name
