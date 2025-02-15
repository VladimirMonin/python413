"""
15.02.2025
Python: ООП. Ч1. Атрибуты и методы. Класс и экземпляр. Практика. Урок: 22
- class
- нейминг классов UpperCamelCase
- атрибут класса
- __init__ - инициализатор
- self - ссылка на экземпляр класса
- __new__ - как скрытая часть конструктора
- методы работающие с self - методы экземпляра
- документация класса и методов
"""

# Класс объявление
class AdPost:
    promote_rate: float = 0.1 # 0.005
    
    def __init__(self, title: str, text: str, price: int):
        self.title = title
        self.text = text
        self.price = price
        # self.promote_rate: float = 0.5


    def __str__(self) -> str:
        return f"Класс {self.__class__.__name__}: Заголовок: {self.title}, Текст: {self.text[:20]}, Цена: {self.price}"
    
    def calculate_promote_cost(self, day:int) -> int:
        promote_cost = int(self.price * (self.promote_rate / 100) * day)
        return promote_cost
    
    @staticmethod
    def get_peak_hours() -> tuple:
        """
        Метод возвращающий часы пик для размещения рекламы.
        :return: Кортеж с часами пик.
        """
        return 13,14,15
    
    @classmethod
    def get_promote_rate(cls) -> float:
        """
        Метод возвращающий текущий процент рекламы.
        :return: Процент рекламы.
        """
        return cls.promote_rate
    
    @classmethod
    def set_promote_rate(cls, rate: float) -> None:
        """
        Метод устанавливающий новый процент рекламы.
        :param rate: Процент рекламы.
        """
        cls.promote_rate = rate
    
ap1 = AdPost("Sony Playstation 5. Муха не сидела!", "Новая, красивая, блестящая...!", 20000)
ap2 = AdPost("Видеокарта RTX 3090", "В компьютере стоявшая, майнинга не видавшая, отвертки не ведавшая. Как новая!", 60000)

AdPost.promote_rate = 1

print(ap1)
print(ap2)
print(ap1.calculate_promote_cost(3))
print(ap2.calculate_promote_cost(3))

print(AdPost.get_peak_hours())
print(AdPost.get_promote_rate())
AdPost.set_promote_rate(5)
print(AdPost.get_promote_rate())
