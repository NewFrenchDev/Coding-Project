
class Player:

    def __init__(self, pseudo, health, attack):
        self.pseudo = pseudo
        self.health = health
        self.attack = attack
        print("Bienvenue au joueur:", pseudo, "/ Points de vie: ", health, "/ Attaque: ", attack)

    def get_pseudo(self):
        return self.pseudo

    def get_health(self):
        return self.health

    def get_attack(self):
        return self.attack

    def damage(self, damage):
        self.health -= damage

    def attack_player(self, target_player):
        target_player.damage(self.attack)
        if target_player.health > 0:
            print("{} a infligé {} points de dégat à {}".format(self.pseudo, self.attack, target_player.pseudo))
            print("Il reste {} points de vie à {}".format(target_player.health, target_player.pseudo))
        else:
            print("{} est mort :(".format(target_player.pseudo))


class Sorcerer(Player):

    def __init__(self, pseudo, health, attack):
        super().__init__(pseudo, health, attack)
        self.magic_shield = 10
        print("Bienvenue au sorcier:", pseudo, "/ Points de vie:", health, "/ Attaque:", attack)

    def damage(self, damage):
        if self.magic_shield > 0:
            self.magic_shield -= damage
        damage = 0
        if self.magic_shield > 0:
            print("Un bouclier magique protège le sorcier")
            print("Points restant: ", self.magic_shield)
        super().damage(damage)



