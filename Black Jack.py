import random

class Card:
    def __init__(self,value, suit):
        self.cost=value
        self.suit= '♥♦♣♠'[suit]
        self.value= ['A','2','3','4','5','6','7','8','9','10','J','Q','K'][value-1]

    def show(self):
        print('┌───────┐')
        print(f'| {self.value:<2}    |')
        print('|       |')
        print(f'|   {self.suit}   |')
        print('|       |')
        print(f'|    {self.value:>2} |')
        print('└───────┘')
    def price(self):
        if self.cost >= 10:
            return 10
        elif self.cost==1:
            return 11
        return self.cost


class Deck:
    def __init__(self):
        self.cards = []
    def generate(self):
        for i in range(1,14):
            for j in range(4):
                self.cards.append(Card(i,j))

    def draw(self, iteration):
        cards=[]
        for i in range(iteration):
            card= random.choice(self.cards)
            self.cards.remove(card)
            cards.append(card)
        return cards
    def count(self):
        return len(self.cards)



class Player:
    def __init__(self,isDealer, deck):
        self.cards= []
        self.isDealer = isDealer
        self.deck= deck
        self.score =0
    def hit(self):
        self.cards.extend(self.deck.draw(1))
        self.check_score()
        if self.score>21:
            return 1
        return 0
    def deal(self):
        self.cards.extend(self.deck.draw(2))
        self.check_score()
        if self.score ==21:
            return 1
        return 0
    def check_score(self):
        a_counter=0
        self.score= 0
        for card in self.cards:
            if card.price()==11:
                a_counter+=1
            self.score+= card.price()
        while a_counter !=0 and self.score>21:
            a_counter-=1
            self.score-=10
        return self.score
    def show(self):
        if self.isDealer:
            print('Dealers cards')
        else:
            print("PLayers Cards")
        for i in self.cards:
            i.show()
        print("Score:"+str(self.score))

class Blackjack:
    def __init__(self):
        self.deck=Deck()
        self.deck.generate()
        self.player= Player(False,self.deck)
        self.dealer= Player(True,self.deck)
    def play(self):
        p_status= self.player.deal
        d_status = self.dealer.deal()

        self.player.show()

        if p_status == 1:
            print("Player got Blackjack! Congrats!")
            if d_status == 1:
                print("Dealer and Player got Blackjack! It's a push. (Tie)")
            return 1

        cmd = ""
        while cmd != "Stand":
            bust = 0
            cmd = input("Hit or Stand? ")

            if cmd == "Hit":
                bust = self.player.hit()
                self.player.show()
            if bust == 1:
                print("Player busted. Good Game!")
                return 1
        print("\n")
        self.dealer.show()
        if d_status == 1:
            print("Dealer got Blackjack! Better luck next time!")
            return 1

        while self.dealer.check_score() < 17:
            if self.dealer.hit() == 1:
                self.dealer.show()
                print("Dealer busted. Congrats!")
                return 1
            self.dealer.show()

        if self.dealer.check_score() == self.player.check_score():
            print("It's a Push (Tie). Better luck next time!")
        elif self.dealer.check_score() > self.player.check_score():
            print("Dealer wins. Good Game!")
        elif self.dealer.check_score() < self.player.check_score():
            print("Player wins. Congratulations!")

b = Blackjack()
b.play()
