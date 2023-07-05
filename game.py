from player import Player


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
