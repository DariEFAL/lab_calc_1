import re

from src.calculate_error import CalcError


def correct_expr(expr_str=str) -> bool:
    """
    Проверяет выражение на правильность ввода
    :param expr_str: Выражение
    :return: Возвращает True или False
    """

    try:
        if not re.match(r"^[\d+\-/%*.()]+$", expr_str):
            raise CalcError
    except CalcError:
        print("Ошибка: Неправильный ввод")
        return False
    
    try:
        if expr_str.count('(') != expr_str.count(')'):
            raise CalcError
    except CalcError:
        print("Ошибка: Скобка без пары")
        return False
    
    try:
        if re.findall(r"\((?:\*\*|//|[+\-/%*])\)", expr_str) or \
           re.findall(r"\(\d+(?:\.\d+)?(?:\*\*|//|[+\-/%*])\)", expr_str) or \
           re.findall(r"\d+(?:\.\d+)?\((?:\*\*|//|[+\-/%*])\d+(?:\.\d+)?\)", expr_str):
            raise CalcError
    except CalcError:
        print("Ошибка: Неправильное использование скобок")
        return False
    
    try:
        if re.findall(r"[+\-%][+\-%]+", expr_str) or \
           re.findall(r"(?:\*\*|//)[*/+\-%]+|[*/+\-%]+(?:\*\*|//)", expr_str) or \
           re.findall(r"[*/][+\-%]+|[+\-%]+[*/]", expr_str):
            raise CalcError
    except CalcError:
        print("Ошибка: Несколько оператора подряд")
        return False
    
    return True


def correct_point(expr=list[str]) -> bool:
    """
    Проверяет выражение на правильность записи вещественных чисел
    :param expr_str: Выражение
    :return: Возвращает True или False
    """

    try:
        if '.' in expr:
            raise CalcError
    except CalcError:
        print("Ошибка: Неправильная запись вещественного числа")
        return False
    
    return True