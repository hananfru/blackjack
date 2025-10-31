from core.deck import *
from core.game_logic import *


def play():
    deck = build_standart_deck()
    deck = shuffle_by_suit(deck)
    player = {"hand": []}
    dealer = {"hand": []}
    run_full_game(deck, player,dealer)

if __name__ == "__main__":
    play()