class Phone:
    def __init__(self, model, storage, battery):
        self.model = model
        self.storage  = storage
        self.battery = battery
        self.is_on = False

    def power_on(self):
        if not self.is_on:
            self.is_on = True
            return f"{self.model} включился."
        return f"{self.model} уже был включён."

    def charge(self, amount):
        self.battery += amount
        if self.battery > 100:
            self.battery = 100
        return f"{self.model} теперь заряжен на {self.battery}%."

    def info(self):
        """Информация о телефоне"""
        status = "включён" if self.is_on else "выключен"
        return (
            f"Телефон {self.model}: память {self.storage} ГБ, "
            f"заряд {self.battery}%, состояние — {status}"
        )

phone1 = Phone("iPhone 14", 128, 45)
phone2 = Phone("Samsung Galaxy S23", 256, 80)
phone3 = Phone("Xiaomi Redmi 12", 64, 10)

print(phone1.info())
print(phone1.power_on())
print(phone1.charge(40))
print(phone1.info())

print("\n" + phone2.info())
print(phone2.power_on())
print(phone2.charge(15))

print("\n" + phone3.info())
print(phone3.power_on())
print(phone3.charge(70))
print(phone3.info())
