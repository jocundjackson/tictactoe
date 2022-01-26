import re
# Jackson de Oliveira
# AA502 TicTacToe


class TicTacToe:
    def __init__(self):
        self.players = [[0, 0, 0, 0, 0, 0, 0, 0, 0],
                        [0, 0, 0, 0, 0, 0, 0, 0, 0]]
        self.__initialize_board()

    def run_game(self):
        while self.__check_for_win() is False:
            self.__print_board()
            self.__handle_turn()

    def __read_user_input(self, player_index):
        if player_index == 0:
            player = "player 1 ( X )"
        else:
            player = "player 2 ( O )"
        print("")
        print("You are", player)
        input_value = input("Choose a position: ")
        print("")
        test_value = re.compile("^[abcABC][123]$")
        if test_value.match(input_value):
            return input_value.upper()
        print("Position Invalid...")
        return self.__read_user_input(player_index)

    def __handle_turn(self):
        player_index = self.__find_current_turn()
        move_location = self.__read_user_input(player_index)
        move_location = self.__convert_move_location(move_location)
        moves_taken = [el1 + el2 for el1, el2 in zip(self.players[0], self.players[1])]
        if moves_taken[move_location] == 0:
            self.players[player_index][move_location] = 1
        else:
            print("Space already taken!")

    @staticmethod
    def __convert_move_location(move_location):
        final_move_location = int(move_location[1])
        if move_location[0] == "B":
            final_move_location += 3
        elif move_location[0] == "C":
            final_move_location += 6
        final_move_location -= 1  # fix off by one error
        return final_move_location

    def __find_current_turn(self):
        player_1 = sum(self.players[0])
        player_2 = sum(self.players[1])
        if player_2 < player_1:
            return 1
        return 0

    @staticmethod
    def __initialize_board():
        print("\r\n\r\nShall we play a game?\r\n\r\n")

    @staticmethod
    def __handle_end_game(player_index=None):
        if player_index is None:
            print("##############")
            print("###TIE GAME###")
            print("##############")
            return False
        if player_index == 0:
            player = "player 1 ( X )"
        else:
            player = "player 2 ( O )"
        print("#############################")
        print(player, "has won!")
        print("#############################")

    def __check_for_win(self):
        moves_taken = sum([el1 + el2 for el1, el2 in zip(self.players[0], self.players[1])])
        if moves_taken < 5:
            return False
        for player_index, player in enumerate(self.players):
            if ((player[0] & player[1] & player[2]) |
                    (player[3] & player[4] & player[5]) |
                    (player[6] & player[7] & player[8]) |
                    (player[0] & player[3] & player[6]) |
                    (player[1] & player[4] & player[7]) |
                    (player[2] & player[5] & player[8]) |
                    (player[0] & player[4] & player[8]) |
                    (player[2] & player[4] & player[6])):
                self.__handle_end_game(player_index)
                return True
        if moves_taken == 9:
            self.__handle_end_game()
            return True
        return False

    def __print_board(self):
        output_string = ""
        for i in range(9):
            if self.players[0][i] == 1:
                output_string += " X "
            elif self.players[1][i] == 1:
                output_string += " O "
            else:
                output_string += " _ "
            if (i+1) % 3 == 0:
                output_string += "\r\n"
            else:
                output_string += "|"
        print(output_string)


tic_tac_toe = TicTacToe()
tic_tac_toe.run_game()
