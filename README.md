# hangman-py
Console based hangman py app

## How to install:
1) Download and install python
```
https://www.python.org/downloads/
```
2) Download `hangman.py`, take note of `path` where py file is saved, like `C:\Users\<yourUserName>\Documents`
3) Open terminal and `cd` to `path`
4) run instruction
```
python hangman.py
```

## Gameplay
1) The game opens with a hangman splash screen
2) The player types `start` when prompted.
3) During game play the user may also `reset` or `quit` the game.
4) Once the game starts, hangman disappears and the user is prompted to guess letters in an unknown word.
5) Each wrong guess renders a component of the hangman.
6) Each correct guess renders the letters in the unknown word.
7) The user's goal is to guess all the letters in the unknown word before hangman is fully rendered.
8) Guessing all correct letters presents `You win!` and prompts the player to `reset` or `quit` the game.
9) If hangman is fully rendered before the player guesses all letters, the player is presented with `You lose...` and is given the unknown word.

```

 ||  ||  / \  | \  ||  /===\ | \  / |  / \  | \  ||
 ||==|| //=\\ || \ || |   __ | \\// | //=\\ || \ ||
 ||  ||//   \\||  \ |  \===/ |  \/  |//   \\||  \ |

                         --------
                         |      |
                        ( )     |
                        /|\     |
                       / | \    |
                        / \     |
                       /   \    |
                                |
                ====================

A B C D E F G H I J K L M N O P Q R S T U V W X Y Z

WORD:

to begin type START
to restart the game at any time, type RESET
to quit the game at any time, type QUIT

>
```
