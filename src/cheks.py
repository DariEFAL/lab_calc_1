from src.constants import OP_PRIO


def is_number(token=str) -> bool:
    """
    Проверяет является ли токен числом или нет
    :param token: Токен
    :return: Возвращает либо True, либо False
    """

    try:
        float(token)
        return True
    except Exception:
        return False


def is_int(op=float) -> int:
    """
    Проверяет является ли число целым для целочисленных операций (//, %)
    :param op: операнд
    :return: Возвращает либо True, либо False
    """

    if int(op) == op:
        return True
    return False


def is_op(token=str) -> bool:
    """
    Проверяет является ли токен операцией или нет
    :param token: Токен
    :return: Возвращает либо True, либо False
    """

    return token in OP_PRIO
