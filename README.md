# ludogui
Development in progress. <br />

To do: <br />
Finalize and improve GUI. <br />
Expand the game's functionality to support three and four players. <br />

Description: <br />
Multiplayer interactive board game utilizing OOP concepts, where players move their tokens around a virtual game board. <br />

Each player is allocated two tokens, labeled 'P' and 'Q', and their goal is to move these tokens from a starting position to an ending position on the game board. The journey from start to end is measured in steps, with each token keeping track of its own step count. <br />

The game allows for four different players, each designated by a letter: 'A', 'B', 'C', or 'D'. These letters represent a specific start and end point on the game board, and the number of steps required for a token to reach the end can vary depending on the player. <br />

The game also keeps track of each player's status, which can be "Not Started", "Playing", or "Finished". The game concludes when a player reaches the end point, at which point their status changes to "Finished", and they are declared the winner. <br />

The GUI aspect of the game uses Python's Tkinter library to represent the game board and its elements. Each token's position on the board is visually represented, allowing players to see their tokens' positions relative to the start and end points, as well as to the positions of the other players' tokens. The GUI also includes buttons or other interactive elements that allow the players to move their tokens, to view the current step counts, and to start or end the game.
