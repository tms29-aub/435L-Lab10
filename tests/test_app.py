# tests/test_app.py
import unittest
from app import greet


class TestApp(unittest.TestCase):
    def test_greet(self):
        self.assertEqual(
            greet("Tamer Safa"), "Hello, World from Tamer Safa!"
        )


if __name__ == "__main__":
    unittest.main()
