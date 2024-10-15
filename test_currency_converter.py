# test_currency_converter.py

import unittest
from currency_converter import usd_to_eur, eur_to_usd, usd_to_uah, uah_to_usd, uah_to_eur

class TestCurrencyConverter(unittest.TestCase):

    def test_usd_to_eur(self):
        # Тестування правильних конвертацій
        self.assertAlmostEqual(usd_to_eur(100), 90.0)  # 100 USD = 90 EUR
        self.assertAlmostEqual(usd_to_eur(0), 0.0)      # 0 USD = 0 EUR

    def test_eur_to_usd(self):
        # Тестування правильних конвертацій
        self.assertAlmostEqual(eur_to_usd(100), 108.0)  # 100 EUR = 108 USD
        self.assertAlmostEqual(eur_to_usd(0), 0.0)       # 0 EUR = 0 USD

    def test_usd_to_uah(self):
        # Тестування правильних конвертацій
        self.assertAlmostEqual(usd_to_uah(100), 4100.0)  # 100 USD = 4100 UAH
        self.assertAlmostEqual(usd_to_uah(0), 0.0)        # 0 USD = 0 UAH

    def test_uah_to_usd(self):
        # Тестування правильних конвертацій
        self.assertAlmostEqual(uah_to_usd(100), 2.4)     # 100 UAH = 2.4 USD
        self.assertAlmostEqual(uah_to_usd(0), 0.0)        # 0 UAH = 0 USD

    def test_uah_to_eur(self):
        # Тестування правильних конвертацій
        self.assertAlmostEqual(uah_to_eur(100), 2.1)      # 100 UAH = 2.1 EUR
        self.assertAlmostEqual(uah_to_eur(0), 0.0)        # 0 UAH = 0 EUR

    def test_invalid_input(self):
        # Тестування на неправильний вхід (має бути число)
        with self.assertRaises(TypeError):
            usd_to_eur("100")  # Має викликати помилку
        with self.assertRaises(TypeError):
            eur_to_usd("100")  # Має викликати помилку
        with self.assertRaises(TypeError):
            usd_to_uah("100")  # Має викликати помилку
        with self.assertRaises(TypeError):
            uah_to_usd("100")  # Має викликати помилку
        with self.assertRaises(TypeError):
            uah_to_eur("100")  # Має викликати помилку

if __name__ == "__main__":
    unittest.main()
