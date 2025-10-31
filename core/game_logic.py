from core.player_io import *

def deal_two_each(deck, player, dealer):
    player["hand"] = [deck.pop(), deck.pop()]
    dealer["hand"] = [deck.pop(), deck.pop()]
    print(f"player-hand: {player["hand"]}")
    print(f"dealer-hand: {dealer["hand"]}")

def calculate_hand_value(hand):
    total = 0
    aces = []
    for card in hand:
        if card["rank"].isdigit():
            total += int(card["rank"])
        elif card["rank"] != 'A':
            total += 10
        else:
            aces.append(card)
    for i in range(len(aces)):
        if 21 - total -len(aces) + i > 10:
            total += 11
        else: 
            total+=1

    return total

def dealer_play(deck, dealer):
    while calculate_hand_value(dealer["hand"]) < 17:
        dealer["hand"].append(deck.pop())
    return calculate_hand_value(dealer["hand"]) > 21

def player_play(deck, player):
    print(player["hand"])
    action = ask_player_action()
    while action == 'H' and calculate_hand_value(player["hand"]) < 21:
        player["hand"].append(deck.pop())
        print(player["hand"])
        if calculate_hand_value(player["hand"]) > 21:
            print("You Losed!")
            return
        action = ask_player_action()

def who_won(player, dealer):
    if calculate_hand_value(player["hand"]) > dealer["hand"]:
        print('Congratulations!')
    elif calculate_hand_value(player["hand"]) < dealer["hand"]:
        print("You can't win the dealer")
    else:
        print("Equality")

def run_full_game(deck, player, dealer):
    deal_two_each(deck, player, dealer)
    player_play(deck, player)
    if calculate_hand_value(player["hand"]) > 21:
        print("Game Over dealer won")
        return 
    player_Won = dealer_play(deck, dealer)
    if(player_Won):
        print('Congratulations!')
    else: 
         who_won(player, dealer)
    print(f"Player hand: {calculate_hand_value(player["hand"])}")
    print(f"dealer hand: {calculate_hand_value(dealer["hand"])}")
    
