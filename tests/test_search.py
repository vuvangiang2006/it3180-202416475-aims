import unittest

from aims.dvd import DigitalVideoDisc
from aims.search import search_by_category, search_by_title


class TestSearch(unittest.TestCase):
    def test_search_by_category_returns_discs_in_category(self):
        items = [
            DigitalVideoDisc("The Lion King", "Animation"),
            DigitalVideoDisc("Star Wars", "Science Fiction"),
            DigitalVideoDisc("Aladdin", "Animation"),
        ]
        result = search_by_category(items, "animation")
        self.assertEqual([dvd.title for dvd in result], ["The Lion King", "Aladdin"])

    def test_search_by_title_returns_matching_discs(self):
        items = [DigitalVideoDisc("The Lion King"), DigitalVideoDisc("Star Wars")]
        result = search_by_title(items, "Lion")
        self.assertEqual([dvd.title for dvd in result], ["The Lion King"])
