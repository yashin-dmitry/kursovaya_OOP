from abc import ABC, abstractmethod


class AbstractVacancyAPI(ABC):
    @abstractmethod
    def connect(self):
        pass

    @abstractmethod
    def get_vacancies(self):
        pass

class HhVacancyAPI(AbstractVacancyAPI):
    def __init__(self, query: str) -> str:
        self.query = query

    def connect(self):
        pass

    def get_vacancies(self):
        pass

class Vacancy:
    def __init__(self, title, link, salary=None, description=None):
        self.title = title
        self.link = link
        self.salary = salary if salary else "Зарплата не указана"
        self.description = description if description else "Описание отсутствует"

    def __repr__(self):
        return f"Vacancy(title='{self.title}', salary='{self.salary}', description='{self.description}')"

    def __str__(self):
        return f"Вакансия: {self.title}, Зарплата: {self.salary}, Описание: {self.description}"


class JSONStorage:
    pass