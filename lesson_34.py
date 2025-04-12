"""
Lesson 34: Поведенческие паттерны проектирования
- Состояние музыкальный плеер
"""

from abc import ABC, abstractmethod

class AbstractState(ABC):
    """
    Абстрактный класс состояния.
    """
    
    @abstractmethod
    def press_play(self):
        """
        Метод для обработки нажатия кнопки "Play".
        """
        pass
    
    @abstractmethod
    def press_pause(self):
        """
        Метод для обработки нажатия кнопки "Pause".
        """
        pass
    
    @abstractmethod
    def press_stop(self):
        """
        Метод для обработки нажатия кнопки "Stop".
        """
        pass


class PlayingState(AbstractState):
    """
    Класс состояния "Воспроизведение".
    """
    
    def __init__(self, player):
        self.player = player
    
    def press_play(self):
        print("Музыка уже играет.")
    
    def press_pause(self):
        print("Пауза.")
        self.player.set_state(PausedState(self.player))
    
    def press_stop(self):
        print("Стоп.")
        self.player.set_state(StoppedState(self.player))


class PausedState(AbstractState):
    """
    Класс состояния "Пауза".
    """
    
    def __init__(self, player):
        self.player = player
    
    def press_play(self):
        print("Продолжение воспроизведения.")
        self.player.set_state(PlayingState(self.player))
    
    def press_pause(self):
        print("Музыка уже на паузе.")
    
    def press_stop(self):
        print("Стоп.")
        self.player.set_state(StoppedState(self.player))


class StoppedState(AbstractState):
    """
    Класс состояния "Стоп".
    """
    
    def __init__(self, player):
        self.player = player
    
    def press_play(self):
        print("Воспроизведение начато.")
        self.player.set_state(PlayingState(self.player))
    
    def press_pause(self):
        print("Музыка остановлена. Невозможно поставить на паузу.")
    
    def press_stop(self):
        print("Музыка уже остановлена.")



class MusicPlayer:
    """
    Класс музыкального плеера.
    """
    
    def __init__(self):
        self.state = StoppedState(self)
    
    def set_state(self, state: AbstractState):
        """
        Установка нового состояния.
        """
        self.state = state
    
    def press_play(self):
        self.state.press_play()
    
    def press_pause(self):
        self.state.press_pause()
    
    def press_stop(self):
        self.state.press_stop()


if __name__ == "__main__":
    player = MusicPlayer()
    
    player.press_play()  # Воспроизведение начато.
    player.press_pause()  # Пауза.
    player.press_play()  # Продолжение воспроизведения.
    player.press_stop()  # Стоп.
    player.press_pause()  # Музыка уже на паузе.
    player.press_stop()  # Музыка уже остановлена.
    player.press_play()  # Воспроизведение начато.
    player.press_stop()  # Стоп.