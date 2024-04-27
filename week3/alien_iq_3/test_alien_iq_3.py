import unittest
import os
import tempfile
from script_alien import read_file, rescue_people, selection_sort_dict, selection_sort_list_tuple


class TestReadFile(unittest.TestCase):
    def setUp(self):
        # Create a temporary file and write some test data
        self.test_file = tempfile.NamedTemporaryFile(delete=False, mode='w+')
        self.test_file.write("Elon Musk,165\n")
        self.test_file.write("Mark Zuckerberg,152\n")
        self.test_file.write("Will Smith,157\n")
        self.test_file.flush()  # Ensure data is written to the file

        self.test_file1 = tempfile.NamedTemporaryFile(delete=False, mode='w+')
        self.test_file1.write("Elon Musk,165\n")
        self.test_file1.write("Mark Zuckerberg,152\n")
        self.test_file1.write("Will Smith,157\n")
        self.test_file1.write("Marilyn vos Savant,186\n")
        self.test_file1.write("Judith Polgar,170\n")
        self.test_file1.write("Quentin Tarantino,163\n")
        self.test_file1.write("Bill Gates,160\n")
        self.test_file1.write("Conan O'Brien,160\n")
        self.test_file1.write("Emma Watson,132\n")
        self.test_file1.write("Barack Obama,137\n")
        self.test_file1.flush()  # Ensure data is written to the file

        self.test_file2 = tempfile.NamedTemporaryFile(delete=False, mode='w+')
        self.test_file2.write("Barack Obama137\n")
        self.test_file2.flush()  # Ensure data is written to the file

    def tearDown(self):
        # Close and remove the temporary file
        self.test_file.close()
        os.remove(self.test_file.name)

        self.test_file1.close()
        os.remove(self.test_file1.name)

        self.test_file2.close()
        os.remove(self.test_file2.name)

    def test_read_file(self):
        # Test the read_file function
        expected_output = {
            'Elon Musk': 165,
            'Mark Zuckerberg': 152,
            'Will Smith': 157
        }
        result = read_file(self.test_file.name)
        self.assertEqual(result, expected_output)


    def test_read_file_multiple_lines(self):
        # Test the read_file function with multiple lines in the file
        expected_output = {
            'Elon Musk': 165,
            'Mark Zuckerberg': 152,
            'Will Smith': 157,
            'Marilyn vos Savant': 186,
            'Judith Polgar': 170,
            'Quentin Tarantino': 163,
            'Bill Gates': 160,
            "Conan O'Brien": 160,
            'Emma Watson': 132,
            'Barack Obama': 137
        }
        result = read_file(self.test_file1.name)
        self.assertEqual(result, expected_output)


class TestRescuePeople(unittest.TestCase):
    def setUp(self):
        self.smarties = {
            "Steve Jobs": 160, "Albert Einstein": 160,
            "Sir Isaac Newton": 195, "Nikola Tesla": 189
        }
        self.smarties_1 = {
            "Elon Musk": 160,
            "Bill Gates": 150,
            "Steve Jobs": 140
        }
        self.single_smartie = {"Elon Musk": 150}
        self.low_iq_smarties = {"Person1": 100, "Person2": 120}
        self.smarties_2 = {
            "Invalid Person": -100,
            "Another Invalid Person": 0
        }

        self.smarties_3 = {
            "Steve Jobs": 160, "Albert Einstein": 160,
            "Sir Isaac Newton": 195, "Nikola Tesla": 189
        }

    def test_rescue_people(self):
        expected = (2, [["Sir Isaac Newton", "Nikola Tesla"], ["Albert Einstein", "Steve Jobs"]])
        result = rescue_people(self.smarties, 500)
        self.assertCountEqual(result, expected)

    def test_empty_list_returns(self):
        self.assertCountEqual(rescue_people({}, 500), (0, []))
        self.assertCountEqual(rescue_people(self.smarties, 100), (0, []))
        self.assertCountEqual(rescue_people(self.smarties, 150), (0, []))

    def test_rescue_all_in_one_trip(self):
        expected = (1, [["Elon Musk", "Bill Gates", "Steve Jobs"]])
        self.assertCountEqual(rescue_people(self.smarties_1, 450), expected)
        self.assertCountEqual(rescue_people(self.single_smartie, 500), (1, [["Elon Musk"]]))
        expected_1 = (1, [["Sir Isaac Newton", "Nikola Tesla", "Albert Einstein", "Steve Jobs"]])
        self.assertCountEqual(rescue_people(self.smarties_3, 1000), expected_1)

    def test_sorting_tuples_on_first_element_when_second_elements_equal(self):
        input_list = [('M', 160), ('A', 160), ('W', 189), ('P', 195)]
        expected_output = [('M', 160), ('A', 160), ('W', 189), ('P', 195)]
        result = selection_sort_list_tuple(input_list)
        self.assertEqual(result, expected_output)