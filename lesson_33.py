"""
Lesson 33 - Паттерны проектирования на ООП
- Абстрактная фабрика
- Прокси
- Адаптер
"""

"""
Адаптер Платежных Систем
- Клиент - приложение для заказа еды
- Интерфейс - интерфейс платежной системы (Абстрактный класс предписывающий методы для работы с платежами)
- Адаптер - адаптер для работы с конкретной платежной системой (например, ЯндексКасса или Робокасса)
- Платежная система - конкретная реализация платежной системы (например, ЯндексКасса или Робокасса)
"""

from abc import ABC, abstractmethod
from typing import Any

class YandexPaymentSystem:
    """
    Имитация платежной системы Яндекс.Касса.
    На схеме это Adaptee.
    """

    def yandex_payment(self, amount: float) -> str:
        """
        Имитация платежа через Яндекс.Кассу.
        """
        return f"Оплата {amount} руб. через Яндекс.Кассу успешно выполнена."
    

class RobokassaPaymentSystem:
    """
    Имитация платежной системы Робокасса.
    На схеме это Adaptee.
    """
    
    def robokassa_payment(self, amount: float, currency: str) -> str:
        """
        Имитация платежа через Робокассу.
        """
        return f"Оплата {amount} {currency} через Робокассу успешно выполнена."
    

class AbstractPaymentSystem(ABC):
    """
    Абстрактный класс платежной системы.
    На схеме это Target.
    """
    
    @abstractmethod
    def pay(self, amount: float) -> str:
        """
        Абстрактный метод для выполнения платежа.
        """
        pass

class YandexPaymentAdapter(AbstractPaymentSystem):
    """
    Адаптер для работы с Яндекс.Кассой.
    На схеме это Adapter.
    """
    
    def __init__(self, yandex_payment_system: YandexPaymentSystem):
        self.yandex_payment_system = yandex_payment_system
    
    def pay(self, amount: float) -> str:
        """
        Выполнение платежа через Яндекс.Кассу.
        """
        return self.yandex_payment_system.yandex_payment(amount)
    

class RobokassaPaymentAdapter(AbstractPaymentSystem):
    """
    Адаптер для работы с Робокассой.
    На схеме это Adapter.
    """
    available_currencies = ["RUB", "USD", "EUR"]
    
    def __init__(self, robokassa_payment_system: RobokassaPaymentSystem):
        self.robokassa_payment_system = robokassa_payment_system

    def __validate_currency(self, currency: str) -> bool:
        """
        Проверка доступности валюты.
        """
        return currency in self.available_currencies
    
    def pay(self, amount: float) -> str:
        """
        Выполнение платежа через Робокассу.
        """
        currency_input = input("Введите валюту платежа: ")
        
        if not self.__validate_currency(currency_input):
            raise ValueError(f"Валюта {currency_input} недоступна. Доступные валюты: {', '.join(self.available_currencies)}")
        
        return self.robokassa_payment_system.robokassa_payment(amount, currency_input)
    

class PaymentFacade:
    """
    Фасад для работы с платежными системами.
    На схеме это Facade.
    """
    
    def __init__(self):
        self.yandex_payment_system = YandexPaymentSystem()
        self.robokassa_payment_system = RobokassaPaymentSystem()
        self.yandex_adapter = YandexPaymentAdapter(self.yandex_payment_system)
        self.robokassa_adapter = RobokassaPaymentAdapter(self.robokassa_payment_system)
    
    def pay_with_yandex(self, amount: float) -> str:
        """
        Выполнение платежа через Яндекс.Кассу.
        """
        return self.yandex_adapter.pay(amount)
    
    def pay_with_robokassa(self, amount: float) -> str:
        """
        Выполнение платежа через Робокассу.
        """
        return self.robokassa_adapter.pay(amount)
    
    def __call__(self, amount: float, payment_system: str) -> str:
        """
        Выполнение платежа через выбранную платежную систему.
        """
        if payment_system == "yandex":
            return self.pay_with_yandex(amount)
        elif payment_system == "robokassa":
            return self.pay_with_robokassa(amount)
        else:
            raise ValueError(f"Неизвестная платежная система: {payment_system}")


if __name__ == "__main__":
    payment_facade = PaymentFacade()
    
    try:
        print(payment_facade(1000, "yandex"))
        print(payment_facade(2000, "robokassa"))
    except ValueError as e:
        print(e)