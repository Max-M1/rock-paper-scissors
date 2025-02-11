def sum_numbers():
    n = int(input("Введіть число: "))

    if n < 1:
        print("Будь ласка, введіть число більше або рівне 1.")
        return

    total = sum(i for i in range(1, n + 1))
    print(f"Сума чисел від 1 до {n} дорівнює {total}")


if __name__ == "__main__":
    sum_numbers()
