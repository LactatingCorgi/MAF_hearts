import random as rd

class Player:
    def __init__(self, name, hand):
        self.name = name
        self.hand = hand
        self.stack = []
        
    def reset(self, hand):
        self.hand = hand
        self.stack = []
    
    def pass_cards(self):
        '''
        Selects three card from it's hand to pass over
        '''
        
        #For now, it selects randomly
        cards_to_pass = []
        for i in range(3):
            rx = rd.randint(0, len(self.hand) - 1)
            card = self.hand[rx]
            cards_to_pass.append(card)
            self.hand.remove(card)
            
        return cards_to_pass
        
    def receive_cards(self, new_cards):
        '''
        Append the list of cards by cards received from one of the opponents
        '''
        
        for card in new_cards:
            self.hand.append(card)
            
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