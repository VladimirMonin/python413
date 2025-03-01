"""
Тема: ООП Ч3. Инкапсуляция. Приватные методы и атрибуты. Урок: 24
Два уровня сокрытия
_ это protected - досупно при наследовании
__ это private - доступно только внутри класса

Собственные getters и setters
@property
@speed.setter
@speed.deleter

"""

data = people = [
    {"first_name": "Олег", "middle_name": "Дмитриевич", "last_name": "Агеев"},
    {"first_name": "Дмитрий", "middle_name": "Витальевич", "last_name": "Аносов"},
    {"first_name": "Кирилл", "middle_name": "Алексеевич", "last_name": "Борсуков"},
    {"first_name": "Алексей", "middle_name": "Леонидович", "last_name": "Бревнов"},
    {"first_name": "Александр", "middle_name": "Сергеевич", "last_name": "Бугаев"},
    {"first_name": "Андрей", "middle_name": "Васильевич", "last_name": "Быстревский"},
    {"first_name": "Ильдар", "middle_name": "Расимович", "last_name": "Гайсин"},
    {"first_name": "Андрей", "middle_name": "Юрьевич", "last_name": "Головатов"},
    {"first_name": "Никита", "middle_name": "Алексеевич", "last_name": "Григорьев"},
    {"first_name": "Даши", "middle_name": "Дашибаевич", "last_name": "Доржиев"},
    {"first_name": "Сергей", "middle_name": "Сергеевич", "last_name": "Киевец"},
    {"first_name": "Никита", "middle_name": "Владимирович", "last_name": "Котельников"},
    {"first_name": "Анна", "middle_name": "Алексеевна", "last_name": "Криштоб"},
    {"first_name": "Никита", "middle_name": "Андреевич", "last_name": "Крюков"},
    {"first_name": "Алексей", "middle_name": "Михайлович", "last_name": "Лапшин"},
    {"first_name": "Егор", "middle_name": "Олегович", "last_name": "Мосин"},
    {"first_name": "Даниил", "middle_name": "Витальевич", "last_name": "Отчин"},
]


# pip install tabulate
from tabulate import tabulate
from typing import List, Dict, Union, Any, Optional


class TabulateTable:

    __awaitable_styles = [
        "plain",
        "simple",
        "github",
        "grid",
        "simple_grid",
        "rounded_grid",
        "heavy_grid",
        "mixed_grid",
        "double_grid",
        "fancy_grid",
        "outline",
        "simple_outline",
        "rounded_outline",
        "heavy_outline",
        "mixed_outline",
        "double_outline",
        "fancy_outline",
        "pipe",
        "orgtbl",
        "asciidoc",
        "jira",
        "presto",
        "pretty",
        "psql",
        "rst",
        "mediawiki",
        "moinmoin",
        "youtrack",
        "html",
        "unsafehtml",
        "latex",
        "latex_raw",
        "latex_booktabs",
        "latex_longtable",
        "textile",
        "tsv",
    ]

    def __init__(self):
        self.__data: Union[List[Dict[str, Any]], List[List[Any]]] = []
        self.__style: str = "pretty"
        self.__headers: Optional[List[str]] = None
        self.__type_data: Optional[str] = None

    @property
    def style(self):
        return self.__style

    @style.setter
    def style(self, style: str):
        if style in self.__awaitable_styles:
            self.__style = style
        else:
            raise ValueError(f"Такого стиля нет. Выберите из {self.__awaitable_styles}")

    @property
    def data(self) -> List[Dict[str, Any]] | List[List[Any]]:
        return self.__data

    @data.setter
    def data(self, data: Union[List[Dict[str, Any]], List[List[Any]]]):
        self.__type_data = self.__validate_data(data)
        self.__data = data

    def __validate_data(self, data: Union[List[Dict[str, Any]], List[List[Any]]]):
        """
        Метод проверят, что данные для таблицы являются либо списком списков либо список словарей
        Возвращает "lists" если список списков и "dicts" если список словарей
        Или вызывает исключение ValueError
        """
        if isinstance(data[0], dict):
            return "dicts"
        elif isinstance(data[0], list):
            return "lists"
        else:
            raise ValueError(
                "Данные для таблицы должны быть списком списков или списком словарей"
            )

    def render(self) -> str:
        """
        Метод отрисовывает таблицу в текстовом виде
        Возвращает строку с таблицей
        """
        if self.__type_data == "dicts":
            return tabulate(self.__data, headers="keys", tablefmt=self.__style)
        elif self.__type_data == "lists":
            return tabulate(self.__data, tablefmt=self.__style)
        else:
            raise ValueError("Данные для таблицы не заданы или имеют неверный формат")


if __name__ == "__main__":
    table = TabulateTable()
    table.data = data
    table.style = "html"
    print(table.render())
