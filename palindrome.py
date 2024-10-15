# palindrome.py

def is_palindrome(s):
    """
    Функція для перевірки, чи є рядок паліндромом.

    :param s: Вхідний рядок
    :return: True, якщо рядок є паліндромом, інакше False
    """
    # Ігноруємо регістр і пробіли
    cleaned_string = ''.join(c.lower() for c in s if c.isalnum())
    return cleaned_string == cleaned_string[::-1]
