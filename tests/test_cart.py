import io
import unittest
from contextlib import redirect_stdout

from aims.cart import MAX_NUMBERS_ORDERED, Cart
from aims.dvd import DigitalVideoDisc


class TestCart(unittest.TestCase):
    def test_add_dvd_until_full(self):
        cart = Cart()
        with redirect_stdout(io.StringIO()):
            for i in range(MAX_NUMBERS_ORDERED):
                self.assertTrue(cart.add_dvd(DigitalVideoDisc(f"DVD {i + 1}")))
            self.assertFalse(cart.add_dvd(DigitalVideoDisc("DVD 21")))
        self.assertEqual(len(cart.items), MAX_NUMBERS_ORDERED)


class TestCartSort(unittest.TestCase):
    def setUp(self):
        self.cart = Cart()
        with redirect_stdout(io.StringIO()):
            self.cart.add_dvd(DigitalVideoDisc("Star Wars", cost=24.95))
            self.cart.add_dvd(DigitalVideoDisc("Aladdin", cost=18.99))
            self.cart.add_dvd(DigitalVideoDisc("The Lion King", cost=19.95))
            self.cart.add_dvd(DigitalVideoDisc("Aladdin", cost=21.00))

    def test_sort_by_title(self):
        self.cart.sort_by_title()
        self.assertEqual(
            [(dvd.title, dvd.cost) for dvd in self.cart.items],
            [("Aladdin", 21.00), ("Aladdin", 18.99), ("Star Wars", 24.95), ("The Lion King", 19.95)],
        )

    def test_sort_by_cost(self):
        self.cart.sort_by_cost()
        self.assertEqual([dvd.cost for dvd in self.cart.items], [24.95, 21.00, 19.95, 18.99])
