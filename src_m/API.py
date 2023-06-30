# -*- coding: utf-8 -*-
from abc import ABC, abstractmethod
import requests


class API(ABC):
    """ Абстрактный класс для работы с API по вакансиям"""

    @abstractmethod
    def get_vacancies(self, keyword):
        pass


class HeadHunterAPI(API):
    """Класс для работы с HeadHunter"""

    def __init__(self):
        self.url = "https://api.hh.ru/vacancies"

    def get_vacancies(self, keyword):
        params = {"text": keyword.lower()}
        vacancies_raw = requests.get(self.url, params=params)
        vacancies = vacancies_raw.json()

        vacancies_data = []
        for i in vacancies.get('items', []):
            title = i.get('name', ' ')
            link = i.get('alternate_url', '')
            salary = i.get('salary')
            description = i.get('snippet', {}).get('responsibility', '')
            vacancies_data.append({'title': title, 'link': link, 'salary': salary, 'description': description})
        return vacancies_data


class SuperJobAPI(API):
    """Класс для работы с Super Job"""

    def __init__(self):
        self.url = "https://api.superjob.ru/2.0/vacancies"

    def get_vacancies(self, keyword):
        headers = {
            "X-Api-App-Id": "v3.r.137616592.aa33c9bf0b28400429de1f2c8dc68679791e09f9.e72e1f56545343820a961593bb2b906754e9370a"}
        params = {"keyword": keyword.lower()}
        response = requests.get(self.url, headers=headers, params=params)
        data = response.json()

        vacancies_data = []
        for i in data.get('objects', []):
            title = i.get('profession', ' ')
            link = i.get('link', '')
            salary = {
                'from': i.get('payment_from'),
                'to': i.get('payment_to')
            }
            description = i.get('candidat')
            vacancies_data.append({'title': title, 'link': link, 'salary': salary, 'description': description})
        return vacancies_data
