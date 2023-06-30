# -*- coding: utf-8 -*-
import json


class JsonHandler:
    def __init__(self):
        self.file_path = "vacancy.json"

    def add_vacancy(self, vacancy_data):
        """Дописываем в файл"""
        with open(self.file_path, 'w', encoding="utf-8") as file:
            json_f = json.dumps(vacancy_data, indent=4, ensure_ascii=False)
            file.write(json_f)

    def get_vacancy(self, criteria):
        """По запрашиваемому слову проверяем соответствие и добавляем в словарь"""
        found_vacancies = []
        with open(self.file_path, 'r', encoding="utf-8") as file:
            data = json.load(file)
        for i in data:
            if criteria in i['title']:
                found_vacancies.append(i)
        return found_vacancies

    def clear_file(self):
        with open(self.file_path, 'w', encoding="utf-8") as file:
            file.write('')

