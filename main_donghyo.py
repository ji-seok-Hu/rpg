import random


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
        super().__init__(random.randint(50, 101), 10, '슬라임')
class Zombie(Body): 
    def __init__(self):
        super().__init__(random.randint(150, 201), 15, '좀비')
class Skeleton(Body): 
    def __init__(self):
        super().__init__(random.randint(175, 201), 20, '해골병사')
class Big_Slime(Body):
    def __init__(self):
        super().__init__(random.randint(300, 401), 15, '중슬')
class bomb_bat(Body):
    def __init__(self):
        super().__init__(random.randint(50, 70), 40, '폭박')
class Shield(Body):
    def __init__(self):
        super().__init__(80, 0, '방어막')

class Hero(Body):
    total_attack_harm = 10
    total_attack_mp = 30
    random_attack_harm = 45
    random_attack_mp = 10
    kill_mp = 80
    preparation = False
    def __init__(self):
        global preparation 
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
    def random_attack_ver2(self, monster_list) -> bool:

        is_mana_enough = self.use_mp(self.random_attack_mp)
        if not is_mana_enough:
            return False        
        harm = self.random_attack_harm
        
        
        monster = monster_list[random.randint(0,len(monster_list) - 1)]
        monster2 = monster_list[random.randint(0,len(monster_list) - 1)]
        if len(monster_list) >=2:
            while True:
                if monster == monster2:
                    monster2 = monster_list[random.randint(0,len(monster_list) - 1)]
                elif monster != monster2:
                    break
            monster.get_damage(harm)
            monster2.get_damage(harm)
            return True
        elif len(monster_list) <2:
            monster.get_damage(harm)
            return True
    
    
    def instant_death(self, target):
        is_mana_enough = self.use_mp(self.kill_mp)
        if not is_mana_enough:
            return False
        target.get_damage(target.hp)
        return True
# Game class
class Field:
    monster_cls_list = [Slime, Zombie, Skeleton,Big_Slime,bomb_bat]
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
    



# main stream
hero = Hero()
Field.random_summon(1, 4)
Field.summons_string_print()
shield = Shield()
shield.is_alive = False
while True:
    print()
    Field.status_monster()
    print()
    print(f"당신의 체력 : {hero.hp}")
    print(f"당신의 기력 : {hero.mp}")
    print()
    probability = [0,0,0,0,0,1,1,1,1,1]
    ## user input section
    selection = input(
        "어떤 행동을 하시겠습니까?\n" +  
        "1. 스킬 사용\n" +  
        "2. 도주\n" +  
        "3. 항복\n"  
        )
    if selection == "1":
        while True:
            Body.preparation = False
            selection = input(
                "어떤 스킬을 사용하시겠습니까?\n" +
                f"1. 기본 공격 (피해 {hero.harm}, 대상 지정)\n" + 
                f"2. 전체 공격 (피해 {hero.total_attack_harm}, 기력 {hero.total_attack_mp} 소모, 모든 대상 지정)\n" +
                f"3. 무작위 공격 (피해 {hero.random_attack_harm}, 기력 {hero.random_attack_mp} 소모, 무작위 대상 지정)\n" +
                f"4. 스킬사용 <검 부메랑> (피해 {hero.random_attack_harm}, 기력 {hero.random_attack_mp} 소모, 무작위 대상2명 지정 )\n"+
                f"5  스킬사용 <즉사저주> (즉사, 기력 {hero.kill_mp} 소모, 지정대상 )\n"+
                f"6. 돌아가기\n"+
                f"7. 숨겨진 치트키 사용 (체력을 1로 만드는 반 즉사기)\n"+
                f"8. 특수스킬 <준비운동> 을 사용합니다. (도주확률 +10% and harm +2)\n" +
                f"9. 특수스킬 <어둠의 고동효 중2 회복술>을 사용합니다. (랜덤 몬스터 소환후, 그 몬스터의 체력 절반만큼 회복.)\n" +
                f"10. 특수스킬 <철옹성>을 사용합니다.(총 80의 피해를 흡수하는 방어막을 얻습니다.)"
            )
            if selection == "1":
                Field.status_monster()
                selection = input("공격할 대상을 지정하십시오. 왼쪽 몬스터부터 1, 2, 3... 번째 몬스터입니다.")  
                index = int(selection) - 1 

                target = Field.return_monsters_all()[index]
                hero.basic_attack(target)
                print(f"당신은 기합을 넣고 {target.name} 을 베었습니다.")
                break
            elif selection == "2":
                is_success = hero.total_attack(Field.return_monsters_all())
                if is_success:
                    print("당신은 엄청난 기력을 집중합니다. 그리고 전방위로 검기를 흩뿌렸습니다. \n몬스터들은 크게 나자빠집니다.")
                    break
                else:
                    print("기력이 부족합니다.")
            elif selection == "3" :
                is_success = hero.random_attack(Field.return_monsters_all())
                if is_success:
                    print(f"당신은 눈을 감고 오직 당신과 검, 이 둘에만 집중합니다. 그리고 크게 검을 휘둘렀습니다.\n 아마 어딘가에는 맞지 않았을까요?")
                    break
                else:
                    print("기력이 부족합니다.")
            elif selection =="4":
                is_success = hero.random_attack_ver2(Field.return_monsters_all())
                if is_success:
                    print(f"당신은 눈을 감고 오직 당신과 검, 이 둘에만 집중합니다. 그리고 크게 검을 휘둘렀습니다.\n 아마 어딘가에는 맞지 않았을까요?")
                    break
                else:
                    print("기력이 부족합니다.")
            elif selection == "5":
                Field.status_monster()
                selection = input("공격할 대상을 지정하십시오. 왼쪽 몬스터부터 1, 2, 3... 번째 몬스터입니다.")  
                index = int(selection) - 1 

                target = Field.return_monsters_all()[index]
                hero.instant_death(target)
                print( f"당신은 {target.name} 에게 즉사의 저주를 겁니다.\n" +
                       f"{target.name}을 쓰러트렸습니다.")

                break
            elif selection == "6" :
                break
            elif selection == "7" :
                print("당신은 치트키를 사용하다가 실수로 자신을 지정하였습니다.")
                hero.hp = 1
                break
            elif selection == "8":
                probability = probability[1:10]
                probability.append(1)
                hero.harm = hero.harm + 2
                break
            elif selection == "9":
                monster_cls_list = [Slime, Zombie, Skeleton]
                random_moster = random.choice(monster_cls_list)
                if random_moster == Slime:
                    slime = random.randint(50, 101)
                    hero.hp = hero.hp + slime/2
                    print(f"슬라임을 소환합니다. 고동효 중2 회복술을 사용해 슬라임을 희생시키고 {slime/2}만큼의 체력을 회복했습니다.")
                elif random_moster == Zombie:
                    zombie = random.randint(150, 201)
                    hero.hp = hero.hp + zombie/2
                    print(f"좀비를 소환합니다. 고동효 중2 회복술을 사용해 좀비를 희생시키고 {zombie/2}만큼의 체력을 회복했습니다.")
                elif random_moster == Skeleton:
                    skeleton = random.randint(175, 201)
                    hero.hp = hero.hp + skeleton/2
                    print(f"스켈레톤을 소환합니다. 고동효 중2 회복술을 사용해 스켈레톤을 희생시키고 {skeleton/2}만큼의 체력을 회복했습니다.")
                break
            elif selection == "10":
                print("철옹성을 사용합니다. 총 80의 피해를 흡수하는 방어막을 얻었습니다.")
                shield.is_alive = True
                break

                
        if selection == "6":
            continue
    elif selection == "2":
        print("당신은 있는 힘껏 도망쳤습니다.")
        is_success = random.choice(probability)
        if is_success == 0:
            print("하지만 그들이 더 빨랐습니다.")
            print("도주는 실패한 듯 합니다...")
        if is_success == 1:
            print("당신은 도망치는데 성공했고, 무사히 탈출했습니다.")
            print("[[ENDING 2 : 탈출]]")
            break
    elif selection == "3":
        print("당신은 조심스레 바닥에 검을 놓고, 투항 의사를 밝혔습니다.")
        print("물론, 한국어로 말이죠.")
        hero.get_damage(hero.hp + 10000)
    
    ## monster attack section
    print("이제 몬스터들이 공격합니다...")
    for monster in Field.return_monsters_all():
        print(f"{monster.name} 이 당신에게 {monster.harm} 만큼의 피해를 입힙니다!")
        monster.basic_attack(hero)
    
    if shield.is_alive == True:
        monster_list:list[Body] = Field.opponent_field
        Monster_cumulative_damage = []
        for i in range(len(monster_list)):
            body = monster_list[i]
            Monster_cumulative_damage.append(body.harm)
            damage = sum(Monster_cumulative_damage)
        if damage <= shield.hp:
            shield.get_damage(damage)
            print(f"방어막이 {damage}만큼 피해를 대신 입었습니다.")
            print(f"남은 방어막 {shield.hp}")
            hero.hp = hero.hp + damage
        elif damage > shield.hp:
            shield.get_damage(damage)
            print(f"방어막이 {shield.hp + damage} 만큼의 데미지를 받아내고 파괴되었습니다.")
            hero.hp = hero.hp + shield.hp + damage
            print(f" {-shield.hp} 만큼의 데미지를 입습니다.")

    ## alive check section
    monster_list:list[Body] = Field.opponent_field
    pop_index_list = [] # alive check 가 끝나고 난 뒤의 리스트
    for i in range(len(monster_list)):
        body = monster_list[i]
        if body.name == "중슬":
            if body.is_alive == False:
                pop_index_list.append(Slime())
                pop_index_list.append(Slime())
        if body.name == "폭박":
            if body.is_alive == False:
                print("폭탄 박쥐가 자폭하며 당신에게 10 만큼의 피해를 입힙니다!")
                hero.get_damage(10)
        if body.is_alive:
            pop_index_list.append(body)
        
    monster_list.clear()
    monster_list += pop_index_list
    
    

    
    if not hero.is_alive:
        print("당신은 사망했습니다.")
        print("[[ENDING 1 : 게임 오버]]")
        break
    
    if len(monster_list) == 0:
        print("당신은 모든 몬스터를 물리쳤습니다.")
        print("드디어 가던 길을 갈 수 있겠군요!")
        print("[[게임 승리!]]")
        print("[[ENDING 0 : 승리!]]")
        break

    print()
    print()
    print("시간이 흐르고, 모두가 숨을 가다듬었습니다. 다음 턴이 시작됩니다...")
    print()
    print()