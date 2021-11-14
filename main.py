import player as pl
import random as rd
#KELL elé a pl., amikor példányosítasz!

#Initiating the deck
card_colors = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
card_numbers = list(range(2,11)) + ['J','Q','K','A']
deck = [(color, number) for color in card_colors for number in card_numbers]

#A few helper functions
def bigger(v1, v2):
    if card_numbers.index(v1) > card_numbers.index(v2):
        return v1
    else:
        return v2
        
def calculate_point_value(stack):
    value = 0
    for item in stack:
        if item[0] == 'Spades':
            value = value + 12
        else:
            value = value + 1
            
    return value

def deal():
    hands = [[],[],[],[]]

    while len(deck) > 0:
        for hand in hands:
            rx = rd.randint(0, len(deck) - 1)
            card = deck[rx]
            hand.append(card)
            deck.remove(card)
    
    return hands

#Creating the bots with the hands and the scoreboard
hands = deal()
bot1 = pl.Player("bot1", hands[0])
bot2 = pl.Player("bot2", hands[1])
bot3 = pl.Player("bot3", hands[2])
bot4 = pl.Player("bot4", hands[3])

scoreboard = {}
scoreboard[bot1] = 0
scoreboard[bot2] = 0
scoreboard[bot3] = 0
scoreboard[bot4] = 0

#Playing the game
rounds = 1

while max(scoreboard.values()) < 100:
    
    #Check how to pass cards according to number of rounds
    match rounds%4:
        case 0:
            #Every fourth round, no cards are passed.
            pass
        case 1:
            #Every first round, 1 passes to 2, 2 passes to 3, 3 passes to 4, 4 passes to 1 (so the player to the right)
            bot1.receive_cards(bot4.pass_cards())
            bot2.receive_cards(bot1.pass_cards())
            bot3.receive_cards(bot2.pass_cards())
            bot4.receive_cards(bot3.pass_cards())
        case 2:
            #Every second round, 1 passes to 4, 2 passes to 1, 3 passes to 2, 4 passes to 3 (so the player to the left)
            bot1.receive_cards(bot2.pass_cards())
            bot2.receive_cards(bot3.pass_cards())
            bot3.receive_cards(bot4.pass_cards())
            bot4.receive_cards(bot1.pass_cards())
        case 3:
            #Every first round, 1 passes to 3, 2 passes to 4, 3 passes to 1, 4 passes to 2 (so the player on the opposite side)
            bot1.receive_cards(bot3.pass_cards())
            bot2.receive_cards(bot4.pass_cards())
            bot3.receive_cards(bot1.pass_cards())
            bot4.receive_cards(bot2.pass_cards())
    
    #Playing the actual round
    while len(bot1.hand) > 0:
        stack = []
        stack_max = 0
        stack_color = ""
        
        new_card = bot1.throw_card(stack)
        stack.append(new_card)
        stack_color = new_card[0]
        stack_max = new_card[1]
        max_bot = bot1
        
        new_card = bot2.throw_card(stack)
        stack.append(new_card)
        if stack_color == new_card[0]:
            stack_max = bigger(new_card[1], stack_max)
            if stack_max == new_card[1]:
                max_bot = bot2
            
        new_card = bot3.throw_card(stack)
        stack.append(new_card)
        if stack_color == new_card[0]:
            stack_max = bigger(new_card[1], stack_max)
            if stack_max == new_card[1]:
                max_bot = bot3
            
        new_card = bot4.throw_card(stack)
        stack.append(new_card)
        if stack_color == new_card[0]:
            stack_max = bigger(new_card[1], stack_max)
            if stack_max == new_card[1]:
                max_bot = bot4
    
        max_bot.receive_stack(stack)
    
    #Dealing again    
    rounds = rounds + 1
    deck = [(color, number) for color in card_colors for number in card_numbers]
    hands = deal()
    
    print("---------------------------")
    for key in scoreboard.keys():
        scoreboard[key] = scoreboard[key] + calculate_point_value(key.stack)
        print(key.name, scoreboard[key])
    
    bot1.reset(hands[0])
    bot2.reset(hands[1])
    bot3.reset(hands[2])
    bot4.reset(hands[3])        
    
    
winner_value = min(scoreboard.values())
for key in scoreboard.keys():
    if scoreboard[key] == winner_value:
       winner_key = key

print(winner_key.name, "won.")       