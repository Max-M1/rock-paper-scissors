import random

"""
Програма "Камінь-Ножиці-Папір" дозволяє грати проти комп'ютера.
Гравець вводить свій вибір (Камінь, Папір або Ножиці), після чого
комп'ютер випадковим чином вибирає свою дію. Програма визначає
переможця згідно з правилами гри та пропонує зіграти ще раз.
"""

# Можливі варіанти дій для гравця та комп'ютера
ACTIONS: dict[int, str] = {0: "Rock", 1: "Paper", 2: "Scissors"}

# Визначає, які дії перемагають інші
VICTORIES: dict[str, str] = {
    "Rock": "Scissors",  # Камінь перемагає ножиці
    "Paper": "Rock",  # Папір перемагає камінь
    "Scissors": "Paper",  # Ножиці перемагають папір
}


def get_user_selection(actions: dict[int, str]) -> str:
    """
    Отримує вибір користувача та повертає відповідну дію.
    Якщо введене значення некоректне, запит повторюється.
    """
    choices = [f"{actions[action]}[{action}]" for action in actions]
    choices_str = ", ".join(choices)

    try:
        selection: int = int(
            input(f"Enter a choice ({choices_str}): ")
        )  # Отримання вводу від користувача
        action: str = actions[selection]  # Перетворення вибору у відповідну дію
        return action
    except (ValueError, KeyError):  # Обробка некоректного вводу
        print(f"Invalid selection. Enter a value in range [0, {len(actions) - 1}]")
        return get_user_selection(actions)  # Повторний запит


def get_computer_selection(actions: dict[int, str]) -> str:
    """
    Випадковим чином обирає дію для комп'ютера.
    """
    selection: int = random.randint(0, len(actions) - 1)  # Генерація випадкового числа
    action: str = actions[selection]  # Визначення дії відповідно до числа
    return action


def determine_winner(
    victories: dict[str, str], user_action: str, computer_action: str
) -> str:
    """
    Визначає переможця гри, порівнюючи вибір користувача і комп'ютера.
    """
    if user_action == computer_action:
        return f"Both players selected {user_action}. It's a tie!"  # Нічия
    elif victories[user_action] == computer_action:
        return f"{user_action} beats {computer_action}! You win!"  # Гравець виграв
    else:
        return f"{computer_action} beats {user_action}! You lose."  # Комп'ютер виграв


if __name__ == "__main__":
    while True:
        # Отримання вибору гравця та комп'ютера
        user_selection: str = get_user_selection(ACTIONS)
        computer_selection: str = get_computer_selection(ACTIONS)

        # Виведення вибору
        print(f"You selected: {user_selection}")
        print(f"Computer selected: {computer_selection}")

        # Визначення та виведення результату гри
        result: str = determine_winner(VICTORIES, user_selection, computer_selection)
        print(result)

        # Перевірка, чи гравець хоче зіграти ще раз
        play_again: str = input("Play again? (y/n): ").strip().lower()
        if play_again != "y":  # Якщо відповідь не "y", гра завершується
            print("Thanks for playing!")
            break
