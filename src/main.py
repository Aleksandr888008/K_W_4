# -*- coding: utf-8 -*-
from sort_v import sort_vacancies, get_top_vacancies, get_hh_vacancies, get_sj_vacancies
from workAPI import HeadHunterAPI, SuperJobAPI


def main():
    """ Пользовательская функция"""
    keyword = input("Введите поисковый запрос: ")

    hh = HeadHunterAPI(keyword)
    sj = SuperJobAPI(keyword)


# теперь нужно обработать запрос по ключевому слову и добавить в файл с помощью get_file_manager(filename)


while True:
    action = input("Как показать вакансии? Отсортировать или вывести топ?\nВведите: 'сортировка' или 'топ': ")
    if action == 'сортировка':
        hh_vacanciec = get_hh_vacancies(....)
        sj_vacancies = get_sj_vacancies(....)
        sort_vacancies = sort_vacancies(hh_vacanciec + sj_vacancies)
        for vacancy in sort_vacancies:
            print(vacancy)

    elif action == 'топ':
        hh_vacanciec = get_hh_vacancies(....)
        sj_vacancies = get_sj_vacancies(....)
        all_vacancies = hh_vacanciec + sj_vacancies
        top_count = int(input("Введите количество вакансий для вывода в топ N: "))
        top_vacancies = get_top_vacancies(all_vacancies, top_count)
        for vacancy in top_vacancies:
            print(vacancy)

    else:
        print("Вы ввели не верный запрос")


if __name__ == '__main__':
    main()