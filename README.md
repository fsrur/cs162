# Board Game

## Introduction
A work-in-progress implementation of the Ludo board game in Python, using object-oriented principles to model the game's mechanics. The game also includes a graphical user interface (GUI), making it interactive and visually appealing.

### Development in progress

### To do:
Finalize and improve GUI. 

Expand the game's functionality to support three and four players. 

## Prerequisites
Ensure you have Python installed on your system to run the game. 

## Installation or Setup
Clone the repository and navigate to the project directory. No additional setup is required.

## Running the Application
You can start the game by running the gui script from the command line:

`python gui.py`

After starting the game, you can interact with the GUI to roll the dice and move your tokens around the board.

## Usage
Once the game is running, interact with the GUI to roll the dice and move your tokens following the rules of the game. The goal is to get all your tokens to the finish line.

## Project Structure and Implementation Details

### Player Class
Each <b>'Player'</b> object represents a player in the game. It has methods to get and set the player's status, token position, and other related attributes.

See the <b>'player.py'</b> file for the class implementation.

### LudoGame Class
The <b>'LudoGame'</b> class manages the game's mechanics. It does not have any data members. Instead, it utilizes methods from the <b>'Player'</b> class to update the game state. It also has a method <b>'set_players'</b>, which sets the number of players in the game.

In <b>'LudoGame'</b>, the <b>'play_game'</b> method takes a list of turns and a list of player selections as parameters. This method then moves each player's tokens according to the game rules and updates the token step count for each player.

See the <b>'game.py'</b> file for the class implementation.

### GUI
In addition to the game logic implementation, this repository includes a graphical user interface (GUI) for the Ludo game, built with Python's Tkinter library.

See the <b>'gui.py'</b> file for the gui implementation.

