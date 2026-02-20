import random     # used for selection of a random word for the player to guess
import sys        # used for stdout terminal write and flush
import os         # used for terminal clear for responsive interactive UX
import subprocess # user for terminal clear for responsive interactive UX

# Word Library 
word_list = [
    # Animals
    "cat", "dog", "elephant", "giraffe", "lion", "tiger", "zebra", "kangaroo", "panda", "dolphin",
    "whale", "shark", "eagle", "falcon", "parrot", "penguin", "rabbit", "bear", "wolf", "fox",

    # Fruits & Vegetables
    "apple", "banana", "cherry", "grape", "orange", "pear", "peach", "plum", "mango", "kiwi",
    "tomato", "potato", "carrot", "onion", "garlic", "spinach", "broccoli", "cabbage", "pepper", "lettuce",

    # Objects
    "chair", "table", "lamp", "phone", "computer", "keyboard", "mouse", "bottle", "cup", "plate",
    "pen", "pencil", "book", "notebook", "bag", "wallet", "watch", "clock", "mirror", "door",

    # Places
    "city", "village", "mountain", "river", "ocean", "forest", "desert", "island", "beach", "valley",
    "park", "garden", "school", "university", "hospital", "market", "restaurant", "hotel", "airport", "station",

    # Verbs
    "run", "walk", "jump", "swim", "fly", "read", "write", "sing", "dance", "cook",
    "eat", "drink", "sleep", "drive", "play", "work", "study", "draw", "paint", "build",

    # Adjectives
    "happy", "sad", "angry", "excited", "tired", "hungry", "thirsty", "cold", "hot", "warm",
    "bright", "dark", "loud", "quiet", "fast", "slow", "big", "small", "long", "short"
]

game_word = "" # store word selected randomly by the game on start
user_word = "" # store correct guesses made by user in position matching game_word

# letter library - constant
letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]

# letter library - dynamically modified - as player makes guesses guessed letters are removed from gameplay
# cannot guess same letter twice
game_letters = letters

# User's incorrect letter selections are stored here
# In this version only the length of this array is relevant
# Incorrect letters could be displayed on UI if desired. Join and print this list if desired
user_errors = ["","","","","","","","",""]

# temporary storage for user input to be processed next scan prior to UI render
inp = ""

# game sequence position 
# 0=inactive, 1=playing, 2=win, 3=lose
phase = 0

# clears console for responsive interactive experience
def clear_console():
    cmd = "cls" if os.name == "nt" else "clear"
    # subprocess.call returns the command's exit code.
    subprocess.call(cmd, shell=True)

# render UI ascii art
def draw_ui():
    s1 = "|" if len(user_errors) > 0 else " "      # pole
    s2 = "-" if len(user_errors) > 1 else " "      # top rod
    s3 = "|" if len(user_errors) > 2 else " "      # rope
    s4 = "( )" if len(user_errors) > 3 else "   "  # head
    s5 = "|" if len(user_errors) > 4 else " "      # body
    s6 = "/" if len(user_errors) > 5 else " "      # left arm
    s7 = "\\" if len(user_errors) > 6 else " "     # right arm
    s8 = "/" if len(user_errors) > 7 else " "      # left leg
    s9 = "\\" if len(user_errors) > 8 else " "     # right leg

    clear_console()
    sys.stdout.write("\r\n"
                     " ||  ||  / \\  | \\  ||  /===\\ | \\  / |  / \\  | \\  ||\n"
                     " ||==|| //=\\\\ || \\ || |   __ | \\\\// | //=\\\\ || \\ ||\n"
                     " ||  ||//   \\\\||  \\ |  \\===/ |  \\/  |//   \\\\||  \\ |\n"
                     "\n"
                     f"                         {s2}{s2}{s2}{s2}{s2}{s2}{s2}{s2}\n"
                     f"                         {s3}      {s1}\n"
                     f"                        {s4}     {s1}\n"
                     f"                        {s6}{s5}{s7}     {s1}\n"
                     f"                       {s6} {s5} {s7}    {s1}\n"
                     f"                        {s8} {s9}     {s1}\n"
                     f"                       {s8}   {s9}    {s1}\n"
                     f"                                {s1}\n"
                     f"                ====================\n"
                     "\n"
                     f"{' '.join(game_letters)}\n"
                     "\n"
                     f"WORD: {''.join(user_word)}\n\n"
                     )
    sys.stdout.flush()

# main loop
# 1 - process user input from prev scan
# 2 - render UI
# 3 - prompt user for next input, input permits next scan
while True:
    # game control words
    if inp.lower() == "reset" and not phase == 0:
        phase = 0
        game_word = ""
        game_letters = letters
        user_word = ""
        user_errors = ["","","","","","","","",""]
        continue
    elif inp.lower() == "quit":
        break
    elif inp.lower() == "start" and phase == 0:
        phase = 1
        game_word = random.choice(word_list)
        game_letters = letters
        user_word = ["_"] * len(game_word)
        user_errors = []
        continue

    # game win/lose logic
    elif "".join(user_word).lower() == game_word.lower() and phase == 1:
        phase = 2
    elif len(user_errors) > 8 and phase == 1:
        phase = 3

    # render after control and game logic processing
    draw_ui()

    # prompt user for input and report game play status, phase dependent
    # phase: 0=inactive, 1=playing, 2=win, 3=lose
    inp = ""
    match phase:
        case 0:
            inp = input("to begin type START\n"
                  "to restart the game at any time, type RESET\n"
                  "to quit the game at any time, type QUIT\n\n>")
        case 1:
            inp = input("guess a letter\n\n>")

            # if input is invalid, do nothing. Control words processed next scan 
            if not inp.upper() in game_letters:
                continue

            # otherwise remove the letter from list of unplayed letters in game
            game_letters = ['_' if inp.upper() == letter else letter for letter in game_letters]

            # iterate over game word, and check for match
            # insert the letter to the user's gameplay word anywhere it matches the randomly selected game word
            letter_matched = False
            for i in range(0, len(user_word)):
                if game_word[i].upper() == inp.upper():
                    user_word[i] = inp.upper()
                    letter_matched = True

            # If a match wasn't found then the letter is added to the list of incorrect guesses.
            # The length of this array determines how many hangman components are displayed by
            # the UI render function
            if not letter_matched:
                user_errors.append(inp.upper())

        # display game end state user won or lost (result determined in pre-render steps
        case 2:
            inp = input("You won!\ntype RESET or QUIT\n\n>")
        case 3:
            inp = input(f"You lost... the word was {game_word}\ntype RESET or QUIT\n\n>")

