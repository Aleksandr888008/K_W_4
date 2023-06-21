# -*- coding: utf-8 -*-
import json
import os


class FileManager:
    """Класс для работы с файлами"""

    def __init__(self, filename):
        """Сохраняет имя файла, с которым выполняется работа"""
        self.filename = filename

    @staticmethod
    def create(filename) -> None:
        """Проверяет существование файла. Если его нет, то создается пустой файл"""

        if not os.path.exists(os.path.dirname(filename)):
            os.mkdir(os.path.dirname(filename))

        if not os.path.exists(filename):
            with open(filename, 'w') as file:
                file.write(json.dumps([]))

    @staticmethod
    def read_file(filename) -> list:
        """Читает данные из файла filename в формате Json"""

        with open(filename, 'r', encoding="utf-8") as file:
            return json.load(file)


