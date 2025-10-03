import sys

from src.calculator import calc


def main() -> None:
    """
    Обязательнная составляющая программ, которые сдаются. Является точкой входа в приложение
    :return: Данная функция ничего не возвращает
    """

    for line in sys.stdin:
        if line.rstrip() == "exit":
            sys.exit(0)
        calc(line)


if __name__ == "__main__":
    main()
