from src.cheks import is_number, is_op
from src.constants import OP_PRIO


def shunting_yard(expr=list[str]) -> list[str | float]:
    """
    Алгоритм шунтирующего двора со скобками
    :param expr: Список токенов в инфиксной записи
    :return: Возвращает список токенов в постфиксной записи
    """

    result: list[str | float] = []
    op_stack: list[str] = []

    for token in expr:
        if is_number(token):
            result.append(float(token))

        elif is_op(token):
            while op_stack and is_op(op_stack[-1]) and OP_PRIO[token] <= OP_PRIO[op_stack[-1]]:
                result.append(op_stack.pop())
            op_stack.append(token)

        elif token == '(':
            op_stack.append(token)

        elif  token == ')':
            while op_stack[-1] != '(':
                result.append(op_stack.pop())
            op_stack.pop()

    while op_stack:
        result.append(op_stack.pop())

    return result
