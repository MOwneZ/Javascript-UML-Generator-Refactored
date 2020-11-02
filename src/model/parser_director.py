from src.model.parser_builder import ParserBuilder


class ParserDirector:
    def __init__(self, new_parser_builder: ParserBuilder):
        self.parser_builder = new_parser_builder

    def make_js_parser(self):
        self.parser_builder.set_get_class_name()
        self.parser_builder.set_get_class_attributes()
        self.parser_builder.set_get_class_methods()
        return self.parser_builder.get_parser()
