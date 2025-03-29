# Lesson 30 SOLID
# SOLID - 5 принципов ООП
# 1. Single Responsibility Principle (Принцип единственной ответственности)
# 2. Open/Closed Principle (Принцип открытости/закрытости)
# 3. Liskov Substitution Principle (Принцип подстановки Барбары Лисков)
# 4. Interface Segregation Principle (Принцип разделения интерфейса)
# 5. Dependency Inversion Principle (Принцип инверсии зависимостей)


# 2. Open/Closed Principle (Принцип открытости/закрытости)
# классы и модули должны быть открыты для расширения, но закрыты для модификации. 
#  код, зависящий от базовых абстракций, остаётся неизменным, а новый код расширяет функциональность. 

# 3. Liskov Substitution Principle (Принцип подстановки Барбары Лисков)
# объекты в программе должны быть заменяемы экземплярами их подтипов без изменения правильности выполнения программы.

from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import List
from uuid import UUID
import logging

# Настраиваем логгер для отслеживания платежных операций
logger = logging.getLogger(__name__)


@dataclass
class Product:
    """Класс для представления товара в магазине."""
    name: str
    price: float
    quantity: int


@dataclass
class Order:
    """Класс для представления заказа покупателя."""
    order_id: UUID
    items: List[Product]
    
    def get_total_amount(self) -> float:
        """Рассчитывает общую сумму заказа."""
        return sum(item.price * item.quantity for item in self.items)


class PaymentProcessor(ABC):
    """
    Абстрактный базовый класс для обработки платежей.
    
    Этот класс определяет интерфейс, который должны реализовать все
    конкретные процессоры платежей. Он закрыт для модификации, но система
    открыта для расширения через создание новых классов-обработчиков.
    """
    
    @abstractmethod
    def process_payment(self, order: Order, payment_data: dict) -> bool:
        """
        Обрабатывает платёжную операцию для заказа.
        
        Args:
            order: Заказ для оплаты
            payment_data: Словарь с данными для проведения платежа
            
        Returns:
            bool: True если платёж успешно обработан, иначе False
        """
        pass


class YandexPaymentProcessor(PaymentProcessor):
    """Процессор платежей для Яндекс.Кассы."""
    
    def process_payment(self, order: Order, payment_data: dict) -> bool:
        """
        Реализует обработку платежа через Яндекс.Кассу.
        
        Args:
            order: Заказ для оплаты
            payment_data: Словарь с данными для проведения платежа, должен содержать
                         'yandex_token' и 'return_url'
        """
        # Здесь был бы реальный код интеграции с API Яндекс.Кассы
        logger.info(f"Обработка платежа через Яндекс.Кассу для заказа {order.order_id}")
        logger.debug(f"Сумма платежа: {order.get_total_amount()} руб.")
        
        # Имитация обработки платежа
        if "yandex_token" not in payment_data:
            logger.error("Отсутствует токен для Яндекс.Кассы")
            return False
            
        # В реальном коде здесь был бы API-запрос
        print(f"Платеж на сумму {order.get_total_amount()} руб. через Яндекс.Кассу выполнен успешно!")
        return True


class PayPalProcessor(PaymentProcessor):
    """Процессор платежей для PayPal."""
    
    def process_payment(self, order: Order, payment_data: dict) -> bool:
        """
        Реализует обработку платежа через PayPal.
        
        Args:
            order: Заказ для оплаты
            payment_data: Словарь с данными платежа, должен содержать
                         'paypal_email' и 'paypal_token'
        """
        # Здесь был бы реальный код интеграции с API PayPal
        logger.info(f"Обработка платежа через PayPal для заказа {order.order_id}")
        logger.debug(f"Сумма платежа: {order.get_total_amount()} USD")
        
        if "paypal_email" not in payment_data:
            logger.error("Отсутствует email для PayPal")
            return False
            
        # В реальном коде здесь был бы API-запрос
        print(f"Платеж на сумму {order.get_total_amount()} USD через PayPal выполнен успешно!")
        return True


# Вот тут магия OCP! Добавляем новую платежную систему без изменения существующего кода
class StripeProcessor(PaymentProcessor):
    """Процессор платежей для Stripe."""
    
    def process_payment(self, order: Order, payment_data: dict) -> bool:
        """
        Реализует обработку платежа через Stripe.
        
        Args:
            order: Заказ для оплаты
            payment_data: Словарь с данными платежа, должен содержать
                         'stripe_api_key' и 'card_token'
        """
        logger.info(f"Обработка платежа через Stripe для заказа {order.order_id}")
        
        if "stripe_api_key" not in payment_data or "card_token" not in payment_data:
            logger.error("Отсутствуют необходимые данные для Stripe")
            return False
            
        # В реальном коде здесь был бы API-запрос к Stripe
        print(f"Платеж на сумму {order.get_total_amount()} USD через Stripe выполнен успешно!")
        return True


# Класс для проведения платежей, который использует принцип открытости/закрытости
class PaymentService:
    """
    Сервис для обработки платежей с использованием различных платежных систем.
    
    Этот класс не нужно модифицировать при добавлении новых платежных систем.
    Просто создайте новый класс, реализующий интерфейс PaymentProcessor.
    """
    
    def __init__(self):
        # Словарь доступных процессоров платежей
        self.payment_processors = {}
        
    def register_processor(self, payment_type: str, processor: PaymentProcessor):
        """
        Регистрирует новый процессор платежей.
        
        Args:
            payment_type: Строковый идентификатор типа платежа
            processor: Экземпляр процессора платежей
        """
        self.payment_processors[payment_type] = processor
        
    def process_payment(self, payment_type: str, order: Order, payment_data: dict) -> bool:
        """
        Обрабатывает платеж, используя соответствующий процессор.
        
        Args:
            payment_type: Тип платежа (например, "yandex", "paypal", "stripe")
            order: Заказ для оплаты
            payment_data: Данные для обработки платежа
            
        Returns:
            bool: True, если платеж успешно обработан, иначе False
            
        Raises:
            ValueError: Если указан неподдерживаемый тип платежа
        """
        if payment_type not in self.payment_processors:
            raise ValueError(f"Неподдерживаемый тип платежа: {payment_type}")
            
        processor = self.payment_processors[payment_type]
        return processor.process_payment(order, payment_data)


# Пример использования
if __name__ == "__main__":
    # Создаем заказ
    products = [
        Product("Пельмени Сибирские", 320.0, 2),
        Product("Вареники с вишней", 290.0, 1)
    ]
    order = Order(UUID('12345678-1234-5678-1234-567812345678'), products)
    
    # Настраиваем сервис платежей
    payment_service = PaymentService()
    payment_service.register_processor("yandex", YandexPaymentProcessor())
    payment_service.register_processor("paypal", PayPalProcessor())
    payment_service.register_processor("stripe", StripeProcessor())
    
    # Проводим платеж через Яндекс.Кассу
    yandex_payment_data = {
        "yandex_token": "yandex_secure_token_123",
        "return_url": "https://morozko-pelmeni.ru/success"
    }
    payment_service.process_payment("yandex", order, yandex_payment_data)
    
    # Проводим платеж через PayPal
    paypal_payment_data = {
        "paypal_email": "customer@example.com",
        "paypal_token": "paypal_secure_token_456"
    }
    payment_service.process_payment("paypal", order, paypal_payment_data)
    
    # Проводим платеж через новую платежную систему Stripe, не меняя ни строчки
    # в PaymentService или существующих процессорах платежей
    stripe_payment_data = {
        "stripe_api_key": "sk_test_stripe_key_789",
        "card_token": "tok_visa"
    }
    payment_service.process_payment("stripe", order, stripe_payment_data)