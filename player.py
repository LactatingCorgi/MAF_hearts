import random as rd
import greedy
import probability
import twentysix
import lesscolors

class Player:

    def __init__(self, name, hand, strategy):
        self.name = name
        self.hand = hand
        self.stack = []
        match strategy:
            case "greedy":
                self.strategy = greedy.Greedy()
            case "probability":
                self.strategy = probability.Probability()
            case "twentysix":
                self.strategy = twentysix.TwentySix()
            case "lesscolors":
                self.strategy = lesscolors.LessColors()
        
    def reset(self, hand):
        '''
        Resets itself - basically forgets everything that happened last round
        '''
        self.hand = hand
        self.stack = []
        self.strategy.clear()
    
    def pass_cards(self):
        '''
        Selects three card from it's hand to pass over, according to strategy
        '''
        
        return self.strategy.pass_cards(self.hand)
        
    def receive_cards(self, new_cards):
        '''
        Append the list of cards by cards received from one of the opponents
        '''

        for card in new_cards:
            self.hand.append(card)
        #print(len(self.hand))
            
    def receive_stack(self, stack):
        '''
        Receive the stack from the middle and keep the important cards
        '''
        
        for item in stack:
            if item[0] == "Hearts":
                self.stack.append(item)
            if item[0] == "Spades" and item[1] == "Q":
                self.stack.append(item)
                
    def throw_card(self, stack):
        '''
        Knowing the current state of stack and it's own cards, throws a card onto the stack
        '''
        
        #For now, it selects it randomly
        rx = rd.randint(0, len(self.hand) - 1)
        card = self.hand[rx]
        self.hand.remove(card)
        
        return card