import unittest
import time
from puzzle import validate_board

class TestValidateBoard(unittest.TestCase):
    def test_board_with_non_numeric_characters(self):
        board = [
            "****a****",
            "***12****",
            "**123****",
            "*1234****",
            "123456789",
            "23456789*",
            "3456789**",
            "456789***",
            "56789****"
        ]
        self.assertFalse(validate_board(board))

    def test_board_dimensions(self):
        # Test case with missing rows
        board_with_missing_rows = [
            "****1****",
            "***12****"
        ]
        self.assertFalse(validate_board(board_with_missing_rows), "Should fail with missing rows")

        # Test case with more than 9 rows
        board_with_extra_rows = [
            "****1****",
            "***12****",
            "**123****",
            "*1234****",
            "123456789",
            "23456789*",
            "3456789**",
            "456789***",
            "56789****",
            "6789*****",
            "789******"  # Extra rows
        ]
        self.assertFalse(validate_board(board_with_extra_rows), "Should fail with extra rows")

        # Test case with fewer than 9 columns in some rows
        board_with_fewer_columns = [
            "****1****",
            "***12***",  # Missing one column
            "**123****",
            "*1234****",
            "123456789",
            "23456789*",
            "3456789**",
            "456789***",
            "56789****"
        ]
        self.assertFalse(validate_board(board_with_fewer_columns), "Should fail with fewer columns")

        # Test case with more than 9 columns in some rows
        board_with_extra_columns = [
            "****1****",
            "***12****",
            "**123****",
            "*1234****",
            "1234567890",  # Extra column
            "23456789*",
            "3456789**",
            "456789***",
            "56789****"
        ]
        self.assertFalse(validate_board(board_with_extra_columns), "Should fail with extra columns")

        # Test board size just below valid
        board_size_just_below_valid = [
            "**** ****",
            "***1 ****",
            "**8 3****",
            "* 4 1****",
            "    9 5  ",
            " 6  83  *",
            "3   7  **",
            "  8  2***",  # Missing one row
        ]
        self.assertFalse(validate_board(board_size_just_below_valid), "Should fail with one row missing")

        # Test board size just above valid
        board_size_just_above_valid = [
            "**** ****",
            "***1 ****",
            "**8 3****",
            "* 4 1****",
            "    9 5  ",
            " 6  83  *",
            "3   7  **",
            "  8  2***",
            "   2 ****",
            "   2 ****"  # One extra row
        ]
        self.assertFalse(validate_board(board_size_just_above_valid), "Should fail with one extra row")  
    def test_valid_board_minimal(self):
        board = [
            "**** ****",
            "***1 ****",
            "**  3****",
            "* 4  ****",
            "    9 5  ",
            " 6  83  *",
            "3   1  **",
            "  8  2***",
            "  2  ****"
        ]
        self.assertTrue(validate_board(board))
    def test_partially_filled_valid_board(self):
        board = [
            "**** ****",
            "***1 ****",
            "**  3****",
            "* 4 2****",
            "    6 5  ",
            " 7  83  *",
            "3   1  **",
            "  8  2***",
            "  9  ****"
        ]
        self.assertTrue(validate_board(board))
    def test_valid_board_fully_filled(self):
        board = [
            "****1****",
            "***12****",
            "**123****",
            "*1234****",
            "123456789",
            "23456789*",
            "3456789**",
            "456789***",
            "56789****"
        ]
        self.assertTrue(validate_board(board))
    def test_all_cells_empty(self):
        board = [
            "         ",
            "         ",
            "         ",
            "         ",
            "         ",
            "         ",
            "         ",
            "         ",
            "         "
        ]
        self.assertTrue(validate_board(board))
    def test_valid_board_specific_blocks(self):
        board = [
            "**** ****",
            "***1 ****",
            "**  3****",
            "* 4  ****",
            "    965  ",
            " 6  837 *",
            "3   1  **",
            "  8  2***",
            "  2  ****"
        ]
        self.assertTrue(validate_board(board))

    def test_invalid_row(self):
        board = [
            "**** ****",
            "***1 ****",
            "**  3****",
            "* 4  ****",
            "    9 5  ",
            " 6  83  *",
            "3   1  **",
            "  8  2***",
            "  2 2****"  # Invalid due to duplicate '2' in the last row
        ]
        self.assertFalse(validate_board(board))

    def test_invalid_column(self):
        board = [
            "**** ****",
            "***1 ****",
            "**  1****",  # Invalid due to duplicate '1' in the third column
            "* 4  ****",
            "    9 5  ",
            " 6  83  *",
            "3   1  **",
            "  8  2***",
            "  2  ****"
        ]
        self.assertFalse(validate_board(board))

    def test_invalid_color_block(self):
        board = [
            "**** ****",
            "***1 ****",
            "**  3****",
            "* 4  ****",
            "    9 5  ",
            " 6  83  *",
            "3   1  **",
            "  8  2***",
            "  3 2****"  # Invalid due to duplicate '3' in the color block 'a'
        ]
        self.assertFalse(validate_board(board))

    def test_empty_cells(self):
        board = [
            "**** ****",
            "***  ****",
            "**   ****",
            "*    ****",
            "         ",
            "        *",
            "       **",
            "      ***",
            "     ****"
        ]
        self.assertTrue(validate_board(board))

    def test_board_with_invalid_special_characters(self):
        board = [
            "****!****",
            "***1 ****",
            "**8 3****",
            "* 4 1****",
            "    9 5  ",
            " 6  83  *",
            "3   7  **",
            "  8  2***",
            "  3 2****" 
        ]
        self.assertFalse(validate_board(board))

    def test_mixed_valid_invalid_rows(self):
        board = [
            "**** ****",
            "***1 ****",
            "**8 3****",
            "* 4 1****",
            "123456789",
            "23456789*",
            "3456789**",
            "456789***",
            "56789****"
        ]
        self.assertFalse(validate_board(board))

    def test_performance_large_board(self):
        board = ["123456789" * 10] * 90  # 90x90 board
        start_time = time.time()
        result = validate_board(board)
        end_time = time.time()
        print(f"Performance test took {end_time - start_time} seconds")
        self.assertFalse(result)  # Assuming the function should handle this as invalid due to size

if __name__ == '__main__':
    unittest.main()