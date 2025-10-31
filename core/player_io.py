def create_player():
    name = input("Please Enter your name:\n")
    return{"name": name, "hand": []}

def ask_player_action():
    action = input("Press 'H' for continue or 'S' to stand")
    while action not in ['H', 'S']:
        action = input("Press 'H' for continue or 'S' to stand")
    return action


