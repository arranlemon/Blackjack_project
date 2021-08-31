
import random

deck = [["2H",2], ["3H",3], ["4H",4], ["5H",5], ["6H",6], ["7H",7], ["8H",8], ["9H",9], ["10H",10], ["JH",10], ["QH",10], ["KH",10], ["AH",11,1], ["2S",2], ["3S",3], ["4S",4], ["5S",5], ["6S",6], ["7S",7], ["8S",8], ["9S",9], ["10S",10], ["JS",10], ["QS",10], ["KS",10], ["AS",11,1], ["2D",2], ["3D",3], ["4D",4], ["5D",5], ["6D",6], ["7D",7], ["8D",8], ["9D",9], ["10D",10], ["JD",10], ["QD",10], ["KD",10], ["AD",11,1], ["2C",2], ["3C",3], ["4C",4], ["5C",5], ["6C",6], ["7C",7], ["8C",8], ["9C",9], ["10C",10], ["JC",10], ["QC",10], ["KC",10], ["AC",11,1]]

class Hand:
    
    def __init__(self, cards, money_bet = 0):
        self.cards = cards
        self.hand_values = []
        self.money_bet = money_bet
        self.money_made = 0
        self.best_hand_value = 0

    def get_value(self):
        values = [0]
        for card in self.cards:
            card_values = card[1:]
            print(card_values)
            for index in range(0,len(values)):
                values[index] += card_values[0]
                if len(card_values) > 1:
                    values.append(values[index] + card_values[1])
        print(values)
        return values            


def get_best_value(values):
        best_value = 0
        for index in range(0,len(values)):
            if index == 0 and values[index] > 21:
                best_value = values[index]
                break
            elif values[index] > best_value and values[index] <=21:
                best_value = values[index]
        return best_value

def get_cards():
        card1 = deck.pop(random.randint(0,len(deck)))
        card2 = deck.pop(random.randint(0,len(deck)))
        return [card1,card2]

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
                            self.currenthands = Hand(get_cards(), money_bet)
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

        print("Works till now I think")
        return 




        
                



        


    


    
        
test_player = Player("zestyboy", 100)
test_player.play_hand()        
# test_hand = Hand([["JH",10], ["AD",1,11], ["AS",1,11]])
# test_values = test_hand.get_value()
# print(test_values)
# print(get_best_value(test_values))



    

    

    # win_multipliers = {"Win":2, "Push": 1, "Blackjack!": 2.5, "Bust": 0}

# class Dealer:

    
#     


#     def __init__(self, num_decks):
#         self.hand = []
#         self.deck = deck*num_decks


