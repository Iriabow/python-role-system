import dice_box
import enum
from abc import ABC, abstractclassmethod

# System dice is that beautifull dodecahedron of twelves faces.

d12 = lambda: dice_box.d(12)

class Modifier(ABC):

    @abstractclassmethod
    def get_bonus() -> int:
        pass

class GreatSword(Modifier):

    @classmethod
    def get_bonus() -> int:
        
        return dice_box.sum_n_d(2, 6)
 
class ShortSword(Modifier):

    @classmethod
    def get_bonus() -> int:
        
        return dice_box.d(6)

class Player:

    def __init__(self, name, body, mind, spirit):
        self.body = body
        self.health = body*10
        self.mind = mind
        self.spirit = spirit
        self.attack_modifier = lambda: 0
        self.defense_modifier = lambda: 0

    def set_weapon(self, weapon: Modifier):

        self.attack_modifier = weapon.get_bonus


def attack(attacker: Player) -> int:    
    
    return d12() + attacker.atack_modifier()

def defend(defender: Player) -> int:

    return d12() + defender.defense_modifier()


class SustancesTypes(enum.Enum):
    material=1
    organic=2
    mental=3
    spiritual=4 


class Estructures(enum.Enum):
    tree="tree"
    cow="cow"
    person="person"
    dragon="dragon"


class Sustance:

    def __init__(self, energy_value: float, estructure: Estructures, s_type: SustancesTypes):
        self.energy_value: float = energy_value
        self.estructure: Estructures = estructure
        self.type: SustancesTypes = s_type


class SustanceInteraction():
    pass

class MindInteraction():
    pass

class SpiritInteraction():
    pass

def resolve_ofensive(attacker: Player, defender: Player, efective_defense_bonus=0):

    attack_result = defend(defender) + efective_defense_bonus - attack(attacker) 
    if attack_result>=0:
        defender.health = defender.health - attack_result*5
    elif attack_result<=-3: # Counter attack
        resolve_ofensive(defender, attacker, efective_defense_bonus=-attack_result)
    
    return attack_result