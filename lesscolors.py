class LessColors:
    
    def __init__(self):
        self.memory = []
        self.dangerous_cards = [('Spades', 'Q'), ('Spades', 'K'), ('Spades, A'), ('Hearts', 2), ('Hearts', 3), ('Hearts', 4), ('Hearts', 5), ('Hearts', 6), ('Hearts', 7), 
                                ('Hearts', 8), ('Hearts', 9), ('Hearts', 10), ('Hearts', 'J'), ('Hearts', 'Q'), ('Hearts', 'K'), ('Hearts', 'A')]        
        self.card_numbers = list(range(2,11)) + ['J','Q','K','A']
        
    def pass_cards(self, hand):
        
        res = []
        color_numbers = {}
        for item in hand:
            key = item[0]
            if key not in color_numbers.keys():
                color_numbers[key] = 1
            else:
                color_numbers[key] = color_numbers[key] + 1
                
        colors_ascending = [item for item in sorted(color_numbers.keys(), key = lambda x: color_numbers[x])]
        
        color_sorted_hand = []
        for i in range(len(colors_ascending)):
            for item in hand:
                if item[0] == colors_ascending[i]:
                    color_sorted_hand.append(item)
        
        for i in range(3):
            card = hand[0]
            res.append(card)
            hand.remove(card)
              
        return res
        
    def thow_card(self, stack):
        pass
        
    def clear(self):
        self.memory = []