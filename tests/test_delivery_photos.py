"""Static menu photo checks. Run: python3 -m unittest discover -s tests -v."""
from html.parser import HTMLParser
from hashlib import sha256
from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]
PHOTO_DISHES = {
    'pork-neck', 'chicken-fillet', 'chicken-assortment',
    'lyulya-beef-lamb', 'fries', 'country-potatoes',
    'chicken-nuggets', 'khachapuri-megrelian', 'khachapuri-puff', 'set-big',
    'lamb-on-bone', 'salmon-steak', 'lyulya-pork-beef',
    'grilled-vegetables', 'pizza-pepperoni',
    'chicken-wings', 'grilled-mushrooms', 'khachapuri-adjarian', 'pizza-ham', 'set-two',
    'pizza-cheese', 'pizza-chicken', 'pork-loin', 'lavash-thin', 'lyulya-chicken',
}
PAIRED_PHOTOS = {'chicken-fillet', 'chicken-assortment', 'lamb-on-bone', 'pork-neck',
                 'chicken-wings', 'lyulya-pork-beef', 'lyulya-beef-lamb', 'pork-loin'}


class MenuParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.dishes = {}
        self.current = None
        self.portions = {}
        self.portion = None

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if tag == 'article' and 'data-dish' in attrs:
            self.current = attrs['data-dish']
            self.dishes[self.current] = []
            self.portions[self.current] = []
        if tag == 'figure' and self.current and 'data-portion' in attrs:
            self.portion = {'weight': attrs['data-portion'], 'images': [], 'prices': []}
            self.portions[self.current].append(self.portion)
        if tag == 'img' and self.current:
            self.dishes[self.current].append(attrs)
            if self.portion is not None:
                self.portion['images'].append(attrs['src'])
        if tag == 'data' and self.portion is not None:
            self.portion['prices'].append(attrs['value'])

    def handle_endtag(self, tag):
        if tag == 'figure':
            self.portion = None
        if tag == 'article':
            self.current = None


class DeliveryPhotosTest(unittest.TestCase):
    def test_selected_shashliks_show_each_portion_with_its_own_price_and_photo(self):
        menu = MenuParser()
        menu.feed((ROOT / 'delivery/index.html').read_text())
        expected = {
            'pork-neck': [('200', '300', 'pork-neck-200g.webp'), ('1000', '1430', 'pork-neck.webp')],
            'pork-ribs': [('200', '300', None), ('1000', '1430', None)],
            'chicken-assortment': [('200', '260', 'chicken-assortment.webp'), ('1000', '950', 'chicken-assortment-1kg.webp')],
            'pork-loin': [('200', '300', 'pork-loin-200g.webp'), ('1000', '1430', 'pork-loin-1kg.webp')],
            'chicken-fillet': [('200', '280', 'chicken-fillet.webp'), ('1000', '1100', 'chicken-fillet-1kg.webp')],
            'lamb-on-bone': [('150', '650', 'lamb-on-bone.webp'), ('750', '3250', 'lamb-on-bone-750g.webp')],
            'chicken-wings': [('200', '280', 'chicken-wings.webp'), ('1000', '1000', 'chicken-wings-1kg.webp')],
            'salmon-steak': [('150', '450', 'salmon-steak.webp'), ('750', '2250', None)],
            'lyulya-pork-beef': [('200', '390', 'lyulya-pork-beef-200g.webp'), ('1000', '1400', 'lyulya-pork-beef-1kg.webp')],
            'lyulya-beef-lamb': [('200', '390', 'lyulya-beef-lamb.webp'), ('1000', '1500', 'lyulya-beef-lamb-1kg.webp')],
            'lyulya-chicken': [('200', '390', 'lyulya-chicken-200g.webp'), ('1000', '1500', None)],
        }
        self.assertEqual({dish for dish, portions in menu.portions.items() if portions}, set(expected))
        for dish, portions in expected.items():
            with self.subTest(dish=dish):
                actual = [(p['weight'], p['prices'], p['images']) for p in menu.portions[dish]]
                self.assertEqual(actual, [(weight, [price], ['/assets/menu/' + photo] if photo else []) for weight, price, photo in portions])

    def test_salmon_labels_the_missing_portion_photo(self):
        html = (ROOT / 'delivery/index.html').read_text()
        card = html.split('data-dish="salmon-steak"')[1].split('</article>')[0]
        missing = card.split('data-portion="750"', 1)
        self.assertEqual(len(missing), 2)
        self.assertIn('Фото порции<br>пока нет', missing[1].split('</figure>', 1)[0])

    def test_chicken_cards_use_confirmed_200g_photos(self):
        menu = MenuParser()
        menu.feed((ROOT / 'delivery/index.html').read_text())
        expected = {
            'chicken-fillet': 'c20aca558b53c7a463bb71b9f436a12fdb7ee3c13fdf9973daabdce5486f911f',
            'chicken-assortment': 'e0281b140b52666d1b278b8f9d904e7171faf60bf8844832ce059f5fa21e66af',
        }
        for dish, digest in expected.items():
            with self.subTest(dish=dish):
                photo = ROOT / menu.dishes[dish][0]['src'].lstrip('/')
                self.assertEqual(sha256(photo.read_bytes()).hexdigest(), digest)

    def test_identified_dishes_have_local_lazy_photos(self):
        menu = MenuParser()
        menu.feed((ROOT / 'delivery/index.html').read_text())
        self.assertEqual(len(menu.dishes), 29)
        self.assertEqual({dish for dish, imgs in menu.dishes.items() if imgs}, PHOTO_DISHES)
        for dish in PHOTO_DISHES:
            with self.subTest(dish=dish):
                self.assertEqual(len(menu.dishes[dish]), 2 if dish in PAIRED_PHOTOS else 1)
                for img in menu.dishes[dish]:
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
