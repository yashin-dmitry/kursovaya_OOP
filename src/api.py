from abc import ABC, abstractmethod
import requests

from src.models import Vacancy


class AbstractVacancyAPI(ABC):
    @abstractmethod
    def connect(self):
        pass

    @abstractmethod
    def get_vacancies(self, query):
        pass


class HhVacancyAPI(AbstractVacancyAPI):
    def __init__(self, query: str) -> None:
        super().__init__()
        self.query = query
        self.base_url = "https://api.hh.ru/"

    def connect(self) -> None:
        # Код для подключения к API hh.ru
        pass

    def get_vacancies(self):
        url = f"{self.base_url}vacancies"
        params = {"text": self.query}
        response = requests.get(url, params=params)
        if response.status_code == 200:
            vacancies_data = response.json()["items"]
            vacancies = []
            for vacancy_data in vacancies_data:
                title = vacancy_data.get("name", "")
                link = vacancy_data.get("alternate_url", "")
                salary_data = vacancy_data.get("salary")
                if salary_data:
                    salary_min = salary_data.get("from", "")
                    salary_max = salary_data.get("to", "")
                    currency = salary_data.get("currency", "")
                    salary_range = f"{salary_min}-{salary_max}" if salary_min and salary_max else "Зарплата не указана"
                    salary_str = f"{salary_range} {currency}" if currency else salary_range
                else:
                    salary_str = "Зарплата не указана"
                description = vacancy_data.get("description",
                                               "Описание отсутствует")

                vacancy = Vacancy(title, link, salary_str, description)
                vacancies.append(vacancy)

            return vacancies
        else:
            print("Ошибка при получении вакансий:", response.status_code)
            return None

    def _parse_salary(self, salary: dict) -> tuple:
        salary_min = salary.get("from", "")
        salary_max = salary.get("to", "")
        currency = salary.get("currency", "")
        return salary_min, salary_max, currency

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
