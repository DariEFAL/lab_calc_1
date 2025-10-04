import sys

from src.calculator import calc


def main() -> None:
    """
    Обязательнная составляющая программ, которые сдаются. Является точкой входа в приложение и отвечает за ввод
    :return: Данная функция ничего не возвращает
    """

    for line in sys.stdin:
        if line.rstrip().replace(' ', '').lower() == "exit":
            sys.exit()

        result = calc(line)

        if result is not None:
            print("Результат:", result)

if __name__ == "__main__":
    main()
