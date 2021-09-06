
import random

deck = [["2H",2], ["3H",3], ["4H",4], ["5H",5], ["6H",6], ["7H",7], ["8H",8], ["9H",9], ["10H",10], ["JH",10], ["QH",10], ["KH",10], ["AH",1,11], ["2S",2], ["3S",3], ["4S",4], ["5S",5], ["6S",6], ["7S",7], ["8S",8], ["9S",9], ["10S",10], ["JS",10], ["QS",10], ["KS",10], ["AS",1,11], ["2D",2], ["3D",3], ["4D",4], ["5D",5], ["6D",6], ["7D",7], ["8D",8], ["9D",9], ["10D",10], ["JD",10], ["QD",10], ["KD",10], ["AD",1,11], ["2C",2], ["3C",3], ["4C",4], ["5C",5], ["6C",6], ["7C",7], ["8C",8], ["9C",9], ["10C",10], ["JC",10], ["QC",10], ["KC",10], ["AC",1,11]]


class Hand:
    
    def __init__(self, cards, money_bet = 0):
        self.cards = cards
        self.hand_values = [0]
        self.money_bet = money_bet
        self.money_made = 0
        self.best_hand_value = 0

    def __repr__(self):
        cards = ""
        for card in self.cards:
            cards += card[0] + " "
        self.get_value()
        best_current_value = self.get_best_value()
        return "Your cards:\n" + cards + "\nbest current value: " + str(self.best_hand_value)

    def get_value(self):
        values = [0]
        for card in self.cards:
            card_values = card[1:]
            for index in range(0,len(values)):
                values[index] += card_values[0]
                if len(card_values) > 1:
                    values.append(values[index]-1 + card_values[1])
        sorted_values = sorted(values)
        self.hand_values = sorted_values
        return            


    def get_best_value(self):
            for index in range(0,len(self.hand_values)):
                if index == 0 and self.hand_values[index] > 21:
                    self.best_hand_value = self.hand_values[index]
                    break
                elif self.hand_values[index] > self.best_hand_value and self.hand_values[index] <=21:
                    self.best_hand_value = self.hand_values[index]
            return

    def hit(self):
        confirmed = False
        while confirmed == False:
            confirmation_decision = input("Confirming that you would like to hit with this hand of current value {}?(y/n)\n".format(self.best_hand_value)).lower().strip()
            if confirmation_decision == "y":
                confirmed = True
            elif confirmation_decision == "n":
                print("What would you like to do with this hand?")
                return
            else:
                print("Please enter y or n.")
        self.cards.append(get_single_card(deck))
        print(self)
        if self.is_bust():
            print("Bust.")
        return 


    def sit(self):
        confirmed = False
        while confirmed == False:
            confirmation_decision = input("Confirming that you would like to sit with this hand of current value {}?(y/n)\n".format(self.best_hand_value)).lower().strip()
            if confirmation_decision == "y":
                confirmed = True
            elif confirmation_decision == "n":
                print("What would you like to do with this hand?")
                return
            else:
                print("Please enter y or n.")
        return

    def is_bust(self):
        if self.best_hand_value > 21:
            return True
        return False

    def play_hand(self):
        #test for blackjack and then for split option
        print(self)
        if self.best_hand_value == 21:
            print("Blackjack!")
            return
        # if self.cards[0][1:] == self.cards[1][1:]:
            #implement split stuff here
        while self.is_bust() == False:
            action = input("Would you like to hit or sit?(hit/sit)\n").lower().strip()
            if action == "hit":
                self.hit()
                continue
            elif action == "sit":
                self.sit()
                print("You sat with the following hand:")
                print(self)
                return
            else:
                print("Please enter hit or sit.")
        return


def get_first_cards(deck):
        card1 = deck.pop(random.randint(0,len(deck)))
        card2 = deck.pop(random.randint(0,len(deck)))
        return [card1,card2]

def get_single_card(deck):
    card = deck.pop(random.randint(0,len(deck)))
    return card

def reset_deck(deck):
    deck = [["2H",2], ["3H",3], ["4H",4], ["5H",5], ["6H",6], ["7H",7], ["8H",8], ["9H",9], ["10H",10], ["JH",10], ["QH",10], ["KH",10], ["AH",1,11], ["2S",2], ["3S",3], ["4S",4], ["5S",5], ["6S",6], ["7S",7], ["8S",8], ["9S",9], ["10S",10], ["JS",10], ["QS",10], ["KS",10], ["AS",1,11], ["2D",2], ["3D",3], ["4D",4], ["5D",5], ["6D",6], ["7D",7], ["8D",8], ["9D",9], ["10D",10], ["JD",10], ["QD",10], ["KD",10], ["AD",1,11], ["2C",2], ["3C",3], ["4C",4], ["5C",5], ["6C",6], ["7C",7], ["8C",8], ["9C",9], ["10C",10], ["JC",10], ["QC",10], ["KC",10], ["AC",1,11]]
    return
    


class Player:
    
    
    def __init__(self, name, chips = 100):
        self.name = name
        self.currenthands = []
        self.chips = chips
        self.hand_history = []
        self.hand_value = -1

    def play_hand(self):
    
        money_bet = 0
        playing_hand = False
        while playing_hand == False:
            play_hand = input("Would {} like to play this hand? (y/n):".format(self.name).lower().strip())
            if play_hand == "n":
                print("{} sits this hand out.".format(self.name))
                return
            elif play_hand == "y":
                playing_hand = True
                money_confirmed = False
                bet_confirmed = False
                while money_confirmed == False and bet_confirmed == False:
                    try:
                        money_bet = int(input("How much would you like to bet on this hand?"))
                        if money_bet <= self.chips:
                            money_confirmed = True
                            bet_confirmed = False
                        else:
                            print("You only have {} chips available. Please enter a valid betting amount.".format(self.chips))
                            continue
                    except TypeError:
                        print("Please enter an integer number you would like to bet.")
                        continue
                    while bet_confirmed == False:
                        bet_confirmation = input("You want to bet {} chips on this hand?(y/n)".format(money_bet)).lower().strip()
                        if bet_confirmation == "y":
                            self.currenthands = Hand(get_first_cards(), money_bet)
                            money_confirmed = True
                            bet_confirmed = True
                        elif bet_confirmation == "n":
                            print("Please enter the value you intended.")
                            money_confirmed = False
                            bet_confirmed = False
                            break
                        else:
                            print("Please enter y or n.")
                            continue
            else:
                print("Please enter y or n.")
        #now we actually play the hand
        for hand in self.currenthands:
            hand.play_hand()
        self.get_value()
        self.get_best_value()
        
        actions = ["hit", "sit", "bust", "blackjack!"]
        action = 0
    
reset_deck(deck)      
test_hand = Hand(get_first_cards(deck),100)
test_hand.play_hand()







    

    

    # win_multipliers = {"Win":2, "Push": 1, "Blackjack!": 2.5, "Bust": 0}

# class Dealer:

    
#     


#     def __init__(self, num_decks):
#         self.hand = []
#         self.deck = deck*num_decks


