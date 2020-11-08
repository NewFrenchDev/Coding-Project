
class Monster:

    def __init__(self, health, attack, xp):
        self.health = health
        self.attack = attack
        self.xp = xp

    def get_health(self):
        return self.health

    def get_attack(self):
        return self.attack

    def damage(self, damage):
        self.health -= damage


class Gobelin(Monster):

    def __init__(self, health, attack, xp):
        super().__init__(health, attack, xp)
        self.special_attack = attack + 2
        print("Un gobelin apparait!")

    def use_special_attack(self, target_player):
        target_player.health -= self.special_attack

    def give_xp_to_player(self, target_player):
        if self.heal <= 0:
            print("Gobelin meurt dans l'agonie")
            print("Le joueur gagne {} xp".format(self.xp))
            target_player.xp += self.xp
        if target_player.xp <= 0:
            print("Le joueur gagne un niveau!")