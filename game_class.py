import os
import random
import time


class Game:
    motions = ["rock", "paper", "scissors"]

    def start_round(self):
        return self.evaluate_round(self.player_turn(), self.computer_turn())

    def evaluate_round(self, user_move, computer_move):
        round_picks = f"You picked {user_move}, and computer picked {computer_move}"

        draw_msg = "It's a draw!"
        winner_msg = "You won this round!"
        loser_msg = "You lost this round!"

        if (user_move == "rock") and (computer_move == "scissors"):
            print(round_picks)
            print(winner_msg)
        elif (user_move == "scissors") and (computer_move == "paper"):
            print(round_picks)
            print(winner_msg)
        elif (user_move == "paper") and (computer_move == "rock"):
            print(round_picks)
            print(winner_msg)
        elif user_move == computer_move:
            print(draw_msg)
        else:
            print(round_picks)
            print(loser_msg)

        time.sleep(2)
        os.system("clear")

        self.run_game("Would you like to play again? Yes or No\n")

    def computer_turn(self):
        computer_choice = random.randint(0, 2)
        return self.motions[computer_choice]

    def player_turn(self):
        print("Pick one of the following options: \n\t0: Rock\n\t1: Paper\n\t2: Scissors")
        try:
            player_input = input("What's your move?\n")
            return self.motions[int(player_input)]
        except (IndexError, ValueError):
            print("\nInvalid input, please try again")
            return self.player_turn()

    def game_option(self, game_input):
        match game_input.lower():
            case "yes":
                print("You decided to start the game!")
                self.start_round()
            case "no":
                print("You decided to quit the game!")
                return
            case _:
                self.run_game()

    def run_game(self, msg="Are you ready to play \"Rock, Paper, Scissors\"? Yes or No\n"):
        """Run the game of Rock-Paper-Scissors"""
        game_input = input(msg).strip()

        self.game_option(game_input)


if __name__ == "__main__":
    game = Game()
    game.run_game()
