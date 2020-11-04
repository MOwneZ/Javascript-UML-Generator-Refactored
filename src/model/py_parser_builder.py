from src.model.parser_builder import ParserBuilder
from esprima import parse


class PYParserBuilder(ParserBuilder):
    def parse_file(self):
        self._parsed_file = parse(self._file)
        self._set_classes()

    def _set_classes(self):
        for key, value in self._parsed_file.items():
            if key == "body":
                for aValue in value:
                    single_class = {"name": (self._get_class_name(aValue)),
                                    "attributes":
                                        (self._get_class_attributes(
                                            aValue.body.body)),
                                    "methods":
                                        self._get_class_methods(
                                            aValue.body.body)}
                    self.add_class(single_class)

    def _get_class_attributes(self, new_class_body):
        attributes = []
        for value in new_class_body:
            if value.type == "MethodDefinition" \
                    and value.key.name == "constructor":
                for aValue in value.value.body.body:
                    attributes.append(aValue.expression.left.property.name)
        return attributes

    def _get_class_methods(self, new_class_body):
        methods = []
        for value in new_class_body:
            methods.append(value.key.name)
        return methods

    def _get_class_name(self, new_value):
        return new_value.id.name
