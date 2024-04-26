# quick-test
# first promt without setUp
import unittest
# cd from unittest.mock import mock_open, patch

'''Program to find out in what order the aliens will deliver the chosen people to their planet'''


def read_file(file_path: str) -> dict:
    '''
    Reads a file and returns a dictionary, the keys of which should be the names of people, \
    and the values - their IQ level.

    >>> read_file('smart_people.txt')
    {'Elon Musk': 165, 'Mark Zuckerberg': 152, 'Will Smith': 157, 'Marilyn vos Savant': 186, \
'Judith Polgar': 170, 'Quentin Tarantino': 163, 'Bill Gates': 160, "Conan O'Brien": 160, \
'Emma Watson': 132, 'Barack Obama': 137}
    '''
    smarties = {}
    with open(file_path, 'r', encoding = 'UTF-8') as file:
        for line in file:
            if line[0].isalpha():
                name = line.split(',')[0]
                iq = int(line.split(',')[1])
                smarties[name] = iq
    return smarties

# def rescue_people(smarties: dict, limit_iq: int) -> tuple:
#     '''
#     Returns a tuple of the number of required trips and a list of lists, \
#     where each inner list represents a trip and contains the names of people \
#     who are transported on this trip and whose iq sum must not exceed the given iq limit.

#     >>> rescue_people({'Steve Jobs': 160, 'Albert Einstein': 160, \
# 'Sir Isaac Newton': 195, 'Nikola Tesla': 189}, 500)
#     (2, [['Sir Isaac Newton', 'Nikola Tesla'], ['Albert Einstein', 'Steve Jobs']])
#     >>> rescue_people({}, 500)
#     (0, [])
#     '''
#     smarties = dict(sorted(smarties.items(), key=lambda x: (-x[1], x[0])))

#     iq_sum = 0
#     trip = []
#     all_trips = []
#     for person, iq in smarties.items():
#         if iq_sum + iq <= limit_iq:
#             trip += [person]
#             iq_sum += iq
#         else:
#             if trip:
#                 all_trips += [trip]
#                 trip = [person]
#                 iq_sum = iq
#     if trip:
#         all_trips += [trip]
#     return (len(all_trips), all_trips)


# class TestReadFile(unittest.TestCase):
#     def test_read_file_success(self):
#         # Mock data and the open function
#         mock_data = "Elon Musk,165\nMark Zuckerberg,152"
#         m = mock_open(read_data=mock_data)
#         with patch('smart_people.txt', m):
#             result = read_file('dummy_path')
#             expected = {'Elon Musk': 165, 'Mark Zuckerberg': 152}
#             self.assertEqual(result, expected)

#     def test_read_file_no_file(self):
#         # Test the behavior when the file does not exist
#         with patch('smart_people.txt', side_effect=FileNotFoundError):
#             result = read_file('nonexistent_path')
#             self.assertEqual(result, {})

#     def test_read_file_invalid_data(self):
#         # Test the behavior with invalid data (non-integer IQ)
#         mock_data = "Elon Musk,not_an_int"
#         m = mock_open(read_data=mock_data)
#         with patch('smart_people.txt', m):
#             result = read_file('dummy_path')
#             self.assertEqual(result, {})

import unittest
import os
import tempfile

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
    # ==================== Add more tests mode ===============
    # def test_read_file_empty_file(self):
    #     # Test the read_file function with an empty file
    #     expected_output = {}
    #     result = read_file(self.test_file.name)
    #     self.assertEqual(result, expected_output)


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


def rescue_people(smarties: dict, limit_iq: int) -> tuple:
    '''
    Returns a tuple of the number of required trips and a list of lists, \
    where each inner list represents a trip and contains the names of people \
    who are transported on this trip and whose iq sum must not exceed the given iq limit.

    >>> rescue_people({'Steve Jobs': 160, 'Albert Einstein': 160, \
'Sir Isaac Newton': 195, 'Nikola Tesla': 189}, 500)
    (2, [['Sir Isaac Newton', 'Nikola Tesla'], ['Albert Einstein', 'Steve Jobs']])
    >>> rescue_people({}, 500)
    (0, [])
    '''
    smarties = dict(sorted(smarties.items(), key=lambda x: (-x[1], x[0])))

    iq_sum = 0
    trip = []
    all_trips = []
    for person, iq in smarties.items():
        if iq_sum + iq <= limit_iq:
            trip += [person]
            iq_sum += iq
        else:
            if trip:
                all_trips += [trip]
                trip = [person]
                iq_sum = iq
    if trip:
        all_trips += [trip]
    return (len(all_trips), all_trips)

# write unittest for this function
# Write a function rescue_people(smarties, limit_iq) that takes a dictionary of smarties, 
# a function read_file as input and limit_iq as an int value. 
# One of the elements that the function returns must be a list of lists, 
# where each element of the main list is a sublist. The sublist must 
# contain the smarties dictionary keys with the highest value, and the 
# sum of the corresponding values of the sublist keys must not exceed limit_iq. 
# When the first sublist is formed, it is added to the main list, 
# and the corresponding keys with values are removed from the dictionary. 
# The function returns a tuple, where the first value is the length of the 
# generated list, and the second is the list itself
# Precondition:
# - People with values in the dictionary higher than 130 can be added to the list
# - If the keys have the same value, the order of selection is in lexicographic order.
# - limit_iq is always greater than the maximum possible value in the dictionary
# - The list can be empty and the application should handle this option correctly.
# For example:
# >>> rescue_people({"Steve Jobs": 160, "Albert Einstein": 160, 
# "Sir Isaac Newton": 195, "Nikola Tesla": 189},500)
# (2, [["Sir Isaac Newton", "Nikola Tesla"], ["Albert Einstein", "Steve Jobs"]])
# 1) We first removed "Sir Isaac Newton" and "Nikola Tesla" because 
# their values in the dictionary are the largest: (500 -195 -189 = 116). No more items can be added here, because the values of the remaining keys in the dictionary are greater than 116.
# 2) Remove ["Albert Einstein", "Steve Jobs"] in lexicographic order.
# The final result is (2, [["Sir Isaac Newton", "Nikola Tesla"], ["Albert Einstein", "Steve Jobs"]])

class TestRescuePeople(unittest.TestCase):
    def test_rescue_people(self):
        # Test case as described in the example
        smarties = {
            "Steve Jobs": 160,
            "Albert Einstein": 160,
            "Sir Isaac Newton": 195,
            "Nikola Tesla": 189
        }
        limit_iq = 500
        expected = (2, [["Sir Isaac Newton", "Nikola Tesla"], ["Albert Einstein", "Steve Jobs"]])
        result = rescue_people(smarties, limit_iq)
        self.assertEqual(result, expected)

        # Additional test cases
        # Test with empty dictionary
        self.assertEqual(rescue_people({}, 500), (0, []))

        # Test with limit_iq less than any valid IQ
        self.assertEqual(rescue_people(smarties, 100), (0, []))

        # Test with all IQs below the threshold
        low_iq_smarties = {"Person1": 100, "Person2": 120}
        self.assertEqual(rescue_people(low_iq_smarties, 500), (0, []))

        # Test with single valid entry
        single_smartie = {"Elon Musk": 150}
        self.assertEqual(rescue_people(single_smartie, 500), (1, [["Elon Musk"]]))


if __name__ == "__main__":
    unittest.main()


# if __name__ == '__main__':
#     unittest.main()
