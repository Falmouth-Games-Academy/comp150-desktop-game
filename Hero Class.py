class MainHero:
    def __init__(self):
        self.health = 20
        self.movement_speed = 8
        self.attack_damage = 6
        self.armour = 4
    def StatusEffects(self, tile):
        if tile == 'grass':
            self.movement_speed += 1
            slef.armour -= 3
        elif tile == 'sand':
            self.movement_speed -= 3
            self.attack_damage -= 2
            self.armour += 2
        elif tile == 'stone':
            self.attack_damage += 2
            self.armour -= 2
        elif tile == 'dirt':
            self.movement_speed -= 2
            self.attack_damage -= 2
            self.armour += 2
        elif tile == 'water':
            self.movement_speed -= 4
            self.attack_damage -= 2
            
