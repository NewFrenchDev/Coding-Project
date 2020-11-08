from player import Player
from player import Sorcerer
from mobs import Monster
from mobs import Gobelin

def main():
    Player1 = Player("Ailios", 1, 10, 30, 8)
    Player2 = Sorcerer("Hermes", 1, 10, 20, 6)
    Monster1 = Gobelin(10, 2, 2)


if __name__ == '__main__':
    main()
