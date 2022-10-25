import random


class Card:
    def __init__(self):
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
        self.checker = 0
        self.points = 0

    def deal_cards(self):
        self.deal = self.card + self.add_card

    def reset(self):
        self.deal = 0

    def show_cards(self):
        print("Your card total is: " + str(self.deal))
        self.check_blackjack()

    def update_deal(self):
        Card.draw_card(self)
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
        elif self.deal < 21:
            z = input("Would you like to draw another card? [y/n]")
            self.check_cards(z)

    def check_cards(self, x):
        if x == "y":
            self.update_deal()
            self.show_cards()
        else:
            self.check_points()

    def play_again(self, x):
        if x == "y":
            Director.start_game(self)
        else:
            print("Thanks for playing...")
            exit()

    def check_points(self):
        self.checker = 21 - self.deal
        if self.checker < 4:
            self.points = self.checker * 100
        if self.checker < 10 and self.checker > 3:
            self.points = self.checker * 5
        self.show_points()

    def show_points(self):
        print("You finished with " + str(self.points) + " points!")
        print("The highest you can finish with is 1000 points when you hit 21!")
        i = input("Would you like to play again? [y/n]")
        self.play_again(i)


class Director(Dealer):

    def start_game(self):
        self.welcome()
        self.reset()
        self.deal_cards()
        self.show_cards()

        self.check_blackjack()

    def welcome(self):
        print("Welcome to BlackJack!")


x = Director()
x.start_game()
