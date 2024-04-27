import unittest
from validator import Validator
class TestValidator(unittest.TestCase):
    def setUp(self):
        self.validator = Validator()

    def test_validate_name_surname(self):
        self.assertTrue(self.validator.validate_name_surname("Elvis Presley"))
        self.assertFalse(self.validator.validate_name_surname("ElvisPresley"))
        self.assertFalse(self.validator.validate_name_surname("Elvis Presley forever"))
        self.assertFalse(self.validator.validate_name_surname("elvis Presley"))
        self.assertFalse(self.validator.validate_name_surname("Elvis presley"))
        self.assertFalse(self.validator.validate_name_surname("Elvis PResley"))
        self.assertFalse(self.validator.validate_name_surname("Elvis Presleyqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqq"))
        self.assertFalse(self.validator.validate_name_surname("Elvis P"))
        self.assertFalse(self.validator.validate_name_surname("Elvis P,resley"))
        self.assertFalse(self.validator.validate_name_surname("El1vis Presley"))
        self.assertTrue(self.validator.validate_name_surname("Jean-Luc Picard"))
        self.assertTrue(self.validator.validate_name_surname("O'Neill"))
        self.assertFalse(self.validator.validate_name_surname(" Elvis Presley"))
        self.assertFalse(self.validator.validate_name_surname("Elvis Presley "))

    def test_validate_age(self):
        self.assertTrue(self.validator.validate_age("20"))
        self.assertFalse(self.validator.validate_age("7"))
        self.assertFalse(self.validator.validate_age("100"))
        self.assertFalse(self.validator.validate_age("20."))
        self.assertFalse(self.validator.validate_age("20a"))
        self.assertTrue(self.validator.validate_age("16"))
        self.assertTrue(self.validator.validate_age("99"))
        self.assertFalse(self.validator.validate_age("15"))
        self.assertFalse(self.validator.validate_age("20 years"))

    def test_validate_country(self):
        self.assertTrue(self.validator.validate_country("Ukraine"))
        self.assertFalse(self.validator.validate_country("U"))
        self.assertFalse(self.validator.validate_country("UUUUUUUUUUUUUUUUUUUUUUU"))
        self.assertFalse(self.validator.validate_country("Ukraine1"))
        self.assertFalse(self.validator.validate_country("ukraine"))
        self.assertTrue(self.validator.validate_country("USA"))
        self.assertTrue(self.validator.validate_country("New Zealand"))
        self.assertFalse(self.validator.validate_country("Ukra1ne"))
        self.assertFalse(self.validator.validate_country("Ukraine!"))

    def test_validate_region(self):
        self.assertTrue(self.validator.validate_region("Lviv"))
        self.assertTrue(self.validator.validate_region("Lviv1"))
        self.assertFalse(self.validator.validate_region("L"))
        self.assertFalse(self.validator.validate_region("lviv"))
        self.assertTrue(self.validator.validate_region("Region1"))
        self.assertFalse(self.validator.validate_region("R"))
        self.assertFalse(self.validator.validate_region("Region_12345678901234567890"))

    def test_validate_living_place(self):
        self.assertTrue(self.validator.validate_living_place("Koselnytska st. 2a"))
        self.assertFalse(self.validator.validate_living_place("koselnytska st. 2a"))
        self.assertFalse(self.validator.validate_living_place("Koselnytska provulok 2a"))
        self.assertFalse(self.validator.validate_living_place("Koselnytska st. 2"))
        self.assertFalse(self.validator.validate_living_place("Koselnytska st. a2"))
        self.assertTrue(self.validator.validate_living_place("Koselnytska st. 22"))
        self.assertFalse(self.validator.validate_living_place("123 Main st."))
        self.assertFalse(self.validator.validate_living_place("Main Street 123"))
        self.assertFalse(self.validator.validate_living_place("Koselnytska st. 2@"))

    def test_validate_index(self):
        self.assertTrue(self.validator.validate_index("79000"))
        self.assertFalse(self.validator.validate_index("7900"))
        self.assertFalse(self.validator.validate_index("790000"))
        self.assertFalse(self.validator.validate_index("7900q"))
        self.assertFalse(self.validator.validate_index("790 00"))
        self.assertFalse(self.validator.validate_index("1234A"))
        self.assertFalse(self.validator.validate_index("1234567"))
        self.assertFalse(self.validator.validate_index("79 000"))

    def test_validate_phone(self):
        self.assertTrue(self.validator.validate_phone("+380951234567"))
        self.assertTrue(self.validator.validate_phone("+38 (095) 123-45-67"))
        self.assertFalse(self.validator.validate_phone("38 (095) 123-45-67"))
        self.assertFalse(self.validator.validate_phone("380951234567"))
        self.assertFalse(self.validator.validate_phone("-380951234567"))
        self.assertFalse(self.validator.validate_phone("+3810951234567"))
        self.assertTrue(self.validator.validate_phone("+20951234567"))
        self.assertFalse(self.validator.validate_phone("+38 095 1234567"))
        self.assertFalse(self.validator.validate_phone("+38095-123-4567"))
        self.assertFalse(self.validator.validate_phone("0951234567"))

    def test_validate_email(self):
        self.assertTrue(self.validator.validate_email("username@domain.com"))
        self.assertTrue(self.validator.validate_email("username+usersurname@domain.com"))
        self.assertTrue(self.validator.validate_email("username@ucu.edu.ua"))
        self.assertFalse(self.validator.validate_email("usernamedomain.com"))
        self.assertFalse(self.validator.validate_email("username@domaincom"))
        self.assertFalse(self.validator.validate_email("username@domain.aaa"))
        self.assertFalse(self.validator.validate_email("username@aaa"))
        self.assertFalse(self.validator.validate_email("@domain.com"))
        self.assertFalse(self.validator.validate_email("username@domain"))
        self.assertFalse(self.validator.validate_email("username@.com"))
        self.assertFalse(self.validator.validate_email("myemaillllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllll@ukr.net"))

    def test_validate_id(self):
        self.assertTrue(self.validator.validate_id("123450"))
        self.assertTrue(self.validator.validate_id("011111"))
        self.assertFalse(self.validator.validate_id("123456"))
        self.assertFalse(self.validator.validate_id("123006"))
        self.assertFalse(self.validator.validate_id("1230916"))
        self.assertFalse(self.validator.validate_id("12306"))
        self.assertFalse(self.validator.validate_id("12345"))
        self.assertFalse(self.validator.validate_id("1234567"))
        self.assertFalse(self.validator.validate_id("12345A"))

    def test_validate_full_data(self):
        self.assertTrue(self.validator.validate("Elvis Presley,20,Ukraine,Lviv,Koselnytska st. 2a,79000,+380951234567,username@domain.com,123450"))
        self.assertTrue(self.validator.validate("Elvis Presley;20;Ukraine;Lviv;Koselnytska st. 2a;79000;+380951234567;username@domain.com;123450"))
        self.assertTrue(self.validator.validate("Elvis Presley; 20; Ukraine; Lviv; Koselnytska st. 2a; 79000; +380951234567; username@domain.com; 123450"))
        self.assertTrue(self.validator.validate("Elvis Presley, 20, Ukraine, Lviv, Koselnytska st. 2a, 79000, +380951234567, username@domain.com, 123450"))
        self.assertFalse(self.validator.validate("Elvis Presley, 3, Ukraine, Lviv, Koselnytska st. 2a, 79000, +380951234567, username@domain.com, 123450"))
        self.assertFalse(self.validator.validate("Elvis Presley, 20, Ukraine, Lviv, Koselnytska st. 2a, 69000, +380951234567, username@domain.com, 123457"))

if __name__ == '__main__':
    unittest.main()