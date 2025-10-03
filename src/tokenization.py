import re

from src.correct import correct_expr, correct_point


def get_token(expr_str=str) -> list[str] | None:
    """
    Токенизатор
    :param expr_str: Выражение
    :return: Возвращает список токенов или None
    """

    expr_str = expr_str.replace(',', '.')
    expr_str = re.sub(r"\s*", "", expr_str)

    if not correct_expr(expr_str):
        return None

    token_re = re.compile(r"""(\d+(?:\.\d+)? | \*\* | // | [+\-/%*().])""", re.VERBOSE)
    result: list[str] = []
    buffer = ""
    tokens = re.findall(token_re, expr_str)

    if not correct_point(tokens):
        return None

    for index in range(len(tokens)):
        if tokens[index] in ('-', '+') and (not result or result[-1] == '('):
            try:
                if tokens[index+1] == '(':
                    result.append('0')
                    result.append(tokens[index])
                else:
                    buffer = tokens[index]
            except Exception:
                print("Ошибка: Неправильный ввод")
                return None

        else:
            if buffer:
                result.append(buffer + tokens[index])
                buffer = ""
            else:
                result.append(tokens[index])

    return result
