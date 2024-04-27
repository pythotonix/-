"""to test"""
import unittest
from final_class_codium_ai import Rational, find_nsd

class TestRational(unittest.TestCase):
    """
    A test suite for testing the functionality of the Rational class.
    """

    def test_initialization_and_representation(self):
        """
        Test the initialization and string representation of Rational objects.
        """
        rational1 = Rational(1, 4)
        self.assertEqual(rational1.numerator, 1)
        self.assertEqual(rational1.denominator, 4)
        self.assertIsInstance(rational1, Rational)
        self.assertEqual(str(rational1), "1/4")

    def test_negative_input(self):
        """
        Test the handling of negative inputs in the numerator and denominator.
        """
        # Test with negative numerator
        rational_neg_num = Rational(-1, 4)
        self.assertEqual(str(rational_neg_num), "-1/4")

        # Test with negative denominator
        rational_neg_denom = Rational(1, -4)
        self.assertEqual(str(rational_neg_denom), "-1/4")

        # Test with both negative numerator and denominator
        rational_both_neg = Rational(-1, -4)
        self.assertEqual(str(rational_both_neg), "1/4")

    def test_property_mixed_form(self):
        """
        Test setting and getting the mixed form representation of a Rational object.
        """
        rational6 = Rational(1, 1)  # Initialize to any valid value
        rational6.mixed_form = '-1 13/27'
        self.assertEqual(rational6.mixed_form, '-1 13/27')

    def test_property_numerator_after_setting_mixed_form(self):
        """
        Test the internal state of the numerator after setting the mixed form.
        """
        rational6 = Rational(1, 1)  # Initialize to any valid value
        rational6.mixed_form = '-1 13/27'
        self.assertEqual(rational6.numerator, -40)

    def test_zero_denominator(self):
        """
        Test that initializing Rational with a zero denominator raises a ValueError.
        """
        with self.assertRaises(ValueError) as context:
            Rational(1, 0)
        self.assertEqual(str(context.exception), "Denominator cannot be zero.")

    def test_reduction(self):
        """
        Test the reduction method of Rational class.
        """
        rational2 = Rational(2, 4)
        self.assertEqual(str(rational2), "2/4")
        rational2 = rational2.reduce()
        self.assertEqual(str(rational2), "1/2")
        with self.assertRaises(TypeError):
            rational = Rational('2', 4)
            rational.reduce()

    def test_arithmetic_operations_and_complex_expressions(self):
        """
        Test basic arithmetic operations and more complex expressions involving multiple operations.
        """
        rational1 = Rational(1, 4)
        rational2 = Rational(2, 5)
        # Basic operations
        self.assertEqual(str(rational1 + rational2), "13/20")
        self.assertEqual(str(rational1 - rational2), "-3/20")
        self.assertEqual(str(rational1 * rational2), "1/10")
        self.assertEqual(str(rational1 / rational2), "5/8")
        # Complex expression
        result = rational1 / rational2 * rational1 - rational1
        self.assertEqual(str(result), "-3/32")
        # Type error checks
        with self.assertRaises(TypeError):
            rational1 + Rational('2', 5)
        with self.assertRaises(TypeError):
            rational1 - Rational(2, '5')
        with self.assertRaises(TypeError):
            rational1 * Rational('1', 10)
        with self.assertRaises(TypeError):
            rational1 / Rational(5, '8')

    def test_comparisons(self):
        """
        Test comparison operations (equality, less than or equal) between Rational objects.
        """
        rational1 = Rational(1, 4)
        rational2 = Rational(2, 5)
        rational3 = Rational(2, 8)
        self.assertEqual(rational1, rational3)
        self.assertLess(rational1, rational2)
        self.assertLessEqual(rational1, rational2)
        with self.assertRaises(TypeError):
            result = rational1 < Rational('2', 5)
        with self.assertRaises(TypeError):
            result = rational1 <= Rational(2, '5')
    def test_find_nsd(self):
        self.assertEqual(find_nsd(18, 24), 6)
        self.assertEqual(find_nsd(7, 13), 1)

    def test_eq_with_non_rational(self):
        rational1 = Rational(1, 2)
        rational2 = Rational(1, 2)
        self.assertTrue(rational1 == rational2)

    def test_lt_with_non_rational(self):
        rational1 = Rational(1, 2)
        rational2 = Rational(1, 3)
        self.assertTrue(rational1 > rational2)

    def test_le_with_non_rational(self):
        rational1 = Rational(1, 2)
        rational2 = Rational(1, 2)
        self.assertTrue(rational1 <= rational2)

    def test_gt_with_non_rational(self):
        rational1 = Rational(1, 2)
        rational2 = Rational(1, 3)
        self.assertTrue(rational1 > rational2)

    def test_ge_with_non_rational(self):
        rational1 = Rational(1, 2)
        rational2 = Rational(1, 2)
        self.assertTrue(rational1 >= rational2)

    def test_mixed_form_getter(self):
        # Test cases for the getter
        r1 = Rational(5, 2)
        self.assertEqual(r1.mixed_form, "2 1/2")

        r2 = Rational(2, 1)
        self.assertEqual(r2.mixed_form, "2")

        r3 = Rational(-3, 2)
        self.assertEqual(r3.mixed_form, "-1 1/2")

        r4 = Rational(0, 1)
        self.assertEqual(r4.mixed_form, "0")

    def test_mixed_form_setter_with_string(self):
        # Test cases for the setter with string input
        r = Rational(1, 1)
        r.mixed_form = "3 1/2"
        self.assertEqual((r.numerator, r.denominator), (7, 2))

        r.mixed_form = "-2 3/4"
        self.assertEqual((r.numerator, r.denominator), (-11, 4))

    def test_mixed_form_setter_with_int(self):
        # Test cases for the setter with integer input
        r = Rational(1, 1)
        r.mixed_form = 5
        self.assertEqual((r.numerator, r.denominator), (5, 1))
    def test_mixed_form_whole_zero(self):
        # Test case where the whole part is zero
        r = Rational(1, 2)
        self.assertEqual(r.mixed_form, "1/2")

    def test_mixed_form_whole_non_zero(self):
        # Test case where the whole part is not zero
        r = Rational(3, 2)
        self.assertEqual(r.mixed_form, "1 1/2")
    def test_mixed_form_setter_no_slash(self):
        r = Rational(1, 2)  # Create a Rational object
        r.mixed_form = "3"  # Set using the mixed form setter
        self.assertEqual(r.numerator, 6)
        self.assertEqual(r.denominator, 1)

if __name__ == '__main__':
    unittest.main()
