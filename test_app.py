import unittest

import app


class TestApp(unittest.TestCase):

    def test_add(self):
        x = 5
        y = 4
        expected = x + y
        res = app.add(x, y)
        self.assertEqual(expected, res)


if __name__ == "__main__":
    unittest.main()
