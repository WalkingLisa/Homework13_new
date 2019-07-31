import json
import random
import datetime
from guessnumber_class import result

today=datetime

# Function for playing the game
def play_game():
    secret = random.randint(1, 30)
    attempts = 0
    score_list = get_score_list()

    while True:
        try:
            guess = int(input("Guess the secret number (between 1 and 30): "))
            attempts += 1

            if guess == secret:

                print("You've guessed it - congratulations! It's number " + str(secret))
                print("Attempts needed: " + str(attempts))
                player_name = input("Please enter your name for the scoreboard: ")
                newGame = result(score=attempts, player_name=player_name, date=str(today))
                with open("results.txt", "w") as result_file:
                    result_file.write(str(newGame.__dict__))
                print("Thank you for playing! Your data has been added to the scoreboard!")
                print("{0}".format(newGame.__dict__))

                break
            elif guess > secret:
                print("Your guess is not correct... try something smaller")
            elif guess < secret:
                print("Your guess is not correct... try something bigger")
        except ValueError:
            print("Please enter a valid number.")

# Get a list of all scores
def get_score_list():
    try:
        with open("scoreboard.txt", "r") as score_file:
            score_list = json.loads(score_file.read())
            return score_list
    except FileNotFoundError:
        print("Oh sorry, the file scoreboard couldn't be found.")


# Return top 3 scores
def get_top_scores():
    score_list = get_score_list()
    top_score_list = sorted(score_list, key=lambda k: k['attempts'])[:3]
    return top_score_list
