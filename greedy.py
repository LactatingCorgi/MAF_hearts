class Greedy:
    
    def __init__(self):
        self.memory = []
        self.dangerous_cards = [('Spades', 'Q'), ('Spades', 'K'), ('Spades, A'), ('Hearts', 2), ('Hearts', 3), ('Hearts', 4), ('Hearts', 5), ('Hearts', 6), ('Hearts', 7), 
                                ('Hearts', 8), ('Hearts', 9), ('Hearts', 10), ('Hearts', 'J'), ('Hearts', 'Q'), ('Hearts', 'K'), ('Hearts', 'A')]
        self.card_numbers = list(range(2,11)) + ['J','Q','K','A']
    
    
    def pass_cards(self, hand):
        
        danger = []
        res = []
        for item in hand:
            if item in self.dangerous_cards:
                danger.append(item)
                
        if len(danger) > 2:
            if ('Spades', 'Q') in danger:
                res.append(('Spades', 'Q'))
                danger.remove(('Spades', 'Q'))
                hand.remove(('Spades', 'Q'))
                danger.sort(key = lambda x: self.card_numbers.index(x[1]), reverse = True)
                for i in range(2):        
                    res.append(danger[i])
                    hand.remove(danger[i])
            else:
                danger.sort(key = lambda x: self.card_numbers.index(x[1]), reverse = True)
                for i in range(3):
                    res.append(danger[i])
                    hand.remove(danger[i])
        else:
            rem = 3 - len(danger)
            for item in danger:
                res.append(item)
                hand.remove(item)
            hand.sort(key = lambda x: self.card_numbers.index(x[1]), reverse = True)
            for i in range(rem):
                card = hand[0]
                res.append(card)
                hand.remove(card)
               
        return res
        
    def thow_card(self, hand, stack):
        pass
        
    def clear(self):
        self.memory = []