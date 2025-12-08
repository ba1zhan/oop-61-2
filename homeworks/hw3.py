class Product:
    def __init__(self, name, price):
        self.name = name
        self._price = price
        self.__discount = 0

    def get_price(self):
        """Возвращает цену с учётом текущей скидки"""
        discount_multiplier = (100 - self.__discount) / 100
        return self._price * discount_multiplier

    def set_discount(self, percent):
        """Устанавливает скидку, только если она не больше 50%"""
        if percent < 0:
            percent = 0
        if percent > 50:
            print("Ошибка: скидка не может быть больше 50%!")
            return
        self.__discount = percent
        print(f"Скидка установлена: {percent}%")

    def apply_extra_discount(self, secret_code):
        """Приватный метод для VIP-кода"""
        if secret_code == "VIP123":
            current_price = self.get_price()
            self._price = current_price * 0.95
            print("VIP-код принят! Дополнительная скидка 5% применена.")
        else:
            print("Неверный код")

    def __str__(self):
        return f"Product({self.name}, базовая цена: {self._price}, скидка: {self.__discount}%)"


print("=== Задача 1: Инкапсуляция ===")
p = Product("Iphone", 1000)
p.set_discount(20)
print("Цена со скидкой 20%:", p.get_price())        # 800.0

p.apply_extra_discount("VIP123")
print("Цена после VIP:", p.get_price())             # 760.0

p.apply_extra_discount("wrong")
print("Цена итоговая:", p.get_price())               # всё ещё 760.0

print("\n")


from abc import ABC, abstractmethod

class PaymentMethod(ABC):
    @abstractmethod
    def pay(self, amount):
        pass

    @abstractmethod
    def refund(self, amount):
        pass


class CardPayment(PaymentMethod):
    def pay(self, amount):
        print(f"Оплата картой: {amount}")

    def refund(self, amount):
        print(f"Возврат на карту: {amount}")


class CashPayment(PaymentMethod):
    def pay(self, amount):
        print(f"Оплата наличными: {amount}")

    def refund(self, amount):
        print(f"Возврат наличными: {amount}")


class CryptoPayment(PaymentMethod):
    def pay(self, amount):
        result = {
            "type": "crypto",
            "amount": amount,
            "currency": "USDT"
        }
        print(result)

    def refund(self, amount):
        result = {
            "type": "crypto_refund",
            "amount": amount,
            "currency": "USDT"
        }
        print(result)


class PaymentProcessor:
    def __init__(self, payment_method: PaymentMethod):
        self.payment_method = payment_method

    def process(self, amount):
        self.payment_method.pay(amount)

print("=== Задача 2: Абстракция ===")

processor = PaymentProcessor(CardPayment())
processor.process(100)

processor = PaymentProcessor(CashPayment())
processor.process(50)

processor = PaymentProcessor(CryptoPayment())
processor.process(200)