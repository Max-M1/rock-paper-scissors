def find_sum(limit):
    return sum(num for num in range(1, limit + 1))


# Приклад використання
if __name__ == "__main__":
    try:
        limit = int(input("Введіть число: "))
        if limit < 0:
            raise ValueError("Число повинно бути невід'ємним.")
        result = find_sum(limit)
        print(f"Сума чисел від 1 до {limit}: {result}")
    except ValueError as e:
        print(f"Помилка: {e}")
