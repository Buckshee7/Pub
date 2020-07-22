import unittest
from src.customer import Customer
from src.pub import Pub
from src.drink import Drink

class TestCustomer(unittest.TestCase):
    def setUp(self):
        self.customer = Customer("Bob", 45.4)

        self.drink_1 = Drink("Whisky", 2.5)
        self.drink_2 = Drink("Beer", 3.1)
        self.drink_3 = Drink("Wine", 5.5)
        drinks = [self.drink_1, self.drink_2, self.drink_3]
        self.pub = Pub("The Prancing Pony", 100.00, drinks)

    def test_customer_has_name(self):
        name = self.customer.name
        self.assertEqual("Bob", name)

    def test_customer_has_wallet(self):
        wallet_value = self.customer.wallet
        self.assertEqual(45.4, wallet_value)

    def test_customer_can_buy_drink(self):
        self.customer.buy_drink(self.pub, self.drink_3)
        new_wallet = self.customer.wallet
        new_till = self.pub.till
        self.assertAlmostEqual(39.9,new_wallet,1)
        self.assertAlmostEqual(105.5,new_till,1)

        