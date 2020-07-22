import unittest
from src.drink import Drink

class TestDrink(unittest.TestCase):
    def setUp(self):
        self.drink = Drink("Whisky", 2.5)

    def test_drink_has_name(self):
        name = self.drink.name
        self.assertEqual(name, "Whisky")

    def test_drink_has_price(self):
        price = self.drink.price
        self.assertEqual(price, 2.5)
