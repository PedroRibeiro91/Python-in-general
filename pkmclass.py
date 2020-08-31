
class Pokemon:
    def __init__(self, name, type, hp, attack, defense, speed):
        self.name = name
        self.type = type
        self.hp = hp
        self.attack = attack
        self.defense = defense
        self.speed = speed

    def getname(self):
        return self.name

    def gethp(self):
        return self.hp

    def getspeed(self):
        return self.speed

    def get_attack(self):
        return self.attack

    def get_defense(self):
        return self.defense

    def getType(self):
        return self.type

    def type_advantage(self, pokemon):
        coef_type_advantage = 1 # neutral
        if self.getType() == "fire" and pokemon.getType() == "water":
            coef_type_advantage = 0.5
        elif self.getType() == "fire" and pokemon.getType() == "grass":
            coef_type_advantage = 2
        elif self.getType() == "fire" and pokemon.getType() == "fire":
            coef_type_advantage = 0.5
        elif self.getType() == "water" and pokemon.getType() == "fire":
            coef_type_advantage = 2
        elif self.getType() == "water" and pokemon.getType() == "grass":
            coef_type_advantage = 0.5
        elif self.getType() == "water" and pokemon.getType() == "water":
            coef_type_advantage = 0.5
        elif self.getType() == "grass" and pokemon.getType() == "fire":
            coef_type_advantage = 0.5
        elif self.getType() == "grass" and pokemon.getType() == "grass":
            coef_type_advantage = 0.5
        elif self.getType() == "grass" and pokemon.getType() == "water":
            coef_type_advantage = 2
        return coef_type_advantage


Charizard = Pokemon("Charizard", "fire", 360, 293, 280, 328)
Blastoise = Pokemon("Blastoise", "water", 362, 291, 328, 280)
Venasaur = Pokemon("Venasaur", "grass", 364, 289, 291, 284)


