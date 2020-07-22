import unittest
from src.pub import Pub
from src.drink import Drink

class TestPub(unittest.TestCase):
    def setUp(self):
        drink_1 = Drink("Whisky", 2.5)
        drink_2 = Drink("Beer", 3.1)
        drink_3 = Drink("Wine", 5.5)
        drinks = [drink_1, drink_2, drink_3]
        self.pub = Pub("The Prancing Pony", 100.00, drinks)

    def test_pub_has_name(self):
        name = self.pub.name
        self.assertEqual("The Prancing Pony", name)

    def test_pub_has_till(self):
        till_value = self.pub.till
        self.assertEqual(100.00, till_value)

    def test_pub_has_drinks(self):
        num_drinks = len(self.pub.drinks)
        self.assertEqual(3, num_drinks)

    def test_pub_can_get_money(self):
        self.pub.increase_till(5)
        new_till = self.pub.till
        self.assertEqual(105, new_till)

