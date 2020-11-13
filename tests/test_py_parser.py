from unittest import TestCase
from os import getcwd
from src.model.py_parser_builder import PYParserBuilder
from src.model.parser_director import ParserDirector
from src.model.py_file_reader import PYFileReader
from src.model.file_reader import FileReader
from src.model.directory_reader import DirectoryReader


class TestJsParser(TestCase):

    def setUp(self):
        self.parser = None
        self.file_reader = FileReader(PYFileReader())
        self.dir_reader = DirectoryReader()
        self.current_dir = getcwd() + '/tests'

    def test_basic_class(self):
        """Tests to see whether it can correctly read a py file with a
        basic class."""

        expected_class = {
            'attributes': ['attribute1', 'attribute2', 'attribute3'],
            'methods': ['__init__'],
            'name': 'TestClass'}
        file_dir = str.format("{}/testing_files/py_files/test_file_1.py",
                              self.current_dir).replace("\\", "/")
        py_file = self.file_reader.get_file_contents(file_dir)
        parser_director = ParserDirector(PYParserBuilder())
        self.parser = parser_director.make_parser(py_file)
        actual_class = self.parser.get_classes()[0]
        self.assertEqual(expected_class, actual_class)

    def test_multiple_classes(self):
        """Tests to see whether it can correctly read a py file with multiple
        classes."""
        expected_classes = [{
            'attributes': ['attribute1', 'attribute2', 'attribute3'],
            'methods': ['__init__'],
            'name': 'TestClass1'},
            {
            'attributes': ['attribute1', 'attribute2', 'attribute3'],
            'methods': ['__init__'],
            'name': 'TestClass2'},
            {
            'attributes': ['attribute1', 'attribute2', 'attribute3'],
            'methods': ['__init__'],
            'name': 'TestClass3'}]
        file_dir = str.format("{}/testing_files/py_files/test_file_2.py",
                              self.current_dir).replace("\\", "/")
        js_file = self.file_reader.get_file_contents(file_dir)
        parser_director = ParserDirector(PYParserBuilder())
        self.parser = parser_director.make_parser(js_file)
        actual_classes = self.parser.get_classes()
        self.assertEqual(expected_classes, actual_classes)

    def test_no_classes(self):
        """Tests to see whether it returns an empty list when there are
        no classes."""
        expected_classes = []
        file_dir = str.format("{}/testing_files/test_file_empty.py",
                              self.current_dir).replace("\\", "/")
        js_file = self.file_reader.get_file_contents(file_dir)
        parser_director = ParserDirector(PYParserBuilder())
        self.parser = parser_director.make_parser(js_file)
        actual_classes = self.parser.get_classes()
        self.assertEqual(expected_classes, actual_classes)

    def test_entire_class(self):
        """Tests to see whether it returns an empty list when the provided
        file is not compatible."""
        expected_classes = []
        file_dir = str.format("{}/testing_files/test_file_bad.js",
                              self.current_dir).replace("\\", "/")
        js_file = self.file_reader.get_file_contents(file_dir)
        parser_director = ParserDirector(PYParserBuilder())
        self.parser = parser_director.make_parser(js_file)
        actual_classes = self.parser.get_classes()
        self.assertEqual(expected_classes, actual_classes)
