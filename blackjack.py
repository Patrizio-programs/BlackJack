import random


class Card:
    def __init__(self) -> None:
        self.card = 0
        self.add_card = 0

    def draw_card(self):
        self.card = random.randint(1, 10)
        return self.card

    def draw_add_card(self):
        self.add_card = random.randint(1, 10)
        return self.add_card


class Dealer:
    def __init__(self):
        self.card = Card.draw_card(self)
        self.add_card = Card.draw_add_card(self)
        self.deal = 0

    def deal_cards(self):
        self.deal = self.card + self.add_card

    def show_cards(self):
        print("Your card total is: " + str(self.deal))

    def update_deal(self):
        Card.draw_card()
        self.deal = self.deal + self.card

    def check_blackjack(self):
        if self.deal == 21:
            print("You won this round! You have 1000 points")
            x = input("Would you like to play again? [y/n]")
            self.play_again(x)
        elif self.deal > 21:
            print("Oh no you lost! Better luck next time")
            i = input("Would you like to play again? [y/n]")
            self.play_again(i)

    def check_cards(self):
        pass

    def play_again(self, x):
        if x == "y":
            Director.start_game()
        else:
            print("Thanks for playing...")
            exit


class Director:

    def start_game(self):
        pass

    def welcome(self):
        pass
