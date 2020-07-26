from player import Player

def main():
    Player1 = Player("Ailios", 30, 12)
    Player2 = Player("Hermes", 20, 6)
    Player1.attack_player(Player2)

if __name__ == '__main__':
    main()
