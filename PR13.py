def find_sum(limit):

    total = 0

    for num in range(1, limit + 1):
        total += num

    return total


# Приклад використання
if __name__ == "__main__":
    limit = int(input("Введіть число: "))
    result = find_sum(limit)
    print(f"Сума чисел від 1 до {limit}: {result}")
