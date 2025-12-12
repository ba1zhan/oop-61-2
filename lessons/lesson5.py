#Методы класса
#Статистический метод (@staticmethod)

class Math:

    @staticmethod
    def add(a, b):
        return a + b

print(Math.add(12, 23))


#2. Метод класса (@classmethod)

class User:

    default_role = "guest"

    def __init__(self, name, role):
        self.name = name
        self.role = role


    @classmethod
    def create_from_name(cls, name):
        return cls(name, cls.default_role)

    @classmethod
    def det_base_role(cls):
        return cls.default_role

    def get_name(self):
        return self.name

user1 = User.create_from_name("User")
ardager = User("baizhan", "hacker")


# print(user1.role)
# print(ardager.role)



