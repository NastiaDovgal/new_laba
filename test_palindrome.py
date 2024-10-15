# test_palindrome.py

import unittest
from palindrome import is_palindrome

class TestPalindromeFunction(unittest.TestCase):

    def test_palindrome(self):
        """Тест на коректність розпізнавання паліндромів"""
        self.assertTrue(is_palindrome("A man a plan a canal Panama"))
        self.assertTrue(is_palindrome("Was it a car or a cat I saw"))
        self.assertTrue(is_palindrome("No 'x' in Nixon"))

    def test_not_palindrome(self):
        """Тест на коректність розпізнавання не-паліндромів"""
        self.assertFalse(is_palindrome("hello"))
        self.assertFalse(is_palindrome("world"))
        self.assertFalse(is_palindrome("python"))

    def test_empty_string(self):
        """Тест на пустий рядок (повинен бути паліндромом)"""
        self.assertTrue(is_palindrome(""))

    def test_single_character(self):
        """Тест на рядок з одного символу (повинен бути паліндромом)"""
        self.assertTrue(is_palindrome("A"))
        self.assertTrue(is_palindrome("1"))
        self.assertTrue(is_palindrome("!"))

    def test_intentional_failure(self):
        """Тест, що навмисно провалиться для демонстрації помилки"""
        self.assertTrue(is_palindrome("abc"))  # Неправильно, очікуємо False, але напишемо True для тесту

if __name__ == '__main__':
    unittest.main()
