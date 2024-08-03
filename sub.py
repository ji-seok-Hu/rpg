import random
import time


# Monster classes
class Body:
    def __init__(self, hp, harm, name) -> None:
        self.hp = hp
        self.harm = harm
        self.name = name
        self.is_alive = True
    
    def get_damage(self, damage):
        """
        get_damage(self, damage)
        takes damage.
        
        Args:
            damage -> int    
        """
        if self.is_alive == False:
            return
        self.hp -= damage
        if self.hp <= 0:
            self.is_alive = False
    
    def basic_attack(self, target):
        """
        basic_attack(self, target)
        attacks the target with the self.harm

        Args:
            target->: Body object    
        """
        target.get_damage(self.harm)
        

class Slime(Body): 
    def __init__(self):
        super().__init__(100, 10, '슬라임')
class Zombie(Body): 
    def __init__(self):
        super().__init__(200, 15, '좀비')
class Skeleton(Body): 
    def __init__(self):
        super().__init__(200, 20, '해골병사')

class Hero(Body):
    total_attack_harm = 10
    total_attack_mp = 30
    random_attack_harm = 45
    random_attack_mp = 10
    def __init__(self):
        super().__init__(300, 30, '영웅')
        self.mp = 100
    
    def reset(self):
        self.__init__()

    def use_mp(self, amount) -> bool:
        """
        if mana is lower than amount, return False.
        else, use mana then return True.
        """
        if self.mp == 0:
            return False
        mp_copied = self.mp
        mp_copied -= amount
        if mp_copied < 0:
            return False
        
        self.mp -= amount
        return True
    
    def total_attack(self, monster_list) -> bool:
        """
        total_attack(self, monster_list)
        attack the whole monsters on the field
        Args:
            monster_list -> List of monster objects
        Return:
            False -> attack failed
            True -> attack succeed
        """
        is_mana_enough = self.use_mp(self.total_attack_mp)
        if not is_mana_enough:
            return False

        harm = self.total_attack_harm

        for monster in monster_list:
            monster.get_damage(harm)
        
        return True
    
    def random_attack(self, monster_list) -> bool:
        """
        random_attack(self, monster_list)
        attacks a random monster on the field
        Args:
            monster_list -> List of monster objects
        Return:
            False -> attack failed
            True -> attack succeed
        """
        is_mana_enough = self.use_mp(self.random_attack_mp)
        if not is_mana_enough:
            return False


        harm = self.random_attack_harm
        
        monster = monster_list[random.randint(0,len(monster_list) - 1)]
        monster.get_damage(harm)

        return True
        

    
# Game class
class Field:
    monster_cls_list = [Slime, Zombie, Skeleton]
    opponent_field = []

    @classmethod
    def return_monsters_all(cls) -> tuple[Body]:
        return tuple(cls.opponent_field)
    
    @classmethod
    def summons_monster(cls, *args):
        """
        summons the monster inside of the args.
        """

        for monster in args:
            cls.opponent_field.append(monster)
    
    @classmethod
    def summons_string_print(cls):
        """
        print the summon string
        """
        summons_string = ",".join(list(map(lambda monster: monster.name, cls.opponent_field)))
        print(summons_string+"가 나타났다.")


    @classmethod
    def status_monster(cls, *args):
        """
        collect the status of the moster then print
        """
        name_list = []
        hp_list = []
        harm_list = []

        for monster in cls.opponent_field:
            name_list.append(f" {monster.name} ")
            hp_list.append(f"hp: {monster.hp} ")
            harm_list.append(f"harm: {monster.harm} ") 

        name_list = " ".join(name_list)
        hp_list = " ".join(hp_list)
        harm_list = " ".join(harm_list)
        print(name_list)
        print(hp_list)
        print(harm_list)
    
    @classmethod
    def random_summon(cls, min, max):
        """
        randomly summons the random kinds of the monster, with the input range min <= num < max
        """
        for i in range(random.randrange(min, max)):
            random_index = random.randrange(len(cls.monster_cls_list))
            cls.summons_monster(cls.monster_cls_list[random_index]())


hero = Hero()
Field.random_summon(1, 4)
Field.summons_string_print()

print(random.randint(0,3 - 1))