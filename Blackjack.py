
class Hand:
    win_multipliers = {"Win":2, "Push": 1, "Blackjack!": 2.5, "Bust": 0}
    
    def __init__(self, cards, money_bet = 0):
        self.cards = cards
        self.money_bet = money_bet
        self.money_made = 0

    def get_value(self):
        best_current_value = 0
        values = [best_current_value]
        print(self.cards)
        for card in self.cards:
            card_values = card[1:]
            print(card_values)
            for index in range(0,len(values)):
                if len(card_values) > 1:
                    values.append(values[index] + card_values[1])
                values[index] += card_values[0]
        return values            
        

        
        
test_hand = Hand([["AH",1,11],["6S",6], ["AD",1,11]])
print(test_hand.get_value())


    

    



# class Dealer:

#     deck = [["2H",2], ["3H",3], ["4H",4], ["5H",5], ["6H",6], ["7H",7], ["8H",8], ["9H",9], ["10H",10], ["JH",10], ["QH",10], ["KH",10], ["AH",11,1], ["2S",2], ["3S",3], ["4S",4], ["5S",5], ["6S",6], ["7S",7], ["8S",8], ["9S",9], ["10S",10], ["JS",10], ["QS",10], ["KS",10], ["AS",11,1], ["2D",2], ["3D",3], ["4D",4], ["5D",5], ["6D",6], ["7D",7], ["8D",8], ["9D",9], ["10D",10], ["JD",10], ["QD",10], ["KD",10], ["AD",11,1], ["2C",2], ["3C",3], ["4C",4], ["5C",5], ["6C",6], ["7C",7], ["8C",8], ["9C",9], ["10C",10], ["JC",10], ["QC",10], ["KC",10], ["AC",11,1]]
    
#     


#     def __init__(self, num_decks):
#         self.hand = []
#         self.deck = deck*num_decks

# class Player:
    
#         def __init__(self, name, chips = 500):
#             self.name = name
#             self.currenhand = []
#             self.chips = chips
#             self.hand_history = []
#             self.hand_value = -1



