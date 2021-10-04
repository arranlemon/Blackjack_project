
from random import randint
from time import sleep

win_multipliers = {"Lose": -1, "Win": 1, "Blackjack": 1.5, "Push": 0}

min_bet = 10
max_bet = 100

def get_first_cards(deck):
        card1 = deck.pop(randint(0,len(deck)-1))
        card2 = deck.pop(randint(0,len(deck)-1))
        return [card1,card2]

def get_single_card(deck):
    card = deck.pop(randint(0,len(deck)-1))
    return card

def reset_deck(deck):
    deck = [["2H",2], ["3H",3], ["4H",4], ["5H",5], ["6H",6], ["7H",7], ["8H",8], ["9H",9], ["10H",10], ["JH",10], ["QH",10], ["KH",10], ["AH",1,11], ["2S",2], ["3S",3], ["4S",4], ["5S",5], ["6S",6], ["7S",7], ["8S",8], ["9S",9], ["10S",10], ["JS",10], ["QS",10], ["KS",10], ["AS",1,11], ["2D",2], ["3D",3], ["4D",4], ["5D",5], ["6D",6], ["7D",7], ["8D",8], ["9D",9], ["10D",10], ["JD",10], ["QD",10], ["KD",10], ["AD",1,11], ["2C",2], ["3C",3], ["4C",4], ["5C",5], ["6C",6], ["7C",7], ["8C",8], ["9C",9], ["10C",10], ["JC",10], ["QC",10], ["KC",10], ["AC",1,11]]
    return



class Player:
    
    def __init__(self, name, chips = 100):
        self.name = name
        self.currenthands = []
        self.chips = chips
        self.starting_chips = chips

    def __repr__(self):
        return_string = "Players name: {}\nPlayers chips: {}\n".format(self.name,self.chips)
        return return_string

    def get_hand_participation(self, deck):
        money_bet = 0
        playing_hand = False
        while playing_hand == False:
            play_hand = input("Would {} like to play this hand?(y/n):\n".format(self.name)).lower().strip()
            if play_hand == "n" or play_hand == "no":
                print("{} sits this hand out.".format(self.name))
                return
            elif play_hand == "y" or play_hand == "yes":
                playing_hand = True
                money_confirmed = False
                bet_confirmed = False
                while money_confirmed == False and bet_confirmed == False:
                    try:
                        money_bet = int(input("You have {} chips. How much would you like to bet on this hand?\n".format(self.chips)))
                        if money_bet <= self.chips and money_bet%10 == 0 and money_bet >= min_bet and money_bet <= max_bet:
                            money_confirmed = True
                            bet_confirmed = False
                        elif money_bet == 0:
                            print("No risk no reward. You need to bet something. Please enter a multiple of 10 that is between {} and {}.".format(min_bet, max_bet))
                            continue
                        elif money_bet < 0:
                            print("Nice try I thought of that. Please enter a multiple of 10 that is between {} and {}.".format(min_bet, max_bet))
                            continue
                        elif money_bet > 100:
                            print("Calm down Mr Packer we can only take bets between {} and {}.".format(min_bet, max_bet))
                            continue
                        elif money_bet < 10:
                            print("Come on cheepskate you need to bet between {} and {}.".format(min_bet, max_bet))
                            continue
                        else:
                            print("You have {} chips available. Please enter a multiple of 10 that is between {} and {}.".format(self.chips, min_bet, max_bet))
                            continue
                    except ValueError:
                        print("Please enter an integer number you would like to bet.")
                        continue
                    while bet_confirmed == False:
                        bet_confirmation = input("You want to bet {} chips on this hand?(y/n)\n".format(money_bet)).lower().strip()
                        if bet_confirmation == "y" or bet_confirmation == "yes":
                            self.currenthands.append(Hand(get_first_cards(deck), money_bet))
                            print("{} was dealt the following:".format(self.name))
                            print(self.currenthands[0])
                            sleep(2)
                            money_confirmed = True
                            bet_confirmed = True
                        elif bet_confirmation == "n" or bet_confirmation == "no":
                            print("Please enter the value you intended.")
                            money_confirmed = False
                            bet_confirmed = False
                            break
                        elif bet_confirmation == "help" or bet_confirmation == "?":
                            print(
                                """
Here you are deciding how much you would like to bet on the hand.
If you have a hand value less that the dealers you lose the hand and the amount 
you bet will be forfeit to the dealer. If you have a hand value greater than the
dealers you win you will recieve the amount you bet back and that amount again. 
If you win and have a blackjack (Ace and a card of value 10) you recieve you bet 
back and one and a half times that amount again. If you have a hand value equal to 
the dealers the result is called a push and you recieve your bet back. The minimum
bet is 10 and the maximum bet is 100. All bets must be a multiple of 10.  
"""
                            )
                            money_confirmed = False
                            bet_confirmed = False
                            break
                        else:
                            print("Please enter y or n.")
                            continue
            else:
                print("Please enter y or n.")
        return

    def play_hands(self, deck):
        print("{} will now play their hands:".format(self.name))
        sleep(1.5)
        #now we actually play the hand
        index = 0
        for hand in self.currenthands:
            if hand.is_split:
                hand.play_split_hand(self, deck, index)
                index += 1
            else:
                hand.play_hand(self, deck, index)
                index += 1
            if index < len(self.currenthands):
                print("Next hand:")
            sleep(2)
        return

    def collect_winnings(self, dealers_hand):
        if len(self.currenthands) == 0:
            print("{} did not play this round. Their chips remain at {}".format(self.name,self.chips))
            sleep(2)
            return
        starting_chips = self.chips
        print("{} will now evaluate their hands:".format(self.name))
        sleep(2)
        dealers_hand.print_dealer_hand()
        sleep(2)
        dealer_is_blackjack = len(dealers_hand.cards) == 2 and dealers_hand.best_hand_value == 21
        for index in range(0,len(self.currenthands)):
            result = ""
            print("Hand " + str(index+1) + ":")
            sleep(1)
            print(self.currenthands[index])
            sleep(2)
            hand_is_blackjack = len(self.currenthands[index].cards) == 2 and self.currenthands[index].best_hand_value == 21
            if self.currenthands[index].is_bust():
                result = "Lose"
                print("You bust with value of {}. Result is a loss of {} chips to the dealer.".format(self.currenthands[index].best_hand_value, self.currenthands[index].money_bet))
            elif dealer_is_blackjack and hand_is_blackjack:
                result = "Push"
                print("Both have blackjack. Result is a push. {} got their {} chips back from this hand.".format(self.name, self.currenthands[index].money_bet))
            elif dealer_is_blackjack and not hand_is_blackjack:
                result = "Lose"
                print("Dealers blackjack wins. Result is a loss. {} lost their {} chips from this hand to the dealer.".format(self.name,self.currenthands[index].money_bet))
            elif not dealer_is_blackjack and hand_is_blackjack:
                result = "Blackjack"
                print("Your Blackjack wins. {} got back their bet of {} plus an extra {}.".format(self.name, self.currenthands[index].money_bet, self.currenthands[index].money_bet*win_multipliers[result]))
            elif dealers_hand.best_hand_value == self.currenthands[index].best_hand_value:
                result = "Push"
                print("Both have same value of {}. Result is a push. {} got their {} chips back from this hand back.".format(dealers_hand.best_hand_value,self.name, self.currenthands[index].money_bet))
            elif self.currenthands[index].best_hand_value > dealers_hand.best_hand_value or dealers_hand.is_bust():
                result = "Win"
                print("Your hand wins. {name} got back their bet of {money_bet} plus an extra {money_bet}.".format(name=self.name, money_bet=self.currenthands[index].money_bet))
            else:
                result = "Lose"
                print("Dealer wins. {} lost their {} chips from this hand to the dealer.".format(self.name,self.currenthands[index].money_bet))
            self.currenthands[index].money_made = int(self.currenthands[index].money_bet*win_multipliers[result])
            self.chips += self.currenthands[index].money_made
            sleep(2)
        profits = self.chips - starting_chips
        if profits > 0:
            print("{} made a total of {} this round.".format(self.name, profits))
        elif profits < 0:
            print("{} lost a total of {} this round.".format(self.name, profits*-1))
        else:
            print("{} broke even this round.".format(self.name))
        print("{} has a total of {} chips available.".format(self.name, self.chips))
        sleep(2)
        return

    def clear_hands(self):
        self.currenthands = []
        return

    def leave_table(self):
        profits = self.chips - self.starting_chips
        print("\n{}:".format(self.name))
        if profits > 0:
            print("{name} cashes out with {chips} chips.\n{name} made {profits} at the table.".format(name = self.name, chips = self.chips, profits = profits))
        elif profits == 0:
            print("{name} cashes out with {chips} chips.\n{name} broke even at the table.".format(name = self.name, chips = self.chips))
        else:
            print("{name} cashes out with {chips} chips.\n{name} lost {profits} at the table.".format(name = self.name, chips = self.chips, profits = profits*-1))
        return



    
def get_players():
    players = []
    more_players = True
    player_number = 1
    while more_players:
        got_name = False
        while got_name == False:
            players_name = input("Player {} please enter your name:\n".format(player_number))
            confirmed_name = False
            while confirmed_name == False:
                confirmation_answer = input("Confirming players name is {}?(y/n)\n".format(players_name)).lower().strip()
                if confirmation_answer == "yes" or confirmation_answer == "y":
                    confirmed_name = True
                    got_name = True
                elif confirmation_answer == "no" or confirmation_answer == "n":
                    print("Please enter the name you intended.")
                    confirmed_name = True
                elif confirmation_answer == "help" or confirmation_answer == "?":
                    print(
"""
Here you are entering the name you will be referred to as 
for the duration of the game.
"""
                    )
                    confirmed_name = True
                else:
                    print("Please enter y or n.")
        got_chips = False
        while got_chips == False:
            try:
                chips = int(input("Please enter how many chips {} is starting with:\n".format(players_name)))
                if chips < min_bet:
                    print("You need at least 10 chips to sit at the table.")
                    continue
                elif chips < 0:
                    print("You can't have negative chips I'm afraid.")
                    continue
            except ValueError:
                print("Please enter an integer value of at least 10.")
                continue
            confirmed_chips = False
            while confirmed_chips == False:
                confirmation = input("Confirming that {} is starting with {} chips today?(y/n)\n".format(players_name, chips)).lower().strip()
                if confirmation == "yes" or confirmation == "y":
                    got_chips = True
                    confirmed_chips = True
                elif confirmation == "no" or confirmation == "n":
                    print("Please enter the amount of chips you intended.")
                    confirmed_chips = True
                elif confirmation == "help" or confirmation == "?":
                    print("""
Here you are entering how many chips you're starting with.
This is fake money so don't worry about not making rent this week.
                    """)
                    confirmed_chips = False
                else:
                    print("Please enter y ot n.")
        players.append(Player(players_name, chips))
        player_number += 1
        if len(players) == 8:
            print("You now have 8 players and the table is full.")
            return players
        keep_going = False
        while keep_going == False:
            more = input("Are there more people wanting to play?(y/n)\n").lower().strip()
            if more == "yes" or more == "y":
                confirmed_more = False
                while confirmed_more == False:
                    more_decision = input("Are you sure there are more players wanting to play?(y/n)\n").lower().strip()
                    if more_decision == "yes" or more_decision == "y":
                        confirmed_more = True
                        keep_going = True
                    elif more_decision == "no" or more_decision == "n":
                        confirmed_more = True
                    else:
                        print("Please enter y or n.")
            elif more == "no" or more == "n":
                confirmed_no_more = False
                while confirmed_no_more == False:
                    no_more_decision = input("Are you sure there are no more players wanting to play?(y/n)\n").lower().strip()
                    if no_more_decision == "yes" or no_more_decision == "y":
                        confirmed_no_more = True
                        keep_going = True
                        more_players = False
                    elif no_more_decision == "no" or no_more_decision == "n":
                        confirmed_no_more = True
                    else:
                        print("Please enter y or n.")
            elif more == "help" or more == "?":
                print("""
If there are more people wanting to play then say yes.
If everyone who wants to play has already chosen a name 
and number of chips then say no and begin playing Blackjack. 
                """)
                confirmed_no_more = True
            else:
                print("Please enter yes or no.")
                confirmed_no_more = True
    return players

    





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

    def hit(self,deck):
        confirmed = False
        while confirmed == False:
            confirmation_decision = input("Confirming that you would like to hit with this hand of current value {}?(y/n)\n".format(self.best_hand_value)).lower().strip()
            if confirmation_decision == "y" or confirmation_decision == "yes":
                confirmed = True
                self.cards.append(get_single_card(deck))
                print(self)
                if self.is_bust():
                    print("Bust.")
            elif confirmation_decision == "n" or confirmation_decision == "no":
                print("Please enter the action you intended.")
                return False
            else:
                print("Please enter y or n.")
        return True


    def sit(self):
        confirmed = False
        while confirmed == False:
            confirmation_decision = input("Confirming that you would like to sit with this hand of current value {}?(y/n)\n".format(self.best_hand_value)).lower().strip()
            if confirmation_decision == "y" or confirmation_decision == "yes":
                confirmed = True
            elif confirmation_decision == "n" or confirmation_decision == "no":
                print("Please enter the action you intended.")
                return False
            else:
                print("Please enter y or n.")
        return True

    def is_bust(self):
        if self.best_hand_value > 21:
            return True
        return False

    def split_hand(self,player,deck,index = 0):
        splitting_hand = player.currenthands.pop(index)
        hand1 = Hand([splitting_hand.cards[0],get_single_card(deck)],splitting_hand.money_bet,True)
        hand2 = Hand([splitting_hand.cards[1],get_single_card(deck)],splitting_hand.money_bet,True)
        player.currenthands.insert(index,hand1)
        player.currenthands.insert(index+1,hand2)
        hand1.play_split_hand(player, deck, index)
        return
        

    def play_hand(self, player,deck, index = 0):
        self.get_best_value()
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
                if split_decision == "y" or split_decision == "yes":
                    decision_confirmation = False
                    while decision_confirmation == False:
                        yes_confirmation = input("Are you sure you want to split this hand?(y/n)\n").lower().strip()
                        if yes_confirmation == "y" or yes_confirmation == "yes":
                            self.split_hand(player, deck, index)
                            return
                        elif yes_confirmation == "n" or yes_confirmation == "no":
                            decision_confirmation = True
                            continue
                        else:
                            print("Please enter y or n.")
                            continue
                elif split_decision == "n" or split_decision == "no":
                    decision_confirmation = False
                    while decision_confirmation == False:
                        print(self)
                        confirmation = input("Are you sure you don't want to split this hand?(y/n)\n").lower().strip()
                        if confirmation == "y" or confirmation == "yes":
                            decision_made = True
                            decision_confirmation = True
                            break
                        elif split_decision == "n" or split_decision == "no":
                            decision_confirmation = True
                            continue
                        else:
                            print("Please enter y or n.")
                            continue
                elif split_decision == "help" or split_decision == "?":
                    print("""
You now have the option of splitting your hand. This will involve taking
the two cards in your existng hand and turning them into two separate hands.
It will also involve betting {} chips again.""".format(self.money_bet))
                else:
                    print("Please enter y or n.")
        confirmed_action = False
        print(self)
        while self.is_bust() == False or confirmed_action == False:
            action = input("Would you like to hit or sit?(hit/sit)\n").lower().strip()
            if action == "hit":
                confirmed_action = self.hit(deck)
            elif action == "sit":
                confirmed_action = self.sit()
                if confirmed_action == True:
                    print("You sat with the following hand:")
                    print(self)
                    return
            elif action == "help" or action == "?":
                print("""
If you HIT you will be dealt another card by the dealer. This has
the potential to make you hand even better but runs the risk of causing
you to bust (end up with a value greater than 21). If you SIT you will stay
with your current hand value and put it up against the dealer.   
                """)
            else:
                print("Please enter hit or sit.")
        return

    def play_split_hand(self, player, deck, index = 0):
        print("Hand {}:".format(index+1))
        if "A" in self.cards[0][0] and "A" not in self.cards[1][0]:
            print(self)
            print("Since you split aces this is as far as you can go with this hand.")
            return
        if self.cards[0][1:] == self.cards[1][1:] and player.chips >= self.money_bet:
            print(self)
            split_decision = False
            while split_decision == False:
                split_choice = input("Would you like to split again?(y/n)\n").lower().strip()
                if split_choice == "y" or split_choice == "yes":
                    confirmation = False
                    while confirmation == False:
                        confirm = input("Are you sure you want to split this hand of value {}?(y/n)\n".format(self.best_hand_value)).lower().strip()
                        if confirm == "y" or confirm == "yes":
                            self.split_hand(player,deck, index)
                            return
                        elif confirm == "n" or confirm == "no":
                            confirmation = True
                            continue
                        else:
                            print("Please enter y or n.")
                elif split_decision == "n" or split_decision == "no":
                    confirmation = False
                    while confirmation == False:
                        confirm = input("Are you sure you don't want to split this hand of value{}?(y/n)\n".format(self.best_hand_value)).lower().strip()
                        if confirm == "y" or confirm == "yes":
                            confirmation = True
                            split_decision = True
                            continue
                        elif confirm == "n" or confirm == "no":
                            confirmation = True
                            continue
                        else:
                            print("Please enter y or n.")
                elif split_decision == "help" or split_decision == "?":
                    print("""
Because you were dealt a card of the same value once more you 
have the option to split again. This of course requires betting
{} again.
                    """.format(self.money_bet))
                else:
                    print("Please enter y on n.")
        self.play_hand(player,deck, index)
        return


    def play_dealer_hand(self,deck):
        print("The dealer will now play their hand:")
        self.print_dealer_hand()
        sleep(2)
        if self.best_hand_value == 21:
            print("Blackjack. Dealer sits.")
            return
        while self.best_hand_value < 17:
            print("Dealer hits.")
            self.cards.append(get_single_card(deck))
            self.print_dealer_hand()
            sleep(2)
        if self.is_bust():
            print("Bust.")
            return
        print("Dealer sits with hand value of {}.".format(self.best_hand_value)) 
        return

    


def play_game():
    deck = [["2H",2], ["3H",3], ["4H",4], ["5H",5], ["6H",6], ["7H",7], ["8H",8], ["9H",9], ["10H",10], ["JH",10], ["QH",10], ["KH",10], ["AH",1,11], ["2S",2], ["3S",3], ["4S",4], ["5S",5], ["6S",6], ["7S",7], ["8S",8], ["9S",9], ["10S",10], ["JS",10], ["QS",10], ["KS",10], ["AS",1,11], ["2D",2], ["3D",3], ["4D",4], ["5D",5], ["6D",6], ["7D",7], ["8D",8], ["9D",9], ["10D",10], ["JD",10], ["QD",10], ["KD",10], ["AD",1,11], ["2C",2], ["3C",3], ["4C",4], ["5C",5], ["6C",6], ["7C",7], ["8C",8], ["9C",9], ["10C",10], ["JC",10], ["QC",10], ["KC",10], ["AC",1,11]]
    rules = False
    while rules == False:
        see_rules = input("Would you like to see the rules before we begin?(y/n)\n").lower().strip()
        if see_rules == "yes" or see_rules == "y":
            print("""
The rules of Blackjack are as follows:

The aim of Blackjack is to get a hand value that beats the dealer whilst still remaining equal or less than 21. 
The values of each card is as follows:

- Cards 2-10 have values equal to their number
- The ace can have a value of 1 or 11 (whichever suits the player)
- All other cards (J,Q,K) have a value of 10 

A hands value consists of the sum of all hand values of the cards in that hand. Before a player is dealt
their cards they elect an amount to bet on that hand. In this game all bets must be a multiple of 10 and
be between 10 and 100 in value (inclusive). After all players have decided on a betting amount each player 
is dealt two cards that make up their initial hand. The dealer then deals themself two cards but only one
is face up and visible to all players. 

THE PLAYERS TURN:

Each player will complete all the actions for their hand before 
moving onto the next player. The actions a player can take include the following:

Hit:

When a player hits they are dealt another card into their hand by the dealer. This cards value is added 
to the value of the hand. If the new value exceeds 21 the player busts and their turn is over. If the new value 
isn't a bust they may take another action.

Sit:

When a player sits they stop playing their hand and finish with the current hand value. They then wait for the
other players and dealer to play their hands. 

THE DEALERS TURN:

After each player has played their hand the dealer then plays their hand. Unlike players the dealer plays their 
hand according to a specific set of rules. The dealer first reveals the second card in their hand. The dealer
must hit for any hand value of sixteen or less. For any hand value of 17 or more the dealer must sit. In this
version of the game this includes a soft 17 (17 involving an ace treated as an 11).

ShOWDOWN:

After all the players and the dealer has played their hands each player compares their hand with the dealer to
determine if they've won any money. The possible results are as follows:

Blackjack: 

When the player has a blackjack (two cards of total value 21) and the dealer doesan't have a blackjack (even if
they have a total value of 21) the player wins. They receive their money back plus one and a half times their
betting amount (e.g. if the player bet 10 you will get your 10 back and an extra 15).

Win:

When the players hand value exceeds that of the dealer (and the player did not bust) or the dealer bust and the 
player did not, the player wins. in this case the player receives back the money they bet plus that amount again
(e.g. if the player bet 10 they would get their 10 back plus an extra 10). 

Push:

If the players hand is not a bust and is equal to that of the dealer the result is called a push. In this case
the player gets back the money they but and nothing extra (essentially breaking even on that hand). Note this
includes if the player and dealer both have a blackjack.

Loss:

If the player busts (even if the dealer has as well) or the dealers hand value exceeds the players hand and the
dealer hasn't busted the player loses. The player will not recieve their money back from that hand.

SIDE RULES:

Splitting:

If the player is dealt two cards of the same value (even if they are different such as a J and a Q) they have
the option of splitting the hand into two separate hands and playing them each individually. In order to do this 
the player must bet the same amount of money again. If the split hands were aces then the split hands get dealt a 
second card and that's as far as the player can go. If the player split anything other than aces the still get dealt
a second card but the player can keep playing on as for a normal hand if they so choose. Note that if the split hand
gets dealt another card of the same value as thee second card the player has the option to split again (which again)
requires the player to bet the same amount of money again.

FINAL NOTES:

This game doesn't implement the following side rules:

- Doubling down
- Surrender
- Insurance

Also note that this game is played with a single deck of cards that is shuffled/reset after each round. The reason more
decks are used in a casino is mostly to reduce shuffling time which isn't an issue in this case.   

If you are at all confused during the game you may enter "?" or "help" for assistance. If you want to see the rules again
they can be found in the README.txt file. Happy playing :)
""")
            break
        elif see_rules == "n" or see_rules == "no":
            confirmed_decision = False
            while confirmed_decision == False:
                rules_confirmation = input("Are you sure you don't want to see the rules?\n").lower().strip()
                if rules_confirmation == "yes" or rules_confirmation == "y":
                    print("If you need help at any point you can enter \"help\" or \"?\" into the terminal. Or you can see the rules\nin the README.txt file.")  
                    confirmed_decision = True
                    rules = True
                elif rules_confirmation == "no" or rules_confirmation == "n":
                    confirmed_decision = True
    players = get_players()
    keep_going = True
    while keep_going and len(players) != 0:
        for player in players:
            player.get_hand_participation(deck)
        hands_being_played = 0
        for player in players:
            hands_being_played += len(player.currenthands)
        if hands_being_played != 0:
            dealer_hand = Hand(get_first_cards(deck))
            dealer_hand.print_dealer_hand(True)
            sleep(2)
            i = 0
            for player in players:
                player.play_hands(deck)
            dealer_hand.play_dealer_hand(deck)
            index = 0
            while index < len(players):
                players[index].collect_winnings(dealer_hand)
                players[index].clear_hands()
                if players[index].chips < 10 and players[index].chips > 0:
                    print("{} only has {} chips left. Hopefully that's enough for the bus home.".format(players[index].name, players[index].chips))
                    print("{} has now left the table.".format(players[index].name))
                    players.pop(index)
                elif player.chips == 0:
                    print("{} only has no chips left. Hopefully someone will lend you the money to get home.".format(players[index].name))
                    print("{} has now left the table.".format(players[index].name))
                    players.pop(index)
                else:
                    index += 1
        else:
            print("Nobody played this round.")
        if len(deck) != 52:
                deck = [["2H",2], ["3H",3], ["4H",4], ["5H",5], ["6H",6], ["7H",7], ["8H",8], ["9H",9], ["10H",10], ["JH",10], ["QH",10], ["KH",10], ["AH",1,11], ["2S",2], ["3S",3], ["4S",4], ["5S",5], ["6S",6], ["7S",7], ["8S",8], ["9S",9], ["10S",10], ["JS",10], ["QS",10], ["KS",10], ["AS",1,11], ["2D",2], ["3D",3], ["4D",4], ["5D",5], ["6D",6], ["7D",7], ["8D",8], ["9D",9], ["10D",10], ["JD",10], ["QD",10], ["KD",10], ["AD",1,11], ["2C",2], ["3C",3], ["4C",4], ["5C",5], ["6C",6], ["7C",7], ["8C",8], ["9C",9], ["10C",10], ["JC",10], ["QC",10], ["KC",10], ["AC",1,11]]
        another_round = False
        while another_round == False:
            play_another = input("Are we playing another round?(y/n)\n").lower().strip()
            if play_another == "yes" or play_another == "y":
                another_round = True
            elif play_another == "no" or play_another == "n":
                another_confirmation = False
                while another_confirmation == False:
                    confirmation = input("Are you sure we're not playing another round?(y/n)\n").lower().strip()
                    if confirmation == "yes" or confirmation == "y":
                        another_confirmation = True
                        another_round = True
                        keep_going = False
                        for player in players:
                            player.leave_table()
                    elif confirmation == "no" or confirmation == "n":
                        another_confirmation = True
                    else:
                        print("Please enter y or n.")
            else:
                print("Please enter y or n.")
    print("Thanks for playing :)")


play_game()