class Dealer:

    deck = [["2H",2], ["3H",3], ["4H",4], ["5H",5, ["6H",6], ["7H",7], ["8H",8], ["9H",9], ["10H",10], ["JH",10], ["QH",10], ["KH",10], ["AH",1,11], ["2S",2], ["3S",3], ["4S",4], ["5S",5, ["6S",6], ["7S",7], ["8S",8], ["9S",9], ["10S",10], ["JS",10], ["QS",10], ["KS",10], ["AS",1,11], ["2D",2], ["3D",3], ["4D",4], ["5D",5, ["6D",6], ["7D",7], ["8D",8], ["9D",9], ["10D",10], ["JD",10], ["QD",10], ["KD",10], ["AD",1,11], ["2C",2], ["3C",3], ["4C",4], ["5C",5, ["6C",6], ["7C",7], ["8C",8], ["9C",9], ["10C",10], ["JC",10], ["QC",10], ["KC",10], ["AC",1,11],
    win_multipliers = {"Win":1.5, "Draw": 0, "Blackjack!": 2}


    def __init__(self, hand, num_decks):
        self.hand = hand
        self.deck = deck*num_decks

class Player:
    
        def __init__(self, hand, chips):
            self.hand = hand
            self.chips = chips
            self.hand_history = []



