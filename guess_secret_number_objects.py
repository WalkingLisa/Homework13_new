from guessnumber_func import play_game
from guessnumber_func import get_top_scores



print("Welcome to this wonderful game!")

# Run the game
while True:
    try:
        selection = input("Would you like to A) play a new game, B) see the best scores, or C) quit? ")

        if selection.upper() == "A":
            play_game()
        elif selection.upper() == "B":
            for score_dict in get_top_scores():
                print(str(score_dict["attempts"]) + " attempts, date: " + score_dict.get("date"))
        elif selection.upper() == "C":
            break
    except ValueError:
        print("This is no valid option. Please try again.")

