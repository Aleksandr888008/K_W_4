# -*- coding: utf-8 -*-

from API import HeadHunterAPI, SuperJobAPI
from vacancy import Vacancy
from jsonhandler import JsonHandler


def user_interaction():
    """
    Функция осуществляет взаимодействие с пользователем
    :return:
    """
    hh_api = HeadHunterAPI()
    json_worker = JsonHandler()
    sj_api = SuperJobAPI()
    while True:
        platform = input("Выберите платформу с которой хотите получить вакансии или иное:\n"
                         "1) HeadHunter 2) SuperJob 3) Сортировка с двух платформ 4) Выход: ")
        if platform == '1':
            search_name_hh = input("Введите запрос вакансии: ")
            data_hh = hh_api.get_vacancies(search_name_hh)
            json_worker.add_vacancy(data_hh)
            if not data_hh:
                print("Такой вакансии нет")
            else:
                filtered_data_hh = [item for item in data_hh if item.get('salary') is not None]
                top_n = int(input("Введите количество вакансий для вывода: "))
                list_vacancies = []
                for item in filtered_data_hh:
                    vacancy = Vacancy(item['title'], item['link'], item['salary'], item['description'])
                    list_vacancies.append(vacancy)
                sorted_data = sorted(list_vacancies, reverse=True)
                top_n_data = sorted_data[:top_n]
                for vacancy in top_n_data:
                    print(f" \n"
                          f"Название: {vacancy.title}\n"
                          f"Ссылка на вакансию: {vacancy.url}\n"
                          f"Зарплата от: {vacancy.salary}\n"
                          f"Описание вакансии: {vacancy.description}"
                          )

        elif platform == '2':
            search_name_sj = input("Введите запрос вакансии: ")
            data_sj = sj_api.get_vacancies(search_name_sj)
            json_worker.add_vacancy(data_sj)
            if not data_sj:
                print("Такой вакансии нет")
            else:
                filtered_data_sj = [item for item in data_sj if item.get('salary') is not None]
                top_n = int(input("Введите количество вакансий для вывода: "))
                list_vacancies = []
                for item in filtered_data_sj:
                    vacancy = Vacancy(item['title'], item['link'], item['salary'], item['description'])
                    list_vacancies.append(vacancy)
                sorted_data = sorted(list_vacancies, reverse=True)
                top_n_data = sorted_data[:top_n]
                for vacancy in top_n_data:
                    print(f" \n"
                          f"Название: {vacancy.title}\n"
                          f"Ссылка на вакансию: {vacancy.url}\n"
                          f"Зарплата от: {vacancy.salary}\n"
                          f"Описание вакансии: {vacancy.description}"
                          )

        elif platform == '3':
            search = input("Введите запрос вакансии: ")
            data_hh = hh_api.get_vacancies(search)
            data_sj = sj_api.get_vacancies(search)
            json_worker.add_vacancy(data_hh + data_sj)
            data = json_worker.get_vacancy(search)
            if not data:
                print("Такой вакансии нет")
            else:
                filtered_data = [item for item in data if item.get('salary') is not None]
                top_n = int(input("Введите количество вакансий для вывода: "))
                list_vacancies = []
                for item in filtered_data:
                    vacancy = Vacancy(item['title'], item['link'], item['salary'], item['description'])
                    list_vacancies.append(vacancy)
                sorted_data = sorted(list_vacancies, reverse=True)
                top_n_data = sorted_data[:top_n]
                for vacancy in top_n_data:
                    print(f" \n"
                          f"Название: {vacancy.title}\n"
                          f"Ссылка на вакансию: {vacancy.url}\n"
                          f"Зарплата от: {vacancy.salary}\n"
                          f"Описание вакансии: {vacancy.description}"
                          )

        elif platform == '4':
            json_worker.clear_file()
            print("Вы вышли из программы")
            break
        else:
            print('НЕ ВЕРНЫЙ ЗАПРОС')
