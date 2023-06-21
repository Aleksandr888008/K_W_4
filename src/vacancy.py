# -*- coding: utf-8 -*-
class Vacancy:
    """Класс с описанием вакансий"""

    __slots__ = ["__title", "__link", "__description", "__salary"]

    def __init__(self, title: str, link: str, description: str, salary: float) -> None:
        """Инициализируем описание вакансии основными характеристиками"""
        self.title = title                  # название
        self.link = link                    # ссылка
        self.description = description      # описание
        self.salary = salary                # зарплата

    @property
    def title(self):
        return self.__title

    @title.setter
    def title(self, title_value):
        if isinstance(title_value, str):
            self.__title = title_value

    @property
    def link(self):
        return self.__link

    @link.setter
    def link(self, link_value):
        if isinstance(link_value, str):
            self.__link = link_value

    @property
    def description(self):
        return self.__description

    @description.setter
    def description(self, description_value):
        if isinstance(description_value, str):
            self.__description = description_value

    @property
    def salary(self):
        return self.__salary

    @salary.setter
    def salary(self, salary_value):
        if isinstance(salary_value, float) or isinstance(salary_value, int) or salary_value is None:
            self.__salary = salary_value
        if salary_value is not None and salary_value < 0:
            self.__salary = 0

    def __repr__(self):
        return f"{self.__class__.__name__}({self.__slots__})"

    def __str__(self):
        return f"Вакансия {self.title} с зарплатой {self.salary}"

    def __gt__(self, other) -> bool:
        salary1 = 0 if self.salary is None else self.salary
        salary2 = 0 if other.salary is None else other.salary
        return salary1 > salary2

    def __lt__(self, other) -> bool:
        salary1 = 0 if self.salary is None else self.salary
        salary2 = 0 if other.salary is None else other.salary
        return salary1 < salary2
