from .test_utils import *

from smol.itertools import *


class TestItertools(TestCase):
    def test_lookahead(self):
        data = []
        for val, is_last in lookahead([1, 2, 3, 4, 5]):
            data.append((val, is_last))

        self.eq(data, [
            (1, False),
            (2, False),
            (3, False),
            (4, False),
            (5, True),
            ])

    def test_flatten(self):
        self.eq(
                flatten([[1,2,3], [4,5,6], [7], [8,9]]),
                [1, 2, 3, 4, 5, 6, 7, 8, 9]
                )

        self.eq(
                flatten(([1,2,3], [4,5,6], [7], [8,9])),
                (1, 2, 3, 4, 5, 6, 7, 8, 9)
                )

    def test_zip_longest(self):
        self.eq(
                list(zip_longest('ABCD', [1, 2])),
                [
                    ('A', 1),
                    ('B', 2),
                    ('C', None),
                    ('D', None),
                    ]
                )

        self.eq(
                list(zip_longest('AB', [1, 2, 3, 4])),
                [
                    ('A', 1),
                    ('B', 2),
                    (None, 3),
                    (None, 4),
                    ]
                )

        self.eq(
                list(zip_longest('ABCD', [1, 2], fillvalues='#')),
                [
                    ('A', 1),
                    ('B', 2),
                    ('C', '#'),
                    ('D', '#'),
                    ]
                )

        self.eq(
                list(zip_longest('AB', [1, 2, 3, 4], fillvalues='#')),
                [
                    ('A', 1),
                    ('B', 2),
                    ('#', 3),
                    ('#', 4),
                    ]
                )

        self.eq(
                list(zip_longest('ABCD', [1, 2], fillvalues=('#', 0))),
                [
                    ('A', 1),
                    ('B', 2),
                    ('C', 0),
                    ('D', 0),
                    ]
                )

        self.eq(
                list(zip_longest('AB', [1, 2, 3, 4], fillvalues=('#', 0))),
                [
                    ('A', 1),
                    ('B', 2),
                    ('#', 3),
                    ('#', 4),
                    ]
                )
