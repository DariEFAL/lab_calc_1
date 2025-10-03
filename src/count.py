from src.cheks import is_op, is_number, is_int
from src.calculate_error import CalcError


def count_rpn(expr=list[str | float]) -> float | None:
    """
    Вычесляет результат выражения в RPN
    :param expr: Список токенов в постфиксной записи
    :return: Возвращает результат выражения или None
    """

    stack: list[float] = []

    for token in expr:
        if is_number(token):
            stack.append(token)

        if is_op(token):
            try:
                op2 = stack.pop()
                op1 = stack.pop()
            except Exception:
                print("Ошибка: Неправильный ввод")
                return None

            match token:
                case '+':
                    stack.append(op1 + op2)

                case '-':
                    stack.append(op1 - op2)

                case '/':
                    try:
                        stack.append(op1 / op2)
                    except ZeroDivisionError:
                        print("Ошибка: Нельзя делить на 0")
                        return None

                case '*':
                    stack.append(op1 * op2)

                case '//':
                    try:
                        if is_int(op1) and is_int(op2):
                            stack.append(op1 // op2)
                        else:
                            raise CalcError
                    except ZeroDivisionError:
                        print("Ошибка: Нельзя делить на 0")
                        return None
                    except CalcError:
                        print("Ошибка: Использовать // можно только с целыми числами")
                        return None

                case '%':
                    try:
                        if is_int(op1) and is_int(op2):
                            stack.append(op1 % op2)
                        else:
                            raise CalcError
                    except ZeroDivisionError:
                        print("Ошибка: Нельзя взять остаток от деления на 0")
                        return None
                    except CalcError:
                        print("Ошибка: Использовать % можно только с целыми числами")
                        return None

                case '**':
                    try:
                        if op1 < 0 and (0 < op2 < 1 or -1 < op2 < 0):
                            raise CalcError
                        else:
                            stack.append(op1 ** op2)
                    except ZeroDivisionError:
                        print("Ошибка: Нельзя возвести 0 в отрицательную степень")
                        return None
                    except CalcError:
                        print("Ошибка: Нельзя взять корень из отрицательного числа")
                        return None

    try:
        if len(stack) == 1:
            return float(stack.pop())
        else:
            raise CalcError
    except CalcError:
        print("Ошибка: неправильный ввод")
        return None
