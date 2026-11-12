"""Static menu photo checks. Run: python3 -m unittest discover -s tests -v."""
from html.parser import HTMLParser
from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]
PHOTO_DISHES = {
    'pork-neck', 'chicken-fillet', 'chicken-assortment',
    'lyulya-beef-lamb', 'fries', 'country-potatoes',
    'chicken-nuggets', 'khachapuri-megrelian', 'khachapuri-puff', 'set-big',
}


class MenuParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.dishes = {}
        self.current = None

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if tag == 'article' and 'data-dish' in attrs:
            self.current = attrs['data-dish']
            self.dishes[self.current] = []
        if tag == 'img' and self.current:
            self.dishes[self.current].append(attrs)

    def handle_endtag(self, tag):
        if tag == 'article':
            self.current = None


class DeliveryPhotosTest(unittest.TestCase):
    def test_identified_dishes_have_local_lazy_photos(self):
        menu = MenuParser()
        menu.feed((ROOT / 'delivery/index.html').read_text())
        self.assertEqual(len(menu.dishes), 29)
        self.assertEqual({dish for dish, imgs in menu.dishes.items() if imgs}, PHOTO_DISHES)
        for dish in PHOTO_DISHES:
            with self.subTest(dish=dish):
                self.assertEqual(len(menu.dishes[dish]), 1)
                img = menu.dishes[dish][0]
                self.assertTrue(img['src'].startswith('/assets/menu/'))
                path = ROOT / img['src'].lstrip('/')
                self.assertTrue(path.is_file(), str(path))
                self.assertLess(path.stat().st_size, 150_000)
                self.assertTrue(img.get('alt'))
                self.assertEqual(img.get('loading'), 'lazy')
                self.assertEqual(img.get('decoding'), 'async')
                self.assertGreater(int(img['width']), 0)
                self.assertGreater(int(img['height']), 0)


if __name__ == '__main__':
    unittest.main()
