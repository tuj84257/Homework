####################################
#            PROJECT 1             #
####################################

# This project consists of python methods that a user (human) can use to create an automatically-generated 
# deck of cards, shuffle it, and draw five random cards from the deck. The user can also check the status
# of the deck (the remaining cards and their count), as well as have the five randomly-drawn cards displayed.
# The user can draw to the same hand randomly-selected cards in packs of five from multiple decks, 
# as well as have multiple hands draw five random cards from the same deck.

# Generating a deck:

#   To generate a deck, create a `deck` object:
#   myDeck = deck(numberOfCards, hasJoker)

#   If no arguments are passed to the `deck` object, a deck containing a single random card (that is not joker)
#   will be created by default. The user can also generate a `deck` object with a specified number of cards (integer),
#   and choose if the deck will contain a joker card (boolean).

#   To generate a deck with 26 cards, where one of them is a joker card, create a `deck` object like this:
#   myDeck = deck(numberOfCards=26, hasJoker=True)

#   If hasJoker=True, then the deck will accept a maximum of 53 generated cards; otherwise, the maximum number of
#   cards that can be generated will be 52.

# Shuffing the deck:

#   To shuffle the deck, apply the shuffle() method to the `deck` object:
#   myDeck.shuffle()

# Deal five random cards from the deck:

#   To deal five random cards from the deck, create a `hand` object, and apply the deal_to_me() method to it by 
#   passing the `deck` object as a parameter:
#   myHand = hand()
#   myHand.deal_to_me(myDeck)

# Show status of deck:

#   To check the count of the remaining cards in the deck and display them, apply the show_status() method to the 
#   `deck` object:
#   myDeck.show_status()

# Display hand:

#   To display the five cards on user's hand, apply the display() method to the `hand` object:
#   myHand.display()


import random

# Class representing the deck of cards

class deck:
    __allowed_suits = ['clubs', 'spades', 'diamonds', 'hearts',]                                           # the double underscore makes these lists private attributes, so that they cannot be accessed outside the class 
    __allowed_values = ['ace', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'jack', 'queen', 'king']                                                                                                                

    def __init__(self, numberOfCards=1, hasJoker=False):                                                   # by default, when deck is created, it has one randomly-generated card, and that card is not joker
        
        if not isinstance(numberOfCards, int):                                                             # if `numberOfCards` is not given as an integer by the user, raise error and don't create object
            print('ERROR: numberOfCards accepts only integer values')
            print('------------------------------------------------')
            raise ValueError('Argument(s) not allowed')
            
        if not isinstance(hasJoker, bool):                                                                 # if `hasJoker` is not given as a boolean value by the user, raise error and don't create object
            print('ERROR: hasJoker accepts only boolean values')
            print('-------------------------------------------')
            raise ValueError('Argument(s) not allowed')
        
        print('Creating your deck with ' + str(numberOfCards) + ' card(s)...')
        self.cards = []                                                                                    # store deck's cards in this list
        self.all_card_possibilities = []                                                                   # store all possible card object combinations in this array
        
        for suit in self.__allowed_suits:                                                                                     
                for value in self.__allowed_values:                                                        # loop through all suits and values
                    self.all_card_possibilities.append(card(suit, value))                                  # append all possible combinations to all_card_possibilities list
        
        if hasJoker is False:                                                                              # if hasJoker is not specified, or specified as False (meaning that the deck does not contain a joker card)
            if numberOfCards > 0 and numberOfCards < 53:                                                   #   if the number of cards is at least 1 or at most 52
                for i in range(numberOfCards):                                                             #       for as many cards as you want to be generated
                    random_card = random.choice(self.all_card_possibilities)                               #           choose a random card object from all_card_possibilities
                    self.all_card_possibilities.remove(random_card)                                        #           remove the selected card object from all_card_possibilities, so that you don't risk appending the same object in another iteration
                    self.cards.append(random_card)                                                         #           append the selected card object to the list of cards of the deck
            else:                                                                                          #   else raise an error and stop creation of object
                print('ERROR: numberOfCards out of range')
                print('---------------------------------')
                raise ValueError('Argument(s) not allowed')
        
        elif hasJoker is True:                                                                             # if hasJoker is specified as True (meaning that the deck contains a joker card)
            print('Your deck will contain a joker card')
            
            if numberOfCards > 0 and numberOfCards < 54:                                                   #   if the number of cards is at least 1 or at most 53
                self.cards.append(card('joker'))                                                           #       append joker to the list of deck's cards
                for i in range(numberOfCards-1):                                                           #       for as many cards as there are left to be generated (one less because joker is already appended)
                    random_card = random.choice(self.all_card_possibilities)                               #           choose a random card object from all_card_possibilities
                    self.all_card_possibilities.remove(random_card)                                        #           remove the selected card object from all_card_possibilities, so that you don't risk appending the same object in another iteration
                    self.cards.append(random_card)                                                         #           append the selected card object to the list of cards of the deck
            else:                                                                                          #   else raise an error and stop creation of object
                print('ERROR: numberOfCards out of range')
                print('---------------------------------')
                raise ValueError('Argument(s) not allowed')
            
        self.numberOfCards = numberOfCards                                                                 # make constructor's parameters attributes of the `deck` type object 
        self.hasJoker = hasJoker                                                                           # in case you need them to expand the code further

    def shuffle(self):                                                                                     # this function shuffles deck's cards                                                         
        random.shuffle(self.cards)
        print("\n--Your cards were shuffled--\n")
        
    def deal(self, card_object):                                                                           # this function removes a specified `card` type object from the deck and displays it
        print("You took from the deck: ", end="") 
        card_object.display() 
        self.cards.remove(card_object)
            
    def show_status(self):                                                                                 # this function checks how many cards there are in the `cards` list, and prints the cards and their count
        if len(self.cards) == 0:
            print('\nThere are no remaining cards in the deck')
        elif len(self.cards) == 1:
            print("\nThere is " + str(len(self.cards)) + " remaining card in the deck:\n")
            for card_ in self.cards:
                card_.display()
        else:
            print("\nThere are " + str(len(self.cards)) + " remaining cards in the deck:\n")
            for card_ in self.cards:
                card_.display()
        
#######################################################################################################################################################################################################################

# Class representing a single card in the deck

class card():
    def __init__(self, suit, value=""):
        self.suit = suit                                                                                   # make constructor's parameters attributes of the `card` type object
        self.value = value
        
    def display(self):                                                                                     # this function displays the suit and value of a card
        if self.value == "":                                                                               # if value is not specified when card is created, that means it is a joker card
            print(self.suit)                                                                               #   print only the suit ('joker' is considered to be a suit in the code)
        else:                                                                                              # else print the suit and value of the card
            print(self.suit, self.value)

#######################################################################################################################################################################################################################

# Class representing a player's hand

class hand():
    def __init__(self):
        self.list_of_five_cards = []                                                                       # store five random card objects here
    
    def deal_to_me(self, deck_object):                                                                     # this method draws five cards from `deck_object`
        if not isinstance(deck_object, deck):                                                              # if user does not pass a `deck` type object
            print('ERROR: deal_to_me() accepts only objects of type `deck`')                               #   raise error and stop creation of object
            print('-------------------------------------------------------')
            raise ValueError('Argument(s) not allowed')
        
        if len(deck_object.cards) < 5:                                                                     # if the deck has less than five cards
            print('Not enough cards to collect!')                                                          #   let the user know and don't draw any card
        else:                                                                                              # else 
            print('Drawing five cards from the deck...\n')
            for i in range(5):                                                                             #   select five random cards from the deck
                random_selection = random.choice(deck_object.cards)                                        #   append them to the your hand's list
                self.list_of_five_cards.append(random_selection)                                           #   and remove them from the deck
                deck_object.deal(random_selection)
        
    def display(self):                                                                                     # this method displays the hand 
        if len(self.list_of_five_cards) < 5:                                                               # if your hand is empty, let the user know
            print('\nYour hand is empty!')
        else:                                                                                              # else
            print("\nThe cards on your hand are:\n")                                                       #   display the card objects of your hand's list of five cards
            for card_ in self.list_of_five_cards:
                card_.display()

#######################################################################################################################################################################################################################

######################
#                    #
#        MAIN        #
#                    #
######################

myDeck = deck(numberOfCards=11, hasJoker=False)                                                            # create a deck with 11 cards, where none of them is 'joker'
myDeck.show_status()                                                                                       # checking the cards I have in the deck
    
myDeck.shuffle()                                                                                           # shuffle the deck

myHand = hand()                                                                                            # create a hand object
print('First hand:')
myHand.deal_to_me(myDeck)                                                                                  # deal five cards from the deck

myDeck.show_status()                                                                                       # display the remaining cards in the deck and their count
myHand.display()                                                                                           # display the cards in your hand

print('--------------------------------------')
print('Second hand (drawing cards from the same deck):')
myHand1 = hand()                                                                                           # create another hand
myHand1.deal_to_me(myDeck)                                                                                 # deal five more cards from the same deck to the new hand
myDeck.show_status()                                                                                       # display the remaining cards in the deck and their count
myHand1.display()                                                                                          # display the cards in your new hand

print('--------------------------------------')

myDeck1 = deck(numberOfCards=5, hasJoker=True)                                                             # create a new deck with 8 cards, where one of them is 'joker'
myDeck1.shuffle()                                                                                          # shuffle the new deck
print('Second hand:')
myHand1.deal_to_me(myDeck1)                                                                                # draw five cards from the new deck
myDeck1.show_status()                                                                                      # display the remaining cards in the deck and their count
myHand1.display()                                                                                          # display the cards in your hand

print('--------------------------------------')

# Here I'm just checking if deck's creation is working properly

print(len(myDeck.all_card_possibilities))                                                                  # the length of the remaining suit and value combinations for each deck 
print(len(myDeck1.all_card_possibilities))                                                                 # should be 52 or 53 minus the number of cards specified by user (depending on hasJoker value)