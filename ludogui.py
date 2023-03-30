import random
from tkinter import *

class Player:
    """Class Player has one data member: player. It keeps track of step count for both Player's token (P and Q),
    Player's status ("Playing" or "Finished"), Player's completions status (True or False) and Player's position
    on the board"""

    def __init__(self, player):
        """Initializes the player, token step count to -1 (both P and Q tokens), player_status to "NOT STARTED",
        completed to False, and position of the board to -1 (both P and Q tokens)"""
        self._player_selection = player
        self._token_p_step_count = -1
        self._token_q_step_count = -1
        self._player_status = "NOT STARTED"
        self._completed = False
        self._position_on_board_p = -1
        self._position_on_board_q = -1

    # Player selection
    def get_player_selection(self):
        """Returns player_selection ('A', 'B', 'C' or 'D') for the Player object"""
        return self._player_selection

    # Each players' start and end space
    def get_player_start_end_space(self):
        """Returns Player's start and end spaces"""
        if self._player_selection == "A":
            return ["start = 1", "end = 50"]
        elif self._player_selection == "A":
            return ["start = 15", "end = 8"]
        elif self._player_selection == "C":
            return ["start = 29", "end = 22"]
        else:
            return ["start = 43", "end = 35"]

    # Step count for P and Q tokens
    def get_token_p_step_count(self):
        """Returns Player's P token step count"""
        return self._token_p_step_count

    def set_token_p_step_count(self, pos):
        """Takes number of steps to add as parameter. Sets Player's P token step count"""
        self._token_p_step_count += pos

    def get_token_q_step_count(self):
        """Returns Player's Q token step count"""
        return self._token_q_step_count

    def set_token_q_step_count(self, pos):
        """Takes number of steps to add as parameter. Sets Player's Q token step count"""
        self._token_q_step_count += pos

    # Player status (playing, or finished)
    def get_player_status(self):
        """Returns Player's status ("PLAYING" OR "FINISHED")"""
        return self._player_status

    def set_player_status(self, pos):
        """Takes status as parameter. Sets Player's status ("PLAYING" OR "FINISHED")"""
        self._player_status = pos

    # Returns name of space based on token total steps
    def get_space_name(self, steps_taken):
        """Takes number of steps taken as parameter. Returns Player's space name"""
        if steps_taken == 0:
            return "R"
        elif steps_taken == -1:
            return "H"
        elif steps_taken == 57:
            return "E"
        elif steps_taken <= 50:
            if self._player_selection == 'A':
                return str(steps_taken)
            elif self._player_selection == 'B':
                if steps_taken <= 42:
                    return str(steps_taken + 14)
                elif steps_taken >= 43:
                    return str(steps_taken - 42)
            elif self._player_selection == 'C':
                if steps_taken <= 28:
                    return str(steps_taken + 28)
                elif steps_taken >= 29:
                    return str(steps_taken - 28)
            elif self._player_selection == 'D':
                if steps_taken <= 14:
                    return str(steps_taken + 42)
                elif steps_taken >= 15:
                    return str(steps_taken - 14)
        elif 57 > steps_taken > 50:
            last_spots = steps_taken - 50
            return str(self._player_selection) + str(last_spots)

    # Returns True if player has finished the game, otherwise returns False
    def get_completed(self):
        """Returns True if Player has finished the game, otherwise returns False"""
        return self._completed

    def set_completed(self, pos):
        """Takes completion status as parameter. Sets True if Player has finished the game, otherwise returns False"""
        self._completed = pos

    # Position on board, based on start and end spots for P token
    def get_position_on_board_p(self):
        """Returns position on the board, for Player's P token"""
        if self._player_selection == "A" and self.get_token_p_step_count() <= 50:
            return self.get_token_p_step_count()
        elif self._player_selection == "A" and self.get_token_p_step_count() > 50:
            return self.get_space_name(self.get_token_p_step_count())

        elif self._player_selection == "B" and self.get_token_p_step_count() <= 42:
            return self.get_token_p_step_count() + 14
        elif self._player_selection == "B" and 50 >= self.get_token_p_step_count() >= 43:
            return self.get_token_p_step_count() - 42
        elif self._player_selection == "B" and self.get_token_p_step_count() > 50:
            return self.get_space_name(self.get_token_p_step_count())

        elif self._player_selection == "C" and self.get_token_p_step_count() <= 28:
            return self.get_token_p_step_count() + 28
        elif self._player_selection == "C" and 50 >= self.get_token_p_step_count() >= 29:
            return self.get_token_p_step_count() - 28
        elif self._player_selection == "C" and self.get_token_p_step_count() > 50:
            return self.get_space_name(self.get_token_p_step_count())

        elif self._player_selection == "D" and self.get_token_p_step_count() <= 14:
            return self.get_token_p_step_count() + 42
        elif self._player_selection == "D" and 50 >= self.get_token_p_step_count() >= 15:
            return self.get_token_p_step_count() - 14
        elif self._player_selection == "D" and self.get_token_p_step_count() > 50:
            return self.get_space_name(self.get_token_p_step_count())

    # Position on board, based on start and end spots for Q token
    def get_position_on_board_q(self):
        """Returns position on the board, for Player's Q token"""
        if self._player_selection == "A" and self.get_token_q_step_count() <= 50:
            return self.get_token_q_step_count()
        elif self._player_selection == "A" and self.get_token_q_step_count() > 50:
            return self.get_space_name(self.get_token_q_step_count())

        elif self._player_selection == "B" and self.get_token_q_step_count() <= 42:
            return self.get_token_q_step_count() + 14
        elif self._player_selection == "B" and 50 >= self.get_token_q_step_count() >= 43:
            return self.get_token_q_step_count() - 42
        elif self._player_selection == "B" and self.get_token_q_step_count() > 50:
            return self.get_space_name(self.get_token_q_step_count())

        elif self._player_selection == "C" and self.get_token_q_step_count() <= 28:
            return self.get_token_q_step_count() + 28
        elif self._player_selection == "C" and 50 >= self.get_token_q_step_count() >= 29:
            return self.get_token_q_step_count() - 28
        elif self._player_selection == "C" and self.get_token_q_step_count() > 50:
            return self.get_space_name(self.get_token_q_step_count())

        elif self._player_selection == "D" and self.get_token_q_step_count() <= 14:
            return self.get_token_q_step_count() + 42
        elif self._player_selection == "D" and 50 >= self.get_token_q_step_count() >= 15:
            return self.get_token_q_step_count() - 14
        elif self._player_selection == "D" and self.get_token_q_step_count() > 50:
            return self.get_space_name(self.get_token_q_step_count())


class LudoGame:
    """Class LudoGame has no data members. It moves Player's tokens (P and Q) according to the game rules, and updates
    the various methods in class Player"""

    def __init__(self):
        """Initializes an empty array of Player objects"""
        self._players_obj = []

    def get_players_obj(self):
        """Returns a list of Player objects playing the game"""
        return self._players_obj

    def set_players(self, num_of_players):
        player_list_2 = ['A', 'B']
        player_list_3 = ['A', 'B', 'C']
        player_list_4 = ['A', 'B', 'C', 'D']
        if num_of_players == 2:
            for i in player_list_2:
                self._players_obj.append(Player(i))
        elif num_of_players == 3:
            for i in player_list_3:
                self._players_obj.append(Player(i))
        elif num_of_players == 4:
            for i in player_list_4:
                self._players_obj.append(Player(i))

    # Player by letter selections
    def get_player_by_position(self, player_pos):
        """Takes Player's letter selection('A', 'B', 'C, or 'D) as parameter. Returns Player object"""
        count = 0
        for player in range(0, len(self._players_obj)):
            if self._players_obj[player].get_player_selection() == player_pos:
                count += 1
        if count == 0:
            return "Player not found!"
        else:
            for player in range(0, len(self._players_obj)):
                if self._players_obj[player].get_player_selection() == player_pos:
                    return self._players_obj[player]  # returns Player object

    # Sets token step count, from class Player
    def move_token(self, player_obj, token_name, steps):
        """Takes Player object, token name ('p' or 'q') and number of steps taken. Sets token (either p or q) step count"""
        if token_name == "p":
            player_obj.set_token_p_step_count(steps)
        elif token_name == "q":
            player_obj.set_token_q_step_count(steps)
        else:
            print("Error")

    # Moves players' P and Q according to the game rules. Uses move_token method to update token step count for each player.
    def play_game(self, turn):
        """Takes a list of letter selections (players) and a list of turns as parameters. Moves players' P and Q tokens
        according to the game rules. Uses move_token method to update token step count for each player. Returns
        a list of positions on the board, for each player's tokens"""
        if len(self._players_obj) > 1:
            # print(self._players_obj)
            # Changes players' status
            for player in self.get_players_obj():
                player.set_player_status("PLAYING")

            # -1(HOME), 0(READY), > 0(SOMEWHERE ON BOARD)
            # for turn in turns:
            player = self.get_player_by_position(turn[0])

            # If both tokens count equal to 57 (E).
            if player.get_token_p_step_count() == 57 and player.get_token_q_step_count() == 57:
                self.move_token(player, "p", 0)
                self.move_token(player, "q", 0)
                player.set_completed(True)
                player.set_player_status("FINISHED")

            # If both P and Q tokens land in the same spot on the BOARD, P and Q move together, until the end or until kicked back HOME by opponent
            elif player.get_token_p_step_count() == player.get_token_q_step_count() and player.get_token_p_step_count() > 0 and player.get_token_q_step_count() > 0:
                # If tokens move goes over 57 (doesn't land on E). Only reference P, because P and Q would move together.
                if player.get_token_p_step_count() + turn[1] > 57:
                    self.move_token(player, "p", ((57 - player.get_token_p_step_count()) - turn[1] + (57 - player.get_token_p_step_count())))
                    self.move_token(player, "q", ((57 - player.get_token_q_step_count()) - turn[1] + (57 - player.get_token_q_step_count())))
                else:
                    self.move_token(player, "p", turn[1])
                    self.move_token(player, "q", turn[1])

            # If tokens are not together

            # Rolls 6 to move P or Q out of HOME
            elif turn[1] == 6 and player.get_token_p_step_count() == -1:  # Q is anywhere, including HOME
                self.move_token(player, "p", 1)
            elif turn[1] == 6 and player.get_token_q_step_count() == -1:  # If P is not HOME, move Q
                self.move_token(player, "q", 1)

            # If turn gets player to 57
            elif 1 <= turn[1] <= 6 and player.get_token_p_step_count() + turn[1] == 57:
                self.move_token(player, "p", turn[1])
            elif 1 <= turn[1] <= 6 and player.get_token_q_step_count() + turn[1] == 57:
                self.move_token(player, "q", turn[1])

            # If at least one token ON BOARD and cannot get to 57
            else:
                list_of_players = list(self._players_obj)
                list_of_players.remove(player)  # Remove player from list, to avoid comparing to player with itself.
                counter_p = 0
                counter_q = 0
                # Loop to iterate through list with other players.
                if turn[1] + player.get_token_p_step_count() < 51:
                    for other_player in list_of_players:
                        # Player's P token lands in other players P token spot or player's P token lands in other players Q token spot
                        if turn[1] + player.get_position_on_board_p() == other_player.get_position_on_board_p() or turn[1] + player.get_position_on_board_p() == other_player.get_position_on_board_q():
                            counter_p += 1
                if turn[1] + player.get_token_q_step_count() < 51:
                    for other_player in list_of_players:
                        # Player's Q token can land in other players P token spot or player's Q token can land in other players Q token spot
                        if turn[1] + player.get_position_on_board_q() == other_player.get_position_on_board_p() or turn[1] + player.get_position_on_board_q() == other_player.get_position_on_board_q():
                            counter_q += 1
                # If a token can be sent HOME. P moves first. If P cannot send another token HOME, Q moves.
                if counter_p > 0:
                    for other_player in list_of_players:
                        # Player's P token lands in other players P token spot
                        if turn[1] + player.get_position_on_board_p() == other_player.get_position_on_board_p():
                            self.move_token(player, "p", turn[1])
                            counter_p += 1
                        # Player's P token lands in other players Q token spot
                        elif turn[1] + player.get_position_on_board_p() == other_player.get_position_on_board_q():
                            self.move_token(player, "p", turn[1])
                            counter_p += 1
                elif counter_q > 0:
                    for other_player in list_of_players:
                        # Player's Q token can land in other players P token spot
                        if turn[1] + player.get_position_on_board_q() == other_player.get_position_on_board_p():
                            self.move_token(player, "q", turn[1])
                            counter_q += 1
                        # Player's Q token can land in other players Q token spot
                        elif turn[1] + player.get_position_on_board_q() == other_player.get_position_on_board_q():
                            self.move_token(player, "q", turn[1])
                            counter_q += 1

                # If another player cannot be sent HOME
                elif counter_p == 0 and counter_q == 0:
                    # Player has a token ON BOARD and a token HOME
                    if player.get_token_p_step_count() == -1 or player.get_token_q_step_count() == -1:
                        if player.get_token_p_step_count() > -1:
                            if player.get_token_p_step_count() + turn[1] > 57:
                                self.move_token(player, "p", ((57 - player.get_token_p_step_count()) - turn[1] + (57 - player.get_token_p_step_count())))
                            else:
                                self.move_token(player, "p", turn[1])
                        elif player.get_token_q_step_count() > -1:
                            if player.get_token_q_step_count() + turn[1] > 57:
                                self.move_token(player, "q", ((57 - player.get_token_q_step_count()) - turn[1] + (57 - player.get_token_q_step_count())))
                            else:
                                self.move_token(player, "q", turn[1])
                    # Player has both tokens ON BOARD
                    # P further away from ending than Q
                    elif player.get_token_p_step_count() < player.get_token_q_step_count():
                        if player.get_token_p_step_count() + turn[1] > 57:
                            self.move_token(player, "p", ((57 - player.get_token_p_step_count()) - turn[1] + (57 - player.get_token_p_step_count())))
                        else:
                            self.move_token(player, "p", turn[1])
                    # Q further away from ending than P
                    elif player.get_token_q_step_count() < player.get_token_p_step_count():
                        if player.get_token_q_step_count() + turn[1] > 57:
                            self.move_token(player, "q", ((57 - player.get_token_q_step_count()) - turn[1] + (57 - player.get_token_q_step_count())))
                        else:
                            self.move_token(player, "q", turn[1])
                    # Both P and Q are ready
                    elif player.get_token_q_step_count() == player.get_token_p_step_count():
                        self.move_token(player, "p", turn[1])

            # Check to see if player landed in spot already occupied by another player. Sends other player back HOME
            list_of_players = list(self._players_obj)
            list_of_players.remove(player) # Remove player from list, to avoid comparing to player with itself.
            # Loop to iterate through list with other players. If statement, instead of elif, in case P and Q tokes are together.
            for other_player in list_of_players:
                # Player's P token lands in other players P token spot
                if player.get_position_on_board_p() == other_player.get_position_on_board_p() and player.get_token_p_step_count() > 0:
                    self.move_token(other_player, "p", -(other_player.get_token_p_step_count()+1))
                # Player's P token lands in other players Q token spot
                if player.get_position_on_board_p() == other_player.get_position_on_board_q() and player.get_token_p_step_count() > 0:
                    self.move_token(other_player, "q", -(other_player.get_token_q_step_count()+1))
                # Player's Q token lands in other players P token spot
                if player.get_position_on_board_q() == other_player.get_position_on_board_p() and player.get_token_q_step_count() > 0:
                    self.move_token(other_player, "p", -(other_player.get_token_p_step_count()+1))
                # Player's Q token lands in other players Q token spot
                if player.get_position_on_board_q() == other_player.get_position_on_board_q() and player.get_token_q_step_count() > 0:
                    self.move_token(other_player, "q", -(other_player.get_token_q_step_count()+1))

        # Returns a list with the positions of the different players' tokens, with H for HOME (-1) and R for READY (0)
        list_of_players_pos = []
        for player in self._players_obj:
            if player.get_token_p_step_count() == -1:
                list_of_players_pos.append("H")
            elif player.get_token_p_step_count() == 0:
                list_of_players_pos.append("R")
            else:
                list_of_players_pos.append(player.get_position_on_board_p())
            if player.get_token_q_step_count() == -1:
                list_of_players_pos.append("H")
            elif player.get_token_q_step_count() == 0:
                list_of_players_pos.append("R")
            else:
                list_of_players_pos.append(player.get_position_on_board_q())
        return list_of_players_pos

#################################
# GUI
#################################
root = Tk()

root.title("Ludo")
root.geometry("680x680")

game = LudoGame()

# Top row (1 - 15)
for i in range(0, 15):
    if i == 0:
        sqr1 = Canvas(root, width=40, height=40, bg="#FFD580", highlightthickness=1, highlightbackground="black")
        sqr1.grid(row=0, column=i)
        sqr1.create_text(20, 20, text=i+1, font=('Helvetica 15'))
    elif i == 7 or i == 14:
        sqr8_15 = Canvas(root, width=40, height=40, bg="#ADD8E6", highlightthickness=1, highlightbackground="black")
        sqr8_15.grid(row=0, column=i)
        sqr8_15.create_text(20, 20, text=i+1, font=('Helvetica 15'))
    else:
        sqr = Canvas(root, width=40, height=40, bg="white", highlightthickness=1, highlightbackground="black")
        sqr.grid(row=0, column=i)
        sqr.create_text(20, 20, font=('Helvetica 15'))

# Right side (15 - 29)
for i in range(1, 15):
    if i == 7:
        sqr22 = Canvas(root, width=40, height=40, bg="#FFC0CB", highlightthickness=1, highlightbackground="black")
        sqr22.grid(row=i, column=14)
        sqr22.create_text(20, 20, text="22", font=('Helvetica 15'))
    elif i == 14:
        sqr29 = Canvas(root, width=40, height=40, bg="#FFC0CB", highlightthickness=1, highlightbackground="black")
        sqr29.grid(row=i, column=14)
        sqr29.create_text(20, 20, text="29", font=('Helvetica 15'))
    else:
        sqr = Canvas(root, width=40, height=40, bg="white", highlightthickness=1, highlightbackground="black")
        sqr.grid(row=i, column=14)
        sqr.create_text(20, 20, font=('Helvetica 15'))

# Bottom row (29 - 43)
for i in range(0, 14):
    if i == 0:
        sqr43 = Canvas(root, width=40, height=40, bg="#90ee90", highlightthickness=1, highlightbackground="black")
        sqr43.grid(row=14, column=i)
        sqr43.create_text(20, 20, text="43", font=('Helvetica 15'))
    elif i == 7:
        sqr36 = Canvas(root, width=40, height=40, bg="#90ee90", highlightthickness=1, highlightbackground="black")
        sqr36.grid(row=14, column=i)
        sqr36.create_text(20, 20, text="36", font=('Helvetica 15'))
    else:
        sqr = Canvas(root, width=40, height=40, bg="white", highlightthickness=1, highlightbackground="black")
        sqr.grid(row=14, column=i)
        sqr.create_text(20, 20, font=('Helvetica 15'))

# Left side (43 - 56)
for i in range(1, 14):
    if i == 7:
        sqr50 = Canvas(root, width=40, height=40, bg="#FFD580", highlightthickness=1, highlightbackground="black")
        sqr50.grid(row=i, column=0)
        sqr50.create_text(20, 20, text="50", font=('Helvetica 15'))
    else:
        sqr = Canvas(root, width=40, height=40, bg="white", highlightthickness=1, highlightbackground="black")
        sqr.grid(row=i, column=0)
        sqr.create_text(20, 20, font=('Helvetica 15'))

# Final squares
for i in range(7, 51, 14):
    x = 7
    if i == 7:
        for j in range(1, 7):
            blue_sqr = Canvas(root, width=40, height=40, bg="#ADD8E6", highlightthickness=1, highlightbackground="black")
            blue_sqr.grid(row=j, column=7)
            blue_sqr.create_text(20, 20, text="B" + str(j), font=('Helvetica 15'))
    if i == 21:
        for j in range(8, 14):
            x -= 1
            pink_sqr = Canvas(root, width=40, height=40, bg="#FFC0CB", highlightthickness=1, highlightbackground="black")
            pink_sqr.grid(row=7, column=j)
            pink_sqr.create_text(20, 20, text="C" + str(x), font=('Helvetica 15'))
    if i == 35:
        for j in range(8, 14):
            x -= 1
            green_sqr = Canvas(root, width=40, height=40, bg="#90ee90", highlightthickness=1, highlightbackground="black")
            green_sqr.grid(row=j, column=7)
            green_sqr.create_text(20, 20, text="D" + str(x), font=('Helvetica 15'))
    if i == 49:
        for j in range(1, 7):
            pink_sqr = Canvas(root, width=40, height=40, bg="#FFD580", highlightthickness=1, highlightbackground="black")
            pink_sqr.grid(row=7, column=j)
            pink_sqr.create_text(20, 20, text="A" + str(j), font=('Helvetica 15'))

# Ending square
end_sqr = Canvas(root, width=40, height=40, bg="white", highlightthickness=1, highlightbackground="black")
end_sqr.grid(row=7, column=7)
end_sqr.create_text(20, 20, text="E", font=('Helvetica 15'))

# "A" Home and Ready squares
a_h_sqr = Canvas(root, width=81, height=81, bg="#FFD580", highlightthickness=1, highlightbackground="black")
a_h_sqr.grid(row=1, column=1, rowspan=2, columnspan=2)
a_h_sqr.create_text(40, 40, text="Ready", font=('Helvetica 12'))

a_r_sqr = Canvas(root, width=81, height=81, highlightthickness=1, highlightbackground="black")
a_r_sqr.grid(row=3, column=3, rowspan=2, columnspan=2)
a_r_sqr.create_text(40, 20, text="A", fill="orange", font=('Helvetica 15 bold'))
a_r_sqr.create_text(40, 40, text="Home", font=('Helvetica 12'))

# "B" Home and Ready squares
a_h_sqr = Canvas(root, width=82, height=82, bg="#ADD8E6", highlightthickness=1, highlightbackground="black")
a_h_sqr.grid(row=1, column=12, rowspan=2, columnspan=2)
a_h_sqr.create_text(40, 40, text="Ready", font=('Helvetica 12'))

a_r_sqr = Canvas(root, width=81, height=81, highlightthickness=1, highlightbackground="black")
a_r_sqr.grid(row=3, column=10, rowspan=2, columnspan=2)
a_r_sqr.create_text(40, 20, text="B", fill="blue", font=('Helvetica 15 bold'))
a_r_sqr.create_text(40, 40, text="Home", font=('Helvetica 12'))

# "C" Home and Ready squares
a_h_sqr = Canvas(root, width=82, height=82, bg="#FFC0CB", highlightthickness=1, highlightbackground="black")
a_h_sqr.grid(row=12, column=12, rowspan=2, columnspan=2)
a_h_sqr.create_text(40, 40, text="Ready", font=('Helvetica 12'))

a_r_sqr = Canvas(root, width=81, height=81, highlightthickness=1, highlightbackground="black")
a_r_sqr.grid(row=10, column=10, rowspan=2, columnspan=2)
a_r_sqr.create_text(40, 20, text="C", fill="pink", font=('Helvetica 15 bold'))
a_r_sqr.create_text(40, 40, text="Home", font=('Helvetica 12'))

# "D" Home and Ready squares
a_h_sqr = Canvas(root, width=82, height=82, bg="#90ee90", highlightthickness=1, highlightbackground="black")
a_h_sqr.grid(row=12, column=1, rowspan=2, columnspan=2)
a_h_sqr.create_text(40, 40, text="Ready", font=('Helvetica 12'))

a_r_sqr = Canvas(root, width=81, height=81, highlightthickness=1, highlightbackground="black")
a_r_sqr.grid(row=10, column=3, rowspan=2, columnspan=2)
a_r_sqr.create_text(40, 20, text="D", fill="green", font=('Helvetica 15 bold'))
a_r_sqr.create_text(40, 40, text="Home", font=('Helvetica 12'))

# Second Window
window2 = Toplevel(root)
window2.wm_transient(root)
window2.title("Who is ready for Ludo!!!")
window2.geometry("300x300")
# User entry field for number of players
e = Entry(window2, width=10)
e.grid(row=0, column=0)
num = None

def number_of_players():
    game.set_players((int(e.get())))
    global apq
    global ap
    global aq
    global bpq
    global bp
    global bq
    if len(game.get_players_obj()) == 2:
        apq = Label(root, text="PQ", bg="orange")
        ap = Label(root, text="P", bg="orange")
        ap.grid(row=4, column=3)
        aq = Label(text="Q", bg="orange")
        aq.grid(row=4, column=4)
        bpq = Label(text="PQ", bg="blue")
        bp = Label(text="P", bg="blue")
        bp.grid(row=4, column=10)
        bq = Label(text="Q", bg="blue")
        bq.grid(row=4, column=11)
    if len(game.get_players_obj()) == 3:
        Label(text="P", bg="orange").grid(row=4, column=3)
        Label(text="Q", bg="orange").grid(row=4, column=4)
        Label(text="P", bg="blue").grid(row=4, column=10)
        Label(text="Q", bg="blue").grid(row=4, column=11)
        Label(text="P", bg="green").grid(row=11, column=3)
        Label(text="Q", bg="green").grid(row=11, column=4)
    window2.destroy()

number_of_players_button = Button(window2, text="Please enter number of players", command=number_of_players)
number_of_players_button.grid(row=1, column=0)

# Dice

dice_button = Button(root, text="Roll")
dice_button.grid(row=8, column=15)

list1 = ["\u2680", "\u2681", "\u2682", "\u2683", "\u2684", "\u2685"]

rolls = []
rounds = []

def dice_click():
    rand = random.choice(list1)

    dice = Label(root, text=rand, font='Helvetica 50')
    dice.grid(row=6, column=15, rowspan=2, columnspan=2)

    if rand == "\u2680":
        rolls.append(1)
    elif rand == "\u2681":
        rolls.append(2)
    elif rand == "\u2682":
        rolls.append(3)
    elif rand == "\u2683":
        rolls.append(4)
    elif rand == "\u2684":
        rolls.append(5)
    elif rand == "\u2685":
        rolls.append(6)

    if len(game.get_players_obj()) == 2:
        if len(rounds) == 0:
            rounds.append(tuple(['A', rolls[-1]]))
        elif rounds[-1][1] == 6 and rounds[-1][0] == 'A':
            rounds.append(tuple(['A', rolls[-1]]))
        elif rounds[-1][1] == 6 and rounds[-1][0] == 'B':
            rounds.append(tuple(['B', rolls[-1]]))
        elif rounds[-1][0] == 'B':
            rounds.append(tuple(['A', rolls[-1]]))
        elif rounds[-1][0] == 'A':
            rounds.append(tuple(['B', rolls[-1]]))

        game_on = game.play_game(rounds[-1])

        # If AP and AQ tokens are the same
        if game_on[0] == game_on[1] and game_on[0] != "H" and game_on[0] != "R":
            if game_on[0] == "A1" or game_on[0] == "A2" or game_on[0] == "A3" or game_on[0] == "A4" or game_on[0] == "A5" or game_on[0] == "A6":
                apq.grid_forget()
                ap.grid_forget()
                aq.grid_forget()
                apq.grid(row=7, column=int(game_on[0][1]))
            elif game_on[0] == "E":
                apq.grid_forget()
                ap.grid_forget()
                aq.grid_forget()
                dice_button.grid_forget()
                dice.grid_forget()
                apq.grid(row=7, column=7)
                win1 = Label(root, text="Orange Wins!!", font='Helvetica 20', fg="orange")
                win1.grid(row=6, column=1, columnspan=6)
                win2 = Label(root, text="Orange Wins!!", font='Helvetica 20', fg="orange")
                win2.grid(row=6, column=8, columnspan=6)
                win3 = Label(root, text="Orange Wins!!", font='Helvetica 20', fg="orange")
                win3.grid(row=8, column=1, columnspan=6)
                win4 = Label(root, text="Orange Wins!!", font='Helvetica 20', fg="orange")
                win4.grid(row=8, column=8, columnspan=6)
            elif 1 <= int(game_on[0]) <= 15:
                apq.grid_forget()
                ap.grid_forget()
                aq.grid_forget()
                apq.grid(row=0, column=int(game_on[0]) - 1)
            elif 16 <= int(game_on[0]) <= 29:
                apq.grid_forget()
                ap.grid_forget()
                aq.grid_forget()
                apq.grid(row=int(game_on[0]) - 15, column=14)
            elif 30 <= int(game_on[0]) <= 43:
                apq.grid_forget()
                ap.grid_forget()
                aq.grid_forget()
                apq.grid(row=14, column=43 - int(game_on[0]))
            elif 44 <= int(game_on[0]) <= 50:
                ap.place_forget()
                aq.place_forget()
                apq.grid(row=57 - int(game_on[0]), column=0)

        else:
            # If tokens are separate
            # AP
            if game_on[0] == "H":
                ap.grid_forget()
                apq.grid_forget()
                ap.grid(row=4, column=3)
            elif game_on[0] == "R":
                ap.grid_forget()
                apq.grid_forget()
                ap.grid(row=2, column=1)
            elif game_on[0] == "A1" or game_on[0] == "A2" or game_on[0] == "A3" or game_on[0] == "A4" or game_on[0] == "A5" or game_on[0] == "A6":
                ap.grid_forget()
                apq.grid_forget()
                ap .grid(row=7, column=int(game_on[0][1]))
            elif game_on[0] == "E":
                ap.grid_forget()
                apq.grid_forget()
                ap.grid(row=7, column=7)
            elif 1 <= int(game_on[0]) <= 15:
                ap.grid_forget()
                apq.grid_forget()
                ap.grid(row=0, column=int(game_on[0])-1)
            elif 16 <= int(game_on[0]) <= 29:
                ap.grid_forget()
                apq.grid_forget()
                ap.grid(row=int(game_on[0])-15, column=14)
            elif 30 <= int(game_on[0]) <= 43:
                ap.grid_forget()
                apq.grid_forget()
                ap.grid(row=14, column=43-int(game_on[0]))
            elif 44 <= int(game_on[0]) <= 50:
                ap.grid_forget()
                apq.grid_forget()
                ap.grid(row=57-int(game_on[0]), column=0)

            # AQ
            if game_on[1] == "H":
                aq.grid_forget()
                aq.grid(row=4, column=4)
            elif game_on[1] == "R":
                aq.grid_forget()
                aq.grid(row=2, column=2)
            elif game_on[1] == "A1" or game_on[1] == "A2" or game_on[1] == "A3" or game_on[1] == "A4" or game_on[1] == "A5" or game_on[1] == "A6":
                aq.grid_forget()
                aq.grid(row=7, column=int(game_on[1][1]))
            elif game_on[1] == "E":
                aq.grid_forget()
                aq.grid(row=7, column=7)
            elif 1 <= int(game_on[1]) <= 15:
                aq.grid_forget()
                aq.grid(row=0, column=int(game_on[1])-1)
            elif 16 <= int(game_on[1]) <= 29:
                aq.grid_forget()
                aq.grid(row=int(game_on[1])-15, column=14)
            elif 30 <= int(game_on[1]) <= 43:
                aq.grid_forget()
                aq.grid(row=14, column=43-int(game_on[1]))
            elif 44 <= int(game_on[1]) <= 50:
                aq.grid_forget()
                aq.grid(row=57-int(game_on[1]), column=0)

        # If BP and BQ are together
        if game_on[2] == game_on[3] and game_on[2] != "H" and game_on[2] != "R":
            if game_on[2] == "B1" or game_on[2] == "B2" or game_on[2] == "B3" or game_on[2] == "B4" or game_on[2] == "B5" or game_on[2] == "B6":
                bpq.grid_forget()
                bp.grid_forget()
                bq.grid_forget()
                bpq.grid(row=int(game_on[2][1]), column=7)
            elif game_on[2] == "E":
                bpq.grid_forget()
                bp.grid_forget()
                bq.grid_forget()
                dice_button.grid_forget()
                dice.grid_forget()
                bpq.grid(row=7, column=7)
                win1 = Label(root, text="Blue Wins!!", font='Helvetica 20', fg="blue")
                win1.grid(row=6, column=1, columnspan=6)
                win2 = Label(root, text="Blue Wins!!", font='Helvetica 20', fg="blue")
                win2.grid(row=6, column=8, columnspan=6)
                win3 = Label(root, text="Blue Wins!!", font='Helvetica 20', fg="blue")
                win3.grid(row=8, column=1, columnspan=6)
                win4 = Label(root, text="Blue Wins!!", font='Helvetica 20', fg="blue")
                win4.grid(row=8, column=8, columnspan=6)
            elif 1 <= int(game_on[2]) <= 8:
                bpq.grid_forget()
                bp.grid_forget()
                bq.grid_forget()
                bpq.grid(row=0, column=int(game_on[2]) - 1)
            elif 15 <= int(game_on[2]) <= 29:
                bpq.grid_forget()
                bp.grid_forget()
                bq.grid_forget()
                bpq.grid(row=int(game_on[2]) - 15, column=14)
            elif 30 <= int(game_on[2]) <= 43:
                bpq.grid_forget()
                bp.grid_forget()
                bq.grid_forget()
                bpq.grid(row=14, column=43 - int(game_on[2]))
            elif 44 <= int(game_on[2]) <= 57:
                bpq.grid_forget()
                bp.grid_forget()
                bq.grid_forget()
                bpq.grid(row=57 - int(game_on[2]), column=0)

        else:
            # If B tokes are separate
            # BP
            if game_on[2] == "H":
                bp.grid_forget()
                bpq.grid_forget()
                bp.grid(row=4, column=10)
            elif game_on[2] == "R":
                bp.grid_forget()
                bpq.grid_forget()
                bp.grid(row=2, column=12)
            elif game_on[2] == "B1" or game_on[2] == "B2" or game_on[2] == "B3" or game_on[2] == "B4" or game_on[2] == "B5" or game_on[2] == "B6":
                bp.grid_forget()
                bpq.grid_forget()
                bp.grid(row=int(game_on[2][1]), column=7)
            elif game_on[2] == "E":
                bp.grid_forget()
                bpq.grid_forget()
                bp.grid(row=7, column=7)
            elif 1 <= int(game_on[2]) <= 8:
                bp.grid_forget()
                bpq.grid_forget()
                bp.grid(row=0, column=int(game_on[2])-1)
            elif 15 <= int(game_on[2]) <= 29:
                bp.grid_forget()
                bpq.grid_forget()
                bp.grid(row=int(game_on[2])-15, column=14)
            elif 30 <= int(game_on[2]) <= 43:
                bp.grid_forget()
                bpq.grid_forget()
                bp .grid(row=14, column=43-int(game_on[2]))
            elif 44 <= int(game_on[2]) <= 57:
                bp.grid_forget()
                bpq.grid_forget()
                bp.grid(row=57-int(game_on[2]), column=0)

            #BQ
            if game_on[3] == "H":
                bq.grid_forget()
                bq.grid(row=4, column=11)
            elif game_on[3] == "R":
                bq.grid_forget()
                bq.grid(row=2, column=13)
            elif game_on[3] == "B1" or game_on[3] == "B2" or game_on[3] == "B3" or game_on[3] == "B4" or game_on[3] == "B5" or game_on[3] == "B6":
                bq.grid_forget()
                bq.grid(row=int(game_on[3][1]), column=7)
            elif game_on[3] == "E":
                bq.grid_forget()
                bq.grid(row=7, column=7)
            elif 1 <= int(game_on[3]) <= 8:
                bq.grid_forget()
                bq.grid(row=0, column=int(game_on[3])-1)
            elif 15 <= int(game_on[3]) <= 29:
                bq.grid_forget()
                bq.grid(row=int(game_on[3])-15, column=14)
            elif 30 <= int(game_on[3]) <= 43:
                bq.grid_forget()
                bq.grid(row=14, column=43-int(game_on[3]))
            elif 44 <= int(game_on[3]) <= 57:
                bq.grid_forget()
                bq.grid(row=57-int(game_on[3]), column=0)

        print(rounds)
        print(game_on)

    elif len(game.get_players_obj()) == 3:
        if len(rounds) == 0:
            rounds.append(tuple(['A', rolls[-1]]))
        elif rounds[-1][1] == 6 and rounds[-1][0] == 'A':
            rounds.append(tuple(['A', rolls[-1]]))
        elif rounds[-1][1] == 6 and rounds[-1][0] == 'B':
            rounds.append(tuple(['B', rolls[-1]]))
        elif rounds[-1][1] == 6 and rounds[-1][0] == 'C':
            rounds.append(tuple(['C', rolls[-1]]))
        elif rounds[-1][0] == 'A':
            rounds.append(tuple(['B', rolls[-1]]))
        elif rounds[-1][0] == 'B':
            rounds.append(tuple(['C', rolls[-1]]))
        elif rounds[-1][0] == 'C':
            rounds.append(tuple(['A', rolls[-1]]))

        print(rounds)
        print(game.play_game(rounds[-1]))
    else:
        print('Not working')

dice_button.config(command=dice_click)

root.mainloop()





