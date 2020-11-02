from src.model.parser import Parser


class JsParser(Parser):
    def _get_class_name(self, new_value):
        return new_value.id.name

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
