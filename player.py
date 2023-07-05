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
