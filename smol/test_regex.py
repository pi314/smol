from .test_utils import *

from smol.regex import *


class TestRegex(TestCase):
    def test_match(self):
        rec = rere('my smol tools')

        m = rec.match(r'^(\w+) (\w+)$')
        self.eq(m, None)

        m = rec.match(r'^(\w+) (\w+) (\w+)$')
        self.eq(m.groups(), ('my', 'smol', 'tools'))
        self.eq(m.group(2), 'smol')

        self.eq(rec.sub(r'smol', 'SMOL'), 'my SMOL tools')
