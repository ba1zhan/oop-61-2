class User:
    def __init__(self, username, role):
        self.username = username
        self.role = role

PERMISSIONS = {
    "admin": ["start", "ban", "stop"],
    "user": ["start", "message"]
}

def check_permission(command_name):
    def decorator(func):
        def wrapper(self, user):
            if command_name not in PERMISSIONS.get(user.role, []):
                print(f' Пользователь {user.username} не может выполнять команду "{command_name}"')
                return
            print(f'Пользователь {user.username} ({user.role}) выполняет команду {command_name}')
            func(self, user)
        return wrapper
    return decorator


class CommandHandler:

    @check_permission("start")
    def start(self, user):
        print(" Система запущена")

    @check_permission("ban")
    def ban(self, user):
        print(" Пользователь заблокирован")

    @check_permission("stop")
    def stop(self, user):
        print(" Система остановлена")

    @check_permission("message")
    def message(self, user):
        print(f' Пользователь {user.username} отправил сообщение')



if __name__ == "__main__":
    admin = User("baizhan", "admin")
    user = User("danislam", "user")

    handler = CommandHandler()

    handler.start(admin)
    handler.ban(admin)
    handler.stop(admin)

    print()

    handler.start(user)
    handler.ban(user)
    handler.message(user)


# def log_action(func):
#     def wrapper(*args, **kwargs):
#         print(f"📌 Выполняется операция: {func.__name__}")
#         return func(*args, **kwargs)
#     return wrapper
#
# class BankAccount:
#     bank_name = "Python Bank"
#     total_accounts = 0
#
#     def __init__(self, owner, balance):
#         self.owner = owner
#         self.balance = balance
#         BankAccount.total_accounts += 1
#
#     @log_action
#     def deposit(self, amount):
#         self.balance += amount
#         print(f"Баланс {self.owner}: {self.balance}")
#
#     @classmethod
#     def get_total_accounts(cls):
#         print(f"Всего счетов в банке: {cls.total_accounts}")
#
#     @staticmethod
#     def is_valid_amount(amount):
#         return amount > 0
#
# account1 = BankAccount("baizhan", 1000)
# account2 = BankAccount("danislam", 500)
#
# account1.deposit(300)
# account2.deposit(200)
#
# BankAccount.get_total_accounts()
#
# print(BankAccount.is_valid_amount(100))
# print(BankAccount.is_valid_amount(-50))
