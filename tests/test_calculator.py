import unitttest

from src.calculator import add, subtract, divide

class TestCalculator(unittest.TestCase):

    def test_add(self):
        self.assertEqual(add(2,3), 5)
        self.assertEqual(add(-1, 1), 0)
        self.assertEqual(add(-1, -1), -2)
    
    def test_substract(self):
        self.assertEqual(subtract(5,3), 2)
        self.assertEqual(subtract(-1, 1), -2)
        self.assertEqual(subtract(-1, -1), 0)

    def test_divide(self):
        self.assertEqual(divide(4,2), 2)
        self.assertEqual(divide(-1, 1), -1)
        with self.assertRaises(ValueError):
                    divide(1, 0)

if __name__ == '__main__':
    unittest.main()