def sum_numbers(n):
    """
    Обчислює суму чисел від 1 до n.

    >>> sum_numbers(10)
    55
    >>> sum_numbers(2)
    3
    >>> sum_numbers(0)
    Traceback (most recent call last):
    ValueError: Число має бути більше 0
    >>> sum_numbers(5)
    15
    >>> sum_numbers(-1)
    Traceback (most recent call last):
    ValueError: Число має бути більше 0
    """
    if n < 1:
        raise ValueError("Число має бути більше 0")
    return sum(i for i in range(1, n + 1))


if __name__ == "__main__":
    try:
        # Запитуємо у користувача число
        n = int(input("Введіть число n: "))

        # Обчислюємо суму та виводимо результат
        total = sum_numbers(n)
        print(f"Сума чисел від 1 до {n} дорівнює {total}")

    except ValueError as e:
        print(f"Помилка: {e}. Введіть коректне додатне число.")

    # Запуск doctest
    import doctest

    doctest.testmod()
