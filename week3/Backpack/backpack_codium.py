import unittest
from backpack import Backpack, Item

class TestBackpack(unittest.TestCase):
    def setUp(self):
        # This method will run before each test method.
        self.backpack = Backpack()
        self.item1 = Item("Book", 1, 15)
        self.item2 = Item("Laptop", 5, 1500)
        self.item3 = Item("HeavyItem", 11, 20)
        self.item4 = Item("Dumbbell", 6, 100)
        self.item5 = Item("Rock", 0, 100)
        self.invalid_item = "not_an_item"

    def test_item_initialization(self):
        # Testing the initialization of an Item object.
        self.assertEqual(self.item1.name, "Book")
        self.assertEqual(self.item1.weight, 1)
        self.assertEqual(self.item1.value, 15)

    def test_item_str(self):
        # Testing the string representation of an Item object.
        self.assertEqual(str(self.item1), "Book (1 kg, $15)")

    def test_backpack_initialization(self):
        # Testing the initialization of a Backpack object.
        self.assertEqual(self.backpack._Backpack__capacity, 10)
        self.assertEqual(self.backpack.items, [])

    def test_add_item(self):
        response = self.backpack.add_item(self.item1)
        self.assertEqual(response, "Object added!")
        self.assertEqual(len(self.backpack.items), 1)
        response = self.backpack.add_item(self.item3)
        self.assertEqual(response, "Item 'HeavyItem' is too heavy for the backpack.")
        self.assertNotIn(self.item3, self.backpack.items)

    def test_remove_item(self):
        # Testing removing an item from the backpack.
        self.backpack.add_item(self.item1)
        response = self.backpack.remove_item(self.item1)
        self.assertEqual(response, "Object succesfully removed.")
        self.assertNotIn(self.item1, self.backpack.items)
        response = self.backpack.remove_item(self.item1)
        self.assertEqual(response, None)

    def test_set_capacity(self):
        Backpack.set_capacity(15)
        self.assertEqual(Backpack._Backpack__capacity, 15)

    def test_add_item_invalid(self):
        response = self.backpack.add_item(self.item5)
        self.assertEqual(response, "Item is not valid")
        self.assertNotIn(self.item5, self.backpack.items)

    def test_item_validation(self):
        self.assertFalse(Backpack.is_item_valid(self.invalid_item))
        self.assertFalse(Backpack.is_item_valid(self.item5))

    def test_items_setter(self):
        items = [self.item1, self.item2]
        self.backpack.items = items
        self.assertEqual(len(self.backpack.items), 2)
        self.assertEqual(self.backpack.items[0].name, "Book")
    
    def test_empty_backpack_properties(self):
        self.assertEqual(self.backpack.total_value, 0)
        self.assertEqual(self.backpack.total_weight, 0)

    def test_total_value_with_items(self):
        self.backpack.add_item(self.item1)
        self.backpack.add_item(self.item2)
        self.assertEqual(self.backpack.total_value, 1515)

    def test_total_weight_with_items(self):
        self.backpack.add_item(self.item1)
        self.backpack.add_item(self.item2)
        self.assertEqual(self.backpack.total_weight, 6)

    def test_str_empty_backpack(self):
        self.assertEqual(str(self.backpack), "Backpack contains 0 item with total weight 0 kg and total value $0")

    def test_str_one_item(self):
        self.backpack.add_item(self.item1)
        self.assertEqual(str(self.backpack), "Backpack contains 1 item with total weight 1 kg and total value $15")

    def test_str_multiple_items(self):
        self.backpack.add_item(self.item1)
        self.backpack.add_item(self.item2)
        self.assertTrue("2 items" in str(self.backpack) and "6 kg" in str(self.backpack) and "$1515" in str(self.backpack))

    def test_items_deleter(self):
        self.backpack.add_item(self.item1)
        del self.backpack.items
        self.assertEqual(self.backpack.items, [])

    def test_item_repr(self):
        # Testing the repr representation of an Item object.
        self.assertEqual(repr(self.item1), "Book")

    def tearDown(self):
        # This method will run after each test method.
        self.backpack.items = []
        Backpack.set_capacity(10)

if __name__ == '__main__':
    unittest.main()
