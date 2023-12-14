import unittest

from parameterized import parameterized

from main import count_islands


class TestCountIslands(unittest.TestCase):

    map_1 = [
        [0, 1, 0],
        [0, 0, 0],
        [0, 1, 1],
    ]

    map_2 = [
        [0, 0, 0, 1],
        [0, 0, 1, 0],
        [0, 1, 0, 0],
    ]

    map_3 = [
        [0, 0, 0, 1],
        [0, 0, 1, 1],
        [0, 1, 0, 1],
    ]

    map_4 = [
        [0, 0, 0],
        [0, 0, 0],
    ]

    map_5 = [
        [1, 0, 1, 0, 1, 0, 1],
    ]

    map_6 = [
        [0, 0, 0, 0, 0, 0, 0],
        [0, 1, 1, 1, 1, 1, 0],
        [0, 1, 0, 0, 0, 1, 0],
        [0, 1, 0, 1, 0, 1, 0],
        [0, 1, 0, 0, 0, 1, 0],
        [0, 1, 1, 1, 1, 1, 0],
    ]

    @parameterized.expand([
        (map_1, 2),
        (map_2, 3),
        (map_3, 2),
        (map_4, 0),
        (map_5, 4),
        (map_6, 2),
    ])
    def test_count_islands(self, map, n_islands):
        self.assertEquals(
            n_islands,
            count_islands(n_rows=len(map), n_columns=len(map[0]), map=map)
        )

    def test_invalid_type(self):
        with self.assertRaises(ValueError):
            count_islands(n_rows=4, n_columns=3, map=[1, 0, 1])

    def test_invalid_n_rows(self):
        with self.assertRaises(ValueError):
            count_islands(n_rows=4, n_columns=3, map=self.map_1)

    def test_invalid_n_columns(self):
        with self.assertRaises(ValueError):
            count_islands(n_rows=3, n_columns=4, map=self.map_1)


if __name__ == '__main__':
    unittest.main()
