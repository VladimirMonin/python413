"""
Lesson 32 
05.04.2025
Порождаюющие паттерны проектирования
Паттерн Singleton
Паттерн Prototype
"""

from abc import ABC, abstractmethod
from copy import deepcopy


class AbstractCharacter(ABC):
    """
    Абстрактный класс для персонажа.
    """
    @abstractmethod
    def clone(self):
        pass

class Warrior(AbstractCharacter):
    """
    Класс для создания персонажа-воителя.
    """
    def __init__(self, name: str, health: int, mana: int):
        self.name = name
        self.health = health
        self.mana = mana
    
    def clone(self):
        """
        Метод для клонирования персонажа.
        """
        return deepcopy(self)
    

class Mage(AbstractCharacter):
    """
    Класс для создания персонажа-мага.
    """
    def __init__(self, name: str, health: int, mana: int):
        self.name = name
        self.health = health
        self.mana = mana
    
    def clone(self):
        """
        Метод для клонирования персонажа.
        """
        return deepcopy(self)
    

class CharRegistry:
    """
    Реестр персонажей.
    """
    def __init__(self):
        self._characters = {}
    
    def register_character(self, name: str, character: AbstractCharacter):
        """
        Метод для регистрации персонажа.
        """
        self._characters[name] = character
    
    def clone_character(self, name: str) -> AbstractCharacter:
        """
        Метод для клонирования персонажа.
        """
        character = self._characters.get(name)
        if character is None:
            raise ValueError(f"Персонаж {name} не зарегистрирован.")
        return character.clone()
    
    def get_available_characters(self):
        """
        Метод для получения доступных персонажей.
        """
        return list(self._characters.keys())
    
# Пример использования
if __name__ == "__main__":
    # Создаем реестр персонажей
    registry = CharRegistry()
    
    # Регистрируем персонажей
    warrior = Warrior(name="Warrior", health=100, mana=50)
    mage = Mage(name="Mage", health=80, mana=100)
    
    registry.register_character("Warrior", warrior)
    registry.register_character("Mage", mage)
    
    # Клонируем персонажей
    cloned_warrior = registry.clone_character("Warrior")
    cloned_mage = registry.clone_character("Mage")
    
    print(f"Клонированный воитель: {cloned_warrior.name}, здоровье: {cloned_warrior.health}, мана: {cloned_warrior.mana}")
    print(f"Клонированный маг: {cloned_mage.name}, здоровье: {cloned_mage.health}, мана: {cloned_mage.mana}")