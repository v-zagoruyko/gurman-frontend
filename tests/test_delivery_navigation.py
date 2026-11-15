"""Exercise the actual inline navigation script with anchor landing geometry."""
from pathlib import Path
import re
import subprocess
import unittest

ROOT = Path(__file__).resolve().parents[1]


class DeliveryNavigationTest(unittest.TestCase):
    def test_anchor_landing_highlights_its_section(self):
        html = (ROOT / 'delivery/index.html').read_text()
        match = re.search(r'<script>(.*?)</script>', html, re.S)
        assert match is not None, 'Delivery navigation script is missing'
        script = match.group(1)
        harness = r"""
const vm = require('node:vm');
const assert = require('node:assert/strict');
let script = '';
process.stdin.setEncoding('utf8');
process.stdin.on('data', chunk => script += chunk);
process.stdin.on('end', () => {
  // Real menu geometry at 390 px, 320 px and desktop, including subpixel rounding.
  for (const [navHeight, margin] of [[54, 80], [108, 128], [57, 80]]) {
    for (let selected = 0; selected < 4; selected++) {
      const links = ['shashlik', 'snacks', 'bakery', 'sets'].map(id => ({
        hash: '#' + id,
        current: false,
        setAttribute() { this.current = true; },
        removeAttribute() { this.current = false; }
      }));
      const sections = links.map((link, i) => ({
        id: link.hash.slice(1),
        getBoundingClientRect() { return {top: margin + 0.3 + (i - selected) * 1000}; }
      }));
      const nav = {offsetHeight: navHeight, querySelectorAll() { return links; }};
      vm.runInNewContext(script, {
        document: {querySelector(selector) {
          return selector === '.menu-nav' ? nav : sections.find(s => '#' + s.id === selector);
        }},
        window: {addEventListener() {}},
        location: {hostname: 'localhost'},
        getComputedStyle() { return {scrollMarginTop: margin + 'px'}; },
        requestAnimationFrame(callback) { callback(); }
      });
      assert.equal(links.find(link => link.current).hash, links[selected].hash,
        `nav=${navHeight}, margin=${margin}, selected=${selected}`);
    }
  }
});
"""
        result = subprocess.run(['node', '-e', harness], input=script, text=True, capture_output=True)
        self.assertEqual(result.returncode, 0, result.stderr)


if __name__ == '__main__':
    unittest.main()
