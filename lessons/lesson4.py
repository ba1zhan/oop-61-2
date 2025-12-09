class Hero:
    def __init__(self, name: str, hp: int, lvl: int):
        self.name = name
        self.hp = hp
        self.lvl = lvl

    def base_action(self):
        return f"{self.name} готов к бою!!!"

class MageHero(Hero):
    def __init__(self, name, hp, lvl, mp: int):
        super().__init__(name, hp, lvl)
        self.mp = mp

    def cast_spell(self):
        return f"Маг {self.name} кастует заклинание!!! Mp: {self.mp}"

class WarriorHero(MageHero):
    def attack(self):
        return f"Воин {self.name} рубит мечом!!! Уровень: {self.lvl}"

Gon = Hero("Gon", 10000, 10000)
Gojo = MageHero("Gojo", 10001, 11110, 100000)
Naruto = WarriorHero("Thorfinn", 1000, 1011, 50000)

print(Gon.name)
print(Gojo.name)
print(Naruto.name)




class BankAccount:
    def __init__(self, hero, bank_name, balance, password):
        self.hero = hero
        self.bank_name = bank_name
        self._balance = balance
        self.password = password

    def login(self, password):
        return password == self.password

    def get_bank_name(self):
        return self.bank_name

    def bonus_for_level(self):
        return self.bank_name