from tkinter import *
import random

class Card:
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit

class GameInterface:
    def __init__(self, root):
        self.root = root
        self.cards = []
        self.hand = []
        self.total_points = 0

        self.start_button = Button(self.root, text="Начать игру", command=self.start_game)
        self.start_button.pack()

        self.take_card_button = Button(self.root, text="Взять карту", command=self.take_card, state=DISABLED)
        self.take_card_button.pack()

        self.label_list = Label(self.root, text="Список карт:")
        self.label_list.pack()

        self.cards_listbox = Listbox(self.root, width=20)
        self.cards_listbox.pack()

        self.points_label = Label(self.root, text="Сумма очков: 0")
        self.points_label.pack()

        self.reset_button = Button(self.root, text="Сбросить руку", command=self.reset_hand, state=DISABLED)
        self.reset_button.pack()

    def start_game(self):
        self.cards = self.create_deck()
        random.shuffle(self.cards)
        self.update_hand()
        
        self.start_button["state"] = DISABLED
        self.take_card_button["state"] = NORMAL
        self.reset_button["state"] = NORMAL

    def create_deck(self):
        ranks = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]
        suits = ["♠", "♣", "♥", "♦"]
        deck = []

        for suit in suits:
            for rank in ranks:
                deck.append(Card(rank, suit))

        return deck

    def take_card(self):
        card = self.cards.pop()
        self.hand.append(card)
        self.update_hand()

    def update_hand(self):
        self.cards_listbox.delete(0, END)

        for card in self.hand:
            self.cards_listbox.insert(END, card.rank + card.suit)

        self.total_points = self.calculate_points()
        self.points_label["text"] = f"Сумма очков: {self.total_points}"

        if not self.cards:
            self.take_card_button["state"] = DISABLED

    def calculate_points(self):
        points = 0
        aces_count = 0

        for card in self.hand:
            if card.rank in ["J", "Q", "K"]:
                points += 10
            elif card.rank == "A":
                points += 11
                aces_count += 1
            else:
                points += int(card.rank)

        while points > 21 and aces_count > 0:
            points -= 10
            aces_count -= 1

        return points

    def reset_hand(self):
        self.cards = []
        self.hand = []
        self.total_points = 0

        self.cards_listbox.delete(0, END)
        self.points_label["text"] = "Сумма очков: 0"
        self.start_button["state"] = NORMAL
        self.take_card_button["state"] = DISABLED
        self.reset_button["state"] = DISABLED

root = Tk()
interface = GameInterface(root)
root.mainloop()