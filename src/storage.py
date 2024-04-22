import json
from abc import ABC, abstractmethod

from src.models import Vacancy


class AbstractStorage(ABC):
    @abstractmethod
    def add_vacancy(self, vacancy):
        pass

    @abstractmethod
    def get_vacancies(self, criteria):
        pass

    @abstractmethod
    def remove_vacancy(self, criteria):
        pass


class JSONStorage(AbstractStorage):
    def __init__(self, filename):
        self.filename = filename

    def add_vacancy(self, vacancy):
        with open(self.filename, "a") as file:
            json.dump(vacancy.__dict__, file)
            file.write("\n")

    def get_vacancies(self, criteria):
        with open(self.filename, "r") as file:
            data = json.load(file)
        # Возвращаем вакансии, удовлетворяющие критериям
        return [Vacancy(**vacancy_data) for vacancy_data in data if self._check_criteria(vacancy_data, criteria)]

    def _check_criteria(self, vacancy_data, criteria):
        def _check_criteria(self, vacancy_data, criteria):
            # Проверяем ключевое слово в названии
            if 'keyword' in criteria:
                keyword = criteria['keyword']
                if keyword.lower() not in vacancy_data['title'].lower():
                    return False

            # Проверяем минимальную требуемую зарплату
            if 'min_salary' in criteria:
                min_salary = criteria['min_salary']
                if vacancy_data['salary'] == 'Зарплата не указана':
                    return False
                vacancy_salary = self._parse_salary(vacancy_data['salary'])
                if vacancy_salary < min_salary:
                    return False

            return True

        def _parse_salary(self, salary):
            # Пример простого парсинга зарплаты
            if '-' in salary:
                min_salary, max_salary = map(int, salary.split('-'))
                return min_salary
            elif 'от' in salary:
                return int(salary[3:])
            elif 'до' in salary:
                return int(salary[3:])
            else:
                return int(salary)
        pass