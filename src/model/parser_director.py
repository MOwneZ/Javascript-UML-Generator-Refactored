from src.model.parser_builder import ParserBuilder


class ParserDirector:
    def __init__(self, new_parser_builder: ParserBuilder):
        self.parser_builder = new_parser_builder

    def make_parser(self, new_file_string):
        self.parser_builder.set_file(new_file_string)
        self.parser_builder.parse_file()
        return self.parser_builder
