
import random

deck = [["2H",2], ["3H",3], ["4H",4], ["5H",5], ["6H",6], ["7H",7], ["8H",8], ["9H",9], ["10H",10], ["JH",10], ["QH",10], ["KH",10], ["AH",1,11], ["2S",2], ["3S",3], ["4S",4], ["5S",5], ["6S",6], ["7S",7], ["8S",8], ["9S",9], ["10S",10], ["JS",10], ["QS",10], ["KS",10], ["AS",1,11], ["2D",2], ["3D",3], ["4D",4], ["5D",5], ["6D",6], ["7D",7], ["8D",8], ["9D",9], ["10D",10], ["JD",10], ["QD",10], ["KD",10], ["AD",1,11], ["2C",2], ["3C",3], ["4C",4], ["5C",5], ["6C",6], ["7C",7], ["8C",8], ["9C",9], ["10C",10], ["JC",10], ["QC",10], ["KC",10], ["AC",1,11]]

win_multipliers = {"Lose":0, "Win": 2, "Blackjack": 2.5, "Push": 1}

min_bet = 10
max_bet = 100

def get_first_cards(deck):
        card1 = deck.pop(random.randint(0,len(deck)-1))
        card2 = deck.pop(random.randint(0,len(deck)-1))
        return [card1,card2]

def get_single_card(deck):
    card = deck.pop(random.randint(0,len(deck)-1))
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

    def get_hand_participantion(self):
    
        money_bet = 0
        playing_hand = False
        while playing_hand == False:
            play_hand = input("Would {} like to play this hand? (y/n):\n".format(self.name).lower().strip())
            if play_hand == "n":
                print("{} sits this hand out.".format(self.name))
                return
            elif play_hand == "y":
                playing_hand = True
                money_confirmed = False
                bet_confirmed = False
                while money_confirmed == False and bet_confirmed == False:
                    try:
                        money_bet = int(input("You have {} chips. How much would you like to bet on this hand?\n".format(self.chips)))
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
                        bet_confirmation = input("You want to bet {} chips on this hand?(y/n)\n".format(money_bet)).lower().strip()
                        if bet_confirmation == "y":
                            self.currenthands.append(Hand(get_first_cards(deck), money_bet))
                            print("{} was dealt the following:".format(self.name))
                            print(self.currenthands[0])
                            self.chips -= money_bet
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
        return

    def play_hands(self):
        print("{} will now play their hand:".format(self.name))
        #now we actually play the hand
        index = 0
        for hand in self.currenthands:
            if hand.is_split:
                hand.play_split_hand(self, index)
                index += 1
            else:
                hand.play_hand(self, index)
                index += 1
            if index < len(self.currenthands):
                print("Next hand:\n")
        return

    def collect_winnings(self, dealers_hand):
        if len(self.currenthands) == 0:
            print("{} did not play this hand. Their chips remain at {}".format(self.name,self.chips))
            return
        starting_chips = self.chips
        total_money_bet = 0
        total_chips_won_from_hands = 0
        dealers_hand.print_dealer_hand()
        dealer_is_blackjack = len(dealers_hand.cards) == 2 and dealers_hand.best_hand_value == 21
        for index in range(0,len(self.currenthands)):
            result = ""
            print("Hand " + str(index+1) + ":")
            print(self.currenthands[index])
            hand_is_blackjack = len(self.currenthands[index].cards) == 2 and self.currenthands[index].best_hand_value == 21
            total_money_bet += self.currenthands[index].money_bet
            if self.currenthands[index].is_bust():
                result = "Lose"
                print("You bust with value of {}. Result is a loss of {} chips to the dealer.".format(self.currenthands[index].best_hand_value, self.currenthands[index].money_bet))
                total_chips_won_from_hands -= self.currenthands[index].money_bet
            elif dealer_is_blackjack and hand_is_blackjack:
                result = "Push"
                total_chips_won_from_hands += self.currenthands[index].money_bet
                print("Both have blackjack. Result is a push. {} got their {} chips back from this hand.".format(self.name, self.currenthands[index].money_bet))
            elif dealer_is_blackjack and not hand_is_blackjack:
                result = "Lose"
                print("Dealers blackjack wins. Result is a loss. {} lost their {} chips from this hand to the dealer.".format(self.name,self.currenthands[index].money_bet))
            elif not dealer_is_blackjack and hand_is_blackjack:
                result = "Blackjack"
                print("Your Blackjack wins. {} got back their bet of {} plus an extra {}.".format(self.name, self.currenthands[index].money_bet, self.currenthands[index].money_bet*1.5))
                total_chips_won_from_hands += self.currenthands[index].money_bet*win_multipliers[result]
            elif dealers_hand.best_hand_value == self.currenthands[index].best_hand_value:
                result = "Push"
                total_chips_won_from_hands += self.currenthands[index].money_bet
                print("Both have same value of {}. Result is a push. {} got their {} chips back from this hand back.".format(dealers_hand.best_hand_value,self.name, self.currenthands[index].money_bet))
            elif self.currenthands[index].best_hand_value > dealers_hand.best_hand_value or dealers_hand.is_bust():
                result = "Win"
                print("Your hand wins. {name} got back their bet of {money_bet} plus an extra {money_bet}.".format(name=self.name, money_bet=self.currenthands[index].money_bet))
                total_chips_won_from_hands += self.currenthands[index].money_bet*win_multipliers[result]
            else:
                result = "Lose"
                print("Dealer wins. {} lost their {} chips from this hand to the dealer.".format(self.name,self.currenthands[index].money_bet))
            self.chips += self.currenthands[index].money_bet*win_multipliers[result]
            self.currenthands[index].money_made = self.currenthands[index].money_bet*win_multipliers[result] - self.currenthands[index].money_bet
        profits = total_chips_won_from_hands - total_money_bet
        if profits > 0:
            print("{} made a total of {} this round.".format(self.name, profits))
        elif profits < 0:
            print("{} lost a total of {} this round.".format(self.name, profits*-1))
        else:
            print("{} broke even this round.".format(self.name, profits*-1))
        print("{} still has a total of {} chips available.".format(self.name, self.chips))
        return

# class Dealer:
    
#     def __init__(self,chips =):


    

class Game:
    pass
    # def __init__(self, players, dealer, ):
        

        
            


class Hand:
    
    def __init__(self, cards, money_bet = 0, is_split = False):
        self.cards = cards
        self.hand_values = [0]
        self.money_bet = money_bet
        self.money_made = 0
        self.best_hand_value = 0
        self.is_split = is_split

    def __repr__(self):
        cards = ""
        for card in self.cards:
            cards += card[0] + " "
        self.get_value()
        best_current_value = self.get_best_value()
        return "Your cards:\n" + cards + "\nbest value: " + str(self.best_hand_value)

    def print_dealer_hand(self,first = False):
                if first:
                    print("Dealers cards:")
                    print(self.cards[0][0] + " X")
                    return
                else:
                    cards = ""
                    for card in self.cards:
                        cards += card[0] + " "
                    self.get_value()
                    best_current_value = self.get_best_value()
                    print("Dealers cards:\n" + cards + "\nbest value: " + str(self.best_hand_value))
                    return

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

    def split_hand(self,player,index = 0):
        #create two separate hands hitting each of them
        splitting_hand = player.currenthands.pop(index)
        hand1 = Hand([splitting_hand.cards[0],get_single_card(deck)],splitting_hand.money_bet,True)
        hand2 = Hand([splitting_hand.cards[1],get_single_card(deck)],splitting_hand.money_bet,True)
        player.chips -= splitting_hand.money_bet
        player.currenthands.insert(index,hand1)
        player.currenthands.insert(index+1,hand2)
        hand1.play_split_hand(player, index)
        return
        

    def play_hand(self, player, index = 0):
        if self.best_hand_value == 21:
            print(self)
            print("Blackjack!")
            return
        elif self.cards[0][1:] == self.cards[1][1:]and player.chips <= self.money_bet:
            print("You don't have the chips to split this hand.")
        elif self.cards[0][1:] == self.cards[1][1:]and player.chips >= self.money_bet:
            decision_made = False
            while decision_made == False:
                print(self)
                split_decision = input("Would you like to split this hand of value {}?(y/n)\n".format(self.best_hand_value)).lower().strip()
                if split_decision == "y":
                    decision_confirmation = False
                    while decision_confirmation == False:
                        confirmation = input("Are you sure you want to split this hand?(y/n)\n").lower().strip()
                        if confirmation == "y":
                            self.split_hand(player, index)
                            return
                        elif split_decision == "n":
                            decision_made = True
                            continue
                        else:
                            print("Please enter y or n.")
                            continue
                elif split_decision == "n":
                    decision_confirmation = False
                    while decision_confirmation == False:
                        print(self)
                        confirmation = input("Are you sure you don't want to split this hand?(y/n)\n").lower().strip()
                        if confirmation == "y":
                            decision_made = True
                            decision_confirmation = True
                            break
                        elif split_decision == "n":
                            decision_confirmation = True
                            continue
                        else:
                            print("Please enter y or n.")
                            continue
        while self.is_bust() == False:
            print(self)
            action = input("Would you like to hit or sit?(hit/sit)\n").lower().strip()
            if action == "hit":
                self.hit()
            elif action == "sit":
                self.sit()
                print("You sat with the following hand:")
                print(self)
                return
            else:
                print("Please enter hit or sit.")
        return

    def play_split_hand(self, player, index = 0):
        if "A" in self.cards[0][0] and "A" not in self.cards[1][0]:
            print(self)
            print("Since you split aces this is as far as you can go with this hand.")
            return
        if self.cards[0][1:] == self.cards[1][1:] and player.chips >= self.money_bet:
            print(self)
            split_decision = False
            while split_decision == False:
                split_choice = input("Would you like to split again?(y/n)\n").lower().strip()
                if split_choice == "y":
                    confirmation = False
                    while confirmation == False:
                        confirm = input("Are you sure you want to split this hand of value {}?(y/n)\n".format(self.best_hand_value)).lower().strip()
                        if confirm == "y":
                            self.split_hand(player, index)
                            return
                        elif confirm == "n":
                            confirmation = True
                            continue
                        else:
                            print("Please enter y or n.")
                elif split_decision == "n":
                    confirmation = False
                    while confirmation == False:
                        confirm = input("Are you sure you don't want to split this hand of value{}?(y/n)\n".format(self.best_hand_value)).lower().strip()
                        if confirm == "y":
                            confirmation = True
                            split_decision = True
                            continue
                        elif confirm == "n":
                            confirmation = True
                            continue
                        else:
                            print("Please enter y or n.")
                else:
                    print("Please enter y on n.")
        self.play_hand(player, index)
        return


    def play_dealer_hand(self):
        self.print_dealer_hand()
        if self.best_hand_value == 21:
            print("Blackjack. Dealer sits.")
            return
        while self.best_hand_value < 17:
            print("Dealer hits.")
            self.cards.append(get_single_card(deck))
            self.print_dealer_hand()
            if self.is_bust():
                print("Bust.")
                return
        print("Dealer sits with hand value of {}.".format(self.best_hand_value)) 
        return

    
    










    



    
reset_deck(deck)
test_player = Player("test_player")
test_player.get_hand_participantion()
test_dealer_hand = Hand(get_first_cards(deck))
test_dealer_hand.print_dealer_hand(True)
test_player.play_hands()
test_dealer_hand.play_dealer_hand()
test_player.collect_winnings(test_dealer_hand)


test_hand2 = Hand()






    

    

    # win_multipliers = {"Win":2, "Push": 1, "Blackjack!": 2.5, "Bust": 0}

# class Dealer:

    
#     


#     def __init__(self, num_decks):
#         self.hand = []
#         self.deck = deck*num_decks


