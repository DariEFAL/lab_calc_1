from src.tokenization import get_token
from src.shunting_yard import shunting_yard
from src.count import count_rpn


def calc(expr_str=str) -> float | int | None:
    """
    Вызывает функции для вычесления выражения
    :param expr_str: Выражение
    :return: ничего не возвращает
    """

    tokens = get_token(expr_str)
    if tokens is None:
        return None
    print("tokens:", tokens)

    rpn_tokens = shunting_yard(tokens)
    print("rpn_tokens:", rpn_tokens)

    result = count_rpn(rpn_tokens)
    if result is None:
        return None

    return result
