from unittest.mock import patch

from src.calculator import calc


def test_number_format():
    """
    Проверяет форматы чисел
    """

    calc("0") is not None
    calc("1234567890") is not None
    calc("     1         20") is not None
    calc("1234.56789") is not None
    calc("001") is not None
    calc("0.5") is not None
    calc("0,5") is not None
    calc("0000.5000") is not None
    calc("-1.5") is not None
    calc("+   1,5") is not None
    calc("0.000000001") is not None
    calc("999999999.999999999") is not None
    calc("1.5 + 2,5") is not None

    calc(".1") is None
    calc(",1") is None
    calc("1.") is None
    calc("2..5") is None
    calc(".") is None
    calc("1.0.0") is None
    calc("1.2.3.4") is None
    calc("1,.2") is None
    calc(",.") is None
    calc("12.3444.56") is None


def test_syntax_expresion():
    """
    Проверяет синтаксес выражения
    """

    calc("") is None
    calc("   ") is None
    calc("()") is None
    calc("(") is None
    calc(")") is None
    calc("*") is None
    calc("+") is None
    calc("//") is None
    calc("%") is None
    calc("-") is None
    calc("**") is None
    calc("/") is None

    calc("1*") is None
    calc("*1") is None
    calc("2 + +1") is None
    calc("+-+1") is None
    calc("1 * -2") is None

    calc("1 * (-1)") is not None
    calc("-2 + 1") is not None
    calc("-(2 + 1)") is not None

    calc("1(") is None
    calc("(1") is None
    calc("1(2+2)") is None
    calc("(1+)") is None
    calc("(+)") is None
    calc("5+()") is None
    calc("(3*(2+1)") is None
    calc("(1-1))") is None
    calc("(1)(1)") is None

    assert calc("1 + a") is None
    assert calc("@") is None
    assert calc("1 . +  2") is None
    assert calc("1 = 2") is None
    assert calc("error") is None


def test_valid_calculator():
    """
    Проверяет выполнение валидного выражения
    """

    assert calc("2 + 3") == 5
    assert calc("5 - 3") == 2
    assert calc("2 * 3") == 6
    assert calc("6 / 2") == 3.0
    assert calc("7 // 2") == 3
    assert calc("7 % 3") == 1
    assert calc("2**3") == 8

    assert calc("2.0 + 3") == 5.0
    assert calc("1.5 + 2,5") == 4.0
    assert calc("1,5 + 2,5") == 4.0
    assert calc("0.5 * 2") == 1.0
    assert calc("3.0 // 1.0") == 3

    assert calc("-5") == -5
    assert calc("+5") == 5
    assert calc("-(2 + 3)") == -5
    assert calc("+2 * (-3)") == -6
    assert calc("-(-5)") == 5

    assert calc("2**3**2") == 512
    assert calc("(2**3)**2") == 64
    assert calc("2 + 3 * 4") == 14
    assert calc("3 * 4 + 2") == 14

    assert calc("0**0") == 1
    assert calc("-1+(-1) + (-(1+1.0))") == -4.0

    assert calc("   2   5   +   3  .     0   ") == 28.0
    assert calc("2        67+        3") == 270
    assert calc("  (  2  +  3  )  *  4  ") == 20

    assert calc("2 ** 3 * 4 + 10 // 3 - 5 % 2") == 34
    assert calc("((2 + 3) * (4 - 1)) ** 2 / 5") == 45.0
    assert calc("-(-2 ** 3) +(5 * (-2)) - (-(+4))") == 2
    assert calc("(1.5 + 2.5) ** 2 / 2.0 + 3.5 * 2.0") == 15.0
    assert calc("17 // 5 * 3 + 17 % 5 ** 2") == 26
    assert calc("-(-(-(-(5 + 3)))) * (+(2))") == 16
    assert calc("(2 ** 3 + 8 // 3) % 5 * 2.5 - 1") == -1.0
    assert calc("10 % 3 ** 2 + 15 // 4 * 2 - 1.5") == 5.5
    assert calc("2 + 3 + 4 - 5 - 1 + 10") == 13
    assert calc("(2 ** 3 ** 1) / (4 ** 2) * 10") == 5.0
    assert calc("(2 ** (1 + 2)) ** (3 - 1) / 4") == 16.0
    assert calc("(2 ** (1 + 1)) ** (0.5) ** (-1)") == 16.0


def test_error_cout_function():
    """
    Проверяет правильность вывода ошибок в cout.py
    """

    with patch('builtins.print') as mock_print:
        calc("1/0")
        mock_print.assert_called_with("Ошибка: Нельзя делить на 0")
    with patch('builtins.print') as mock_print:
        calc("1//0")
        mock_print.assert_called_with("Ошибка: Нельзя делить на 0")
    with patch('builtins.print') as mock_print:
        calc("1%0")
        mock_print.assert_called_with("Ошибка: Нельзя взять остаток от деления на 0")

    with patch('builtins.print') as mock_print:
        calc("0**(-1)")
        mock_print.assert_called_with("Ошибка: Нельзя возвести 0 в отрицательную степень")
    with patch('builtins.print') as mock_print:
        calc("-1 ** 0.5")
        mock_print.assert_called_with("Ошибка: Нельзя взять корень из отрицательного числа")

    with patch('builtins.print') as mock_print:
        calc("1.5 // 1")
        mock_print.assert_called_with("Ошибка: Использовать // можно только с целыми числами")
    with patch('builtins.print') as mock_print:
        calc("2 // 0.5")
        mock_print.assert_called_with("Ошибка: Использовать // можно только с целыми числами")
    with patch('builtins.print') as mock_print:
        calc("2.5 // 0.5")
        mock_print.assert_called_with("Ошибка: Использовать // можно только с целыми числами")
    with patch('builtins.print') as mock_print:
        calc("1.5 % 10")
        mock_print.assert_called_with("Ошибка: Использовать % можно только с целыми числами")
    with patch('builtins.print') as mock_print:
        calc("10 % 2.5")
        mock_print.assert_called_with("Ошибка: Использовать % можно только с целыми числами")
    with patch('builtins.print') as mock_print:
        calc("12.5 % 2.5")
        mock_print.assert_called_with("Ошибка: Использовать % можно только с целыми числами")


def test_error_correct_calculator():
    """
    Проверяет правильность вывода ошибок на синтаксис
    """

    with patch('builtins.print') as mock_print:
        calc("hellow + 1")
        mock_print.assert_called_with("Ошибка: Неправильный ввод")
    with patch('builtins.print') as mock_print:
        calc("1 + 1 +")
        mock_print.assert_called_with("Ошибка: Неправильный ввод")
    with patch('builtins.print') as mock_print:
        calc("2*(-3) (1)")
        mock_print.assert_called_with("Ошибка: Неправильный ввод")

    with patch('builtins.print') as mock_print:
        calc("2 * (3 + 1))")
        mock_print.assert_called_with("Ошибка: Неправильное использование скобок")
    with patch('builtins.print') as mock_print:
        calc("2 * (3 (+ 1))")
        mock_print.assert_called_with("Ошибка: Неправильное использование скобок")
    with patch('builtins.print') as mock_print:
        calc("2 * (3 (+) 1)")
        mock_print.assert_called_with("Ошибка: Неправильное использование скобок")
    with patch('builtins.print') as mock_print:
        calc("2 * ((3 +) 1)")
        mock_print.assert_called_with("Ошибка: Неправильное использование скобок")

    with patch('builtins.print') as mock_print:
        calc("2 * (3 + -1)")
        mock_print.assert_called_with("Ошибка: Несколько оператора подряд")
    with patch('builtins.print') as mock_print:
        calc("2 * (3 /// 1)")
        mock_print.assert_called_with("Ошибка: Несколько оператора подряд")

    with patch('builtins.print') as mock_print:
        calc("2.")
        mock_print.assert_called_with("Ошибка: Неправильная запись вещественного числа")
    with patch('builtins.print') as mock_print:
        calc(".3")
        mock_print.assert_called_with("Ошибка: Неправильная запись вещественного числа")
    with patch('builtins.print') as mock_print:
        calc("2.3.2")
        mock_print.assert_called_with("Ошибка: Неправильная запись вещественного числа")
    with patch('builtins.print') as mock_print:
        calc("2..3")
        mock_print.assert_called_with("Ошибка: Неправильная запись вещественного числа")
