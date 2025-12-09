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
        return self.hero.lvl * 10

    def __str__(self):
        return f"{self.hero.name} | Баланс: {self._balance} SOM"

    def __add__(self, other):
        if type(self.hero) != type(other.hero):
            raise TypeError("Нельзя складывать счета героев разных классов!")
        return self._balance + other.balance

    def __eq__(self, other):
        return self.hero.name == other.hero.name and self.hero.level == other.hero.level



class SmsService:
    def send_otp(self, phone):
        pass


class KGSms(SmsService):
    def send_otp(self, phone):
        opt = 1234
        return f"<text>Код: {opt} </text><phone>{phone}</phone>"

class RUSms(SmsService):
    def send_otp(self, phone):
        otp = 1234
        return {"text": f"Код: {otp}", "phone": phone}

mage1 = MageHero("Merlin", 80, 500, 150)
mage2 = MageHero("Merlin", 80, 500, 200)
warrior = WarriorHero("Conan", 50, 900, 20)

acc1 = BankAccount(mage1, 5000, "1234", "Simba")
acc2 = BankAccount(mage2, 3000, "0000", "Simba")
acc3 = BankAccount(warrior, 2500, "1111", "Simba")

print(mage1.action())
print(warrior.action())

print(acc1)
print(acc2)

print("Банк:", acc1.get_bank_name())

sms = KGSms()
print(sms.send_otp("+996777123456"))