from player import Player
from player import Sorcerer

def main():
    Player1 = Player("Ailios", 30, 8)
    Player2 = Sorcerer("Hermes", 20, 6)
    Player1.attack_player(Player2)
    Player1.attack_player(Player2)
    Player1.attack_player(Player2)

if __name__ == '__main__':
    main()
