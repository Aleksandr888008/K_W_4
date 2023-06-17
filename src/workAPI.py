from abc import ABC, abstractmethod
import requests
from file_manager import FileManager
import os

urlHH = "https://api.hh.ru/vacancies"

urlSJ = "https://api.superjob.ru/2.0/vacancies"
key = "v3.r.137616592.aa33c9bf0b28400429de1f2c8dc68679791e09f9.e72e1f56545343820a961593bb2b906754e9370a"


class API(ABC):
    """ ����������� ����� ��� ������ � API �� ���������"""

    @abstractmethod
    def get_from_api(self):
        pass

    @staticmethod
    def get_file_manager(filename):
        """���������� ������ ������ FileManager ��� ������ � ������"""
        return FileManager(filename)


class HeadHunterAPI(API):
    def __init__(self, profession, page):
        self.url = urlHH
        self.params = {
            "text": profession,  #������ ���������
            "page": page  #��������
        }

    def get_from_api(self):
        response = requests.get(self.url, params=self.params)
        return response


class SuperJobAPI(API):
    def __init__(self, profession, page):
        self.url = urlSJ
        self.params = {
            "text": profession,  #������ ���������
            "page": page  #��������
        }

    def get_from_api(self):
        response = requests.get(self.url, params=self.params)
        return response
