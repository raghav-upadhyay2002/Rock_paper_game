import random


def get_choices():
    player_choice = input("Enter a choice(rock, paper, scissors)")
    options = ["rock", "paper", "scissors"]
    computer_choice = random.choice(options)
    choices = {"player": player_choice, "computer": computer_choice}
    # to access a dic-->using above example
    # p_choice= choices["computer"]
    return choices


def check_win(player, computer):
    # print("You chose " + player+", Computer chose "+computer)
    # or use f before string to make above print function
    # easier eg. print("your age is "+ age)
    # we can write it as (f"your age is {age})
    print(f"Your chose {player}, computer chose {computer}")
    if player == computer:
        return "It's a tie!!"
    elif player == "rock":
        if computer == "scissors":
            return "Rock smashes scissors ! You win"
        else:
            return "Paper cover rock! You lose"
    elif player == "scissors":
        if computer == "rock":
            return "Rock smashes scissors ! You lose"
        else:
            return "Scissors cut paper! You win"
    elif player == "paper":
        if computer == "scissors":
            return "Scissors cut paper! You lose"
        else:
            return "Paper cover rock ! You win"


choices = get_choices()
result = check_win(choices["player"], choices["computer"])
print(result)
