from io import StringIO
from unittest import TestCase
from unittest.mock import patch
from src.ViewController import View
from os import getcwd


class TestFileReader(TestCase):

    def setUp(self):
        self.the_view = View()

    def test_set_empty_name(self):
        """Tests if controller gives correct output
         to an empty string given."""
        arg = ""
        correct_output = "Please provide a name."
        with patch('sys.stdout', new=StringIO()) as print_output:
            self.the_view.do_set_name(arg)
            self.assertEqual(correct_output,
                             print_output.getvalue().rstrip())

    def test_set_actual_name(self):
        """Tests to see if gives correct output to correct input."""
        arg = "Luofeng"
        correct_output = str.format("Name set to {}!", arg)
        with patch('sys.stdout', new=StringIO()) as print_output:
            self.the_view.do_set_name(arg)
            self.assertEqual(correct_output,
                             print_output.getvalue().rstrip())

    def test_exit(self):
        """Tests to ensure controller correctly exists."""
        arg = ""
        self.assertTrue(self.the_view.do_exit(arg))

    def test_bad_output_dir(self):
        """Tests to ensure controller identifies bad directory."""
        arg = "this/is/not/a/directory"
        correct_output = "Invalid directory/input. Please try again."
        with patch('sys.stdout', new=StringIO()) as print_output:
            self.the_view.do_set_output_dir(arg)
            self.assertEqual(correct_output,
                             print_output.getvalue().rstrip())

    def test_good_output_dir(self):
        """Tests to ensure controller identifies good directory."""
        arg = getcwd().replace("\\", "/")
        correct_output = str.format("Output directory set to [{}].", arg)
        with patch('sys.stdout', new=StringIO()) as print_output:
            self.the_view.do_set_output_dir(arg)
            self.assertEqual(correct_output,
                             print_output.getvalue().rstrip())

    def test_bad_file_type(self):
        """Tests to ensure controller rejects bad file type."""
        arg = "qq"
        correct_output = "incorrect file type."
        with patch('sys.stdout', new=StringIO()) as print_output:
            self.the_view.do_set_file_type(arg)
            self.assertEqual(correct_output,
                             print_output.getvalue().rstrip())

    def test_set_type_to_jpg(self):
        """Tests the controller successfully setting filetype to jpg."""
        arg = "jpg"
        correct_output = "set file type to jpg!"
        with patch('sys.stdout', new=StringIO()) as print_output:
            self.the_view.do_set_file_type(arg)
            self.assertEqual(correct_output,
                             print_output.getvalue().rstrip())

    def test_set_type_to_png(self):
        """Tests the controller successfully setting filetype to png."""
        arg = "png"
        correct_output = "set file type to png!"
        with patch('sys.stdout', new=StringIO()) as print_output:
            self.the_view.do_set_file_type(arg)
            self.assertEqual(correct_output,
                             print_output.getvalue().rstrip())

    def test_create_uml_no_directory_set(self):
        """Tests controller to reject this command with no output dir set."""
        arg1 = "C:/"
        arg_file_type = "jpg"
        expected = "Set output dir, file type, or provide valid input dir."
        self.the_view.do_set_file_type(arg_file_type)
        with patch('sys.stdout', new=StringIO()) as print_output:
            self.the_view.do_create_uml(arg1)
            self.assertEqual(expected,
                             print_output.getvalue().rstrip())

    def test_create_uml_no_filetype_set(self):
        """Tests controller to reject this command with no filetype set."""
        arg1 = "C:/Program Files"
        arg_output_dir = "C:/"
        expected = "Set output dir, file type, or provide valid input dir."
        self.the_view.do_set_output_dir(arg_output_dir)
        with patch('sys.stdout', new=StringIO()) as print_output:
            self.the_view.do_create_uml(arg1)
            self.assertEqual(expected,
                             print_output.getvalue().rstrip())

    def test_create_uml_not_valid_js_dir(self):
        """Tests controller to reject this command with bad js directory."""
        arg1 = "C:/Program Files"
        arg_output_dir = "C:/"
        arg_file_type = "jpg"
        expected = "Set output dir, file type, or provide valid input dir."
        self.the_view.do_set_output_dir(arg_output_dir)
        self.the_view.do_set_file_type(arg_file_type)
        with patch('sys.stdout', new=StringIO()) as print_output:
            self.the_view.do_create_uml(arg1)
            self.assertEqual(expected,
                             print_output.getvalue().rstrip())

    def test_create_js_uml_working(self):
        """Tests controller to correctly create an array of classes."""
        expected_classes = [
            {
                'name': 'TestClass1',
                'attributes': ['attribute1', 'attribute2'],
                'methods': ['constructor']},
            {
                'name': 'TestClass2',
                'attributes': ['attribute1', 'attribute2'],
                'methods': ['constructor']},
            {
                'name': 'TestClass3',
                'attributes': ['attribute1', 'attribute2'],
                'methods': ['constructor']
            }]
        arg = "{}/tests/testing_files/test_single_js_file".format(getcwd())
        arg_output_dir = "C:/"
        arg_file_type = "jpg"
        self.the_view.do_set_output_dir(arg_output_dir)
        self.the_view.do_set_file_type(arg_file_type)
        self.the_view.do_create_uml(arg)
        self.assertEqual(expected_classes,
                         self.the_view.parser.get_classes())

    def test_create_py_uml_working(self):
        """Tests controller to correctly create an array of classes."""
        print("running test for py")
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
        arg = "{}/tests/testing_files/py_files".format(getcwd())
        arg_output_dir = "C:/"
        arg_file_type = "jpg"
        self.the_view.do_set_output_dir(arg_output_dir)
        self.the_view.do_set_file_type(arg_file_type)
        self.the_view.do_create_uml(arg)
        self.assertEqual(expected_classes,
                         self.the_view.parser.get_classes())

    def test_help_all(self):
        with patch('sys.stdout', new=StringIO()) as print_output:
            self.the_view.do_help_all("")
            self.assertTrue(type(print_output.getvalue().rstrip()) is str)

    def test_instructions(self):
        with patch('sys.stdout', new=StringIO()) as print_output:
            self.the_view.do_instructions("")
            self.assertTrue(type(print_output.getvalue().rstrip()) is str)
