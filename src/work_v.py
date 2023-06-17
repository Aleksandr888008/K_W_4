# -*- coding: utf-8 -*-
from abc import ABC, abstractmethod
from file_manager import FileManager
import json


class Work_vacancies(ABC):
    """ Класс для выполнения операций с множеством вакансий"""

    @abstractmethod
    def add_vacancy(self, vacancy):
        """Добавляет вакансию в файл"""
        pass

    @abstractmethod
    def search(self, query=None):
        """Выбирает данные из вакансий по критериям"""
        pass

    @abstractmethod
    def delete_vacancy(self, query=None):
        """Удаляет вакансию"""
        pass


class Vacancies(Work_vacancies, FileManager):
    """Основной класс для операций с вакансиями"""

    def add_vacancy(self, vacancy) -> None:
        """Добавляет вакансию в файл"""

        jobs_list = self.read_file(self.filename)
        jobs_list.append(vacancy)

        with open(self.filename, 'w', encoding='utf-8') as file:
            json.dump(jobs_list, file, indent=4, ensure_ascii=False)

    def search(self, query: dict = None) -> list:
        """Выбирает данные из вакансий по критериям"""
        jobs_list = self.read_file(self.filename)
        if not query:  # Нет критериев поиска, значит возвращаем все
            return jobs_list

        new_jobs_list = []
        for job in jobs_list:
            if all(job.get(key) == value for key, value in query.items()):
                new_jobs_list.append(job)
        return new_jobs_list

    def delete_vacancy(self, query=None) -> None:
        """Удаляет вакансию"""
        jobs_list = self.read_file(self.filename)

        if not query:  # Нет критериев удаления
            return

        new_jobs_list = []
        for job in jobs_list:
            if not all(job.get(key) == value for key, value in query.items()):
                new_jobs_list.append(job)

        with open(self.filename, 'w', encoding='utf-8') as file:
            json.dump(new_jobs_list, file, indent=4, ensure_ascii=False)
