class TwentySix:
    
    def __init__(self):
        self.memory = []
        self.dangerous_cards = [('Spades', 'Q'), ('Spades', 'K'), ('Spades, A'), ('Hearts', 2), ('Hearts', 3), ('Hearts', 4), ('Hearts', 5), ('Hearts', 6), ('Hearts', 7), 
                                ('Hearts', 8), ('Hearts', 9), ('Hearts', 10), ('Hearts', 'J'), ('Hearts', 'Q'), ('Hearts', 'K'), ('Hearts', 'A')]        
        self.card_numbers = list(range(2,11)) + ['J','Q','K','A']
        
    def pass_cards(self, hand):
        
        res = []
        hand.sort(key = lambda x: self.card_numbers.index(x[1]))
        ix = 0
        while len(res) < 3 and ix < 13:
            card = hand[ix]
            if card not in self.dangerous_cards:
                res.append(card)
            ix = ix + 1
            
        if len(res) == 3:
            for item in res:
                hand.remove(item)
        else:
            for item in res:
                hand.remove(item)
            rem = 3 - len(res)
            for i in range(rem):
                card = hand[0]
                res.append(card)
                hand.remove(card)
        
        return res
        
    def thow_card(self, stack):
        pass
        
    def clear(self):
        self.memory = []