from abc import ABC, abstractmethod
import requests

class AbstractVacancyAPI(ABC):
    @abstractmethod
    def connect(self):
        pass

    @abstractmethod
    def get_vacancies(self, query):
        pass


class HhVacancyAPI(AbstractVacancyAPI):
    def __init__(self, query):
        self.query = query
        self.base_url = "https://api.hh.ru/"

    def connect(self):
        pass

    def get_vacancies(self):
        url = f"{self.base_url}vacancies"
        params = {"text": self.query}
        response = requests.get(url, params=params)
        if response.status_code == 200:
            return response.json()["items"]
        else:
            print("Ошибка при получении вакансий:", response.status_code)
            return None

class HeadHunterAPI(AbstractVacancyAPI):
    def __init__(self, query):
        self.query = query
        self.base_url = "https://api.hh.ru/"

    def get_vacancies(self, query):
        url = f"{self.base_url}vacancies"
        params = {"text": query}
        response = requests.get(url, params=params)
        if response.status_code == 200:
            return response.json()["items"]
        else:
            print("Ошибка при получении вакансий:", response.status_code)
            return None
