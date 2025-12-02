class Hero:
#конструктор класса
    def __init__(self, name, lvl, hp):
        self.name = name
        self.lvl = lvl
        self.hp = hp

    def base_method(self):
        return f"base action {self.name}"

kirito = Hero('Kirito', 100, 1000)
asuna = Hero('Asuna', 101,1001)