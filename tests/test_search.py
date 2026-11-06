import unittest

from aims.dvd import DigitalVideoDisc
from aims.search import search_by_title


class TestSearch(unittest.TestCase):
    def test_search_by_title_returns_matching_discs(self):
        items = [DigitalVideoDisc("The Lion King"), DigitalVideoDisc("Star Wars")]
        result = search_by_title(items, "Lion")
        self.assertEqual([dvd.title for dvd in result], ["The Lion King"])
