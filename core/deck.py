import random



def build_standart_deck():
    deck = []
    for item in ['A'] + [f"{i}" for i in range(2,11)] + ["J", "Q", "K"]:
        for suit in ['S', 'H', "D", "C"]:
            deck.append({"rank": item, "suit": suit})
    return deck

def shuffle_by_suit(deck, swap = 5000):
    suits = {
        "H": lambda h : h % 5 == 0,
        "C": lambda c : c % 3 == 0,
        "D": lambda d : d % 2 == 0,
        "S": lambda s : s % 7 == 0,
    }
    for _ in range(swap):
        i = random.randint(0,51)
        j = random.randint(0,51)
        while i == j or not suits[deck[i]["suit"]](j):
            j = random.randint(0,51)
        deck[i], deck[j] = deck[j], deck[i]
    return deck    


