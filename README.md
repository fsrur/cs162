# ludogui

### Development in progress

## To do:
Finalize and improve GUI. 

Expand the game's functionality to support three and four players. 

## Ludo Game Implementation in Python
This repository contains an implementation of the Ludo game in Python. This implementation uses object-oriented principles to model the game's mechanics.

The main classes in this implementation are:

- <b>'Player'</b>: Represents each player participating in the game.
- <b>'LudoGame'</b>: Manages the game's mechanics, including the movement of player tokens according to game rules.

## Player Class

Each <b>'Player'</b> object represents a player in the game. It has methods to get and set the player's status, token position, and other related attributes.

See the <b>'player.py'</b> file for the class implementation.

## LudoGame Class

The <b>'LudoGame'</b> class manages the game's mechanics. It does not have any data members. Instead, it utilizes methods from the <b>'Player'</b> class to update the game state. It also has a method <b>'set_players'</b>, which sets the number of players in the game.

In <b>'LudoGame'</b>, the <b>'play_game'</b> method takes a list of turns and a list of player selections as parameters. This method then moves each player's tokens according to the game rules and updates the token step count for each player.

See the <b>'game.py'</b> file for the class implementation.

## GUI
In addition to the game logic implementation, this repository includes a graphical user interface (GUI) for the Ludo game, built with Python's Tkinter library. This makes the game more interactive and visually appealing.

See the <b>'gui.py'</b> file for the gui implementation.

## How to Run the Game
You can start the game by running the gui script from the command line:

`python gui.py`

After starting the game, you can interact with the GUI to roll the dice and move your tokens around the board.
