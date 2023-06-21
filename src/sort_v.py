# -*- coding: utf-8 -*-
from vacancy import Vacancy
from work_v import Vacancies


def sort_vacancies(vacancies: list[Vacancy]) -> list:
    """Сортировка вакансий"""
    return sorted(vacancies, reverse=True)


def get_top_vacancies(vacancies: list[Vacancy], top_count: int) -> list:
    """Сортировка вакансий 'ТОП'"""
    return sorted(vacancies, reverse=True)[:top_count]


def get_hh_vacancies(file) -> list:
    vacancies = [
        HHVacancy(
            title=vacancy["name"],
            link=vacancy["alternate_url"],
            description=vacancy["snippet"]['requirement'],
            salary=vacancy["salary"]["from"] if vacancy.get("salary") else None)
        for vacancy in search()]

    return vacancies


def get_sj_vacancies(file) -> list:
    vacancies = [
        SJVacancy(
            title=vacancy["profession"],
            link=vacancy["link"],
            description=vacancy["candidat"],
            salary=vacancy["payment_from"])
        for vacancy in search()]

    return vacancies