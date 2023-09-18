# 연습 문제

"""
    게임에서 캐릭터는 구현할 예정입니다. 아래 클래스를 적절하게 조합하여
    만들어주세요
    
    Body
    Weapon
    WeaponEnchant (강화)
    Skill
    Equipment (장착)
    Role (히어로 인지, 빌런인지, 몹인지)
"""

from dataclasses import dataclass, field


@dataclass
class Equipment:
    pass


@dataclass
class Enchant:
    enchant_count: int = 0

    def enchant(self):
        self.enchant_count += 1


@dataclass
class Weapon(Equipment, Enchant):
    name: str = None
    damage: int = 0


@dataclass
class Armor(Equipment, Enchant):
    name: str = None


@dataclass
class Skill:
    name: str
    damage: int


@dataclass
class Body:
    weapon: Weapon
    armor: Armor
    hp: int = 10
    mp: int = 10

    def change_weapon(self, weapon: Weapon):
        self.weapon = weapon

    def change_armor(self, armor: Armor):
        self.armor = armor


@dataclass
class Character(Body):
    role: str = None
    skill: list[Skill] = field(
        default_factory=list,
    )

    def attack(self):
        print(f"{self.role}가 {self.weapon.damage} 데미지로 공격합니다.")

    def use_skill(self, skill_name: str):
        print(
            f"{self.role}가 스킬 {self.skill[skill_name].name}을 사용하여 {self.skill[skill_name].damage}의 데미지를 입혔습니다."
        )


if __name__ == "__main__":
    화염방사기 = Weapon(name="화염방사기", damage=100)
    철갑옷 = Armor(name="철갑옷")
    스킬: list[Skill] = [Skill("화염구", 1000), Skill("얼음구", 1000)]

    character = Character(role="히어로", weapon=화염방사기, armor=철갑옷, skill=스킬)
    character.attack()
    character.use_skill("화염구")

    print(character)
    character.weapon.enchant()
    character.armor.enchant()

    print(character)
