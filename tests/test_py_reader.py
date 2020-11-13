from unittest import TestCase
from src.model.py_file_reader import PYFileReader
from src.model.file_reader import FileReader
from os import getcwd


class TestFileReader(TestCase):

    def setUp(self):
        self.file_reader = FileReader(PYFileReader())
        self.current_dir = getcwd() + "/tests"

    def test_read_txt_file(self):
        """This test simply tests the basic reader - whether it can correctly
         read a regular .txt file"""
        file_dir = str.format("{}/testing_files/not_a_js_file.txt",
                              self.current_dir).replace("\\", "/")
        file_contents = "This is not a JS file!"
        self.assertEqual(self.file_reader.get_file_contents(file_dir),
                         file_contents)

    def test_read_py_file(self):
        """This tests to ensure it can correctly read a .py file contents"""
        file_dir = str.format("{}/testing_files/py_files/test_file_1.py",
                              self.current_dir).replace("\\", "/")
        expected_file_contents = 'class TestClass:\n'\
                                 '    def __init__(self):\n'\
                                 '        self.attribute1 = ""\n'\
                                 '        self.attribute2 = ""\n'\
                                 '        self.attribute3 = ""\n'
        actual_file_contents = self.file_reader.get_file_contents(file_dir)
        self.assertEqual(expected_file_contents, actual_file_contents)

    def test_reject_wrong_file(self):
        """This tests to ensure the class will reject a file that's not
        a js file, when using that particular checker."""
        file_dir = str.format("{}/testing_files/not_a_js_file.txt",
                              self.current_dir).replace("\\", "/")
        self.assertFalse(self.file_reader.check_if_valid_file(file_dir))

    def test_accept_right_file(self):
        """This tests to ensure the class will accept a file that's
                a js file, when using that particular checker."""
        file_dir = str.format("{}/testing_files/test_file_1.py",
                              self.current_dir).replace("\\", "/")
        self.assertTrue(self.file_reader.check_if_valid_file(file_dir))

    def test_no_file(self):
        """This tests to ensure the class will reject a file that doesn't
        exist!"""
        file_dir = str.format("{}/testing_files/no_file",
                              self.current_dir).replace("\\", "/")
        self.assertFalse(self.file_reader.check_if_valid_file(file_dir))

    def test_empty_file(self):
        """This tests to ensure the class will read a class that's empty.
        It's not an issue if an empty file makes it through as it makes no
        difference to the program."""
        file_dir = str.format("{}/testing_files/test_file_empty.py",
                              self.current_dir).replace("\\", "/")
        self.assertTrue(self.file_reader.check_if_valid_file(file_dir))

    def test_is_valid_file_dir(self):
        """This tests to see whether it correctly returns true on a valid
        file directory."""
        file_dir = str.format("{}/testing_files/test_file_empty.py",
                              self.current_dir).replace("\\", "/")
        self.assertTrue(self.file_reader.check_if_valid_dir(file_dir))

    def test_is_invalid_file_dir(self):
        """This tests to see whether it correctly returns false on an invalid
        file directory."""
        file_dir = "Bad times! No."
        self.assertFalse(self.file_reader.check_if_valid_dir(file_dir))
