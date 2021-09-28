Date: 28/9/2021
Author: Arran Lemon

This project attempts to implement the game blackjack as a terminal game. It is the final project 
in the Learning Python module as a part of my Codecademy course. I have done some coding as a part
of my electrical engineering degree but due to a combination of poor mental health and other reasons
I haven't been able to develop the skill as much as I'd like. During the pandemic I've taken a 
semester off my studies and got a Codecademy subscription. I'm so far really enjoying the course and 
have enjoyed this project, it's sea of errors and all. 


As a fan of card games I originally wanted to implement the game Hearts but in that game it's important 
to not be able to see the hands of other players which seemed a little too inconvenient for a terminal game. 
So instead I decided to implement Blackjack. In this game everyone is supposed to be aware of everyone elses 
cards whilst still allowing for up to 8 players. I have implmented almost all of aspects of the game with the 
following exceptions:

INSURANCE:

When the dealers first face upc ard is an ace, each player gets the chance to bet on wheather the dealer has a 
blackjack or not (before any player takes an action). The insurance wager is equal to the original bet and is
used to canvel out the likely loss of the bet. This is one of the more obscure rules and strategy guides tend
to advise against taking inurance anyway.

SURRENDER:

If you have a really bad initial deal compared to the dealers you can give up the hand straight away and reclaim
half your bet, essentially giving the other half to the dealer uncontested. 

DOUBLING DOWN:

Like the opposite of surrender if you love your initial deal you can double the original bet. 


If you need to review the rules of the game they are detailed below.

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

In normal Blackjack each player takes an action in a clockwise direction but to avoid players constantly 
switching seats in front of the computer each player will complete all the actions for their hand before 
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