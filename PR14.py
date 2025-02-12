import random


ACTIONS = ["Rock", "Paper", "Scissors"]


def get_user_selection(actions):
    choices = [f"{action}[{num}]" for num, action in enumerate(actions)]
    choices_str = ", ".join(choices)
    selection = int(input(f"Enter a choice ({choices_str}): "))
    user_action = actions[selection]
    return user_action


def get_computer_selection(actions):
    computer_action = random.choice(actions)
    return computer_action


def get_determine_winner(actions, user_action, computer_action):
    if user_action == computer_action:
        result = f"Both players selected {user_action}. It's a tie!\n"
    elif user_action == actions[0]:
        if computer_action == actions[2]:
            result = "Rock smashes Scissors! You win!"
        else:
            result = "Paper covers Rock! You lose."
    elif user_action == actions[1]:
        if computer_action == actions[0]:
            result = "Paper covers Rock! You win!"
        else:
            result = "Scissors cuts Paper! You lose."
    elif user_action == actions[2]:
        if computer_action == actions[1]:
            result = "Scissors cuts Paper! You win!"
        else:
            result = "Rock smashes Scissors! You lose."
    return result


if __name__ == "__main__":
    user_selection = get_user_selection(ACTIONS)
    print(user_selection)
    computer_selection = get_computer_selection(ACTIONS)
    print(computer_selection)
    determine_winner = get_determine_winner(ACTIONS, user_selection, computer_selection)
    print(determine_winner)
