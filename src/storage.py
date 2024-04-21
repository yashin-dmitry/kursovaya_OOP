from abc import ABC, abstractmethod


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
        # Код для добавления вакансии в JSON-файл
        pass

    def get_vacancies(self, criteria):
        # Код для получения вакансий из JSON-файла по указанным критериям
        pass

    def remove_vacancy(self, criteria):
        # Код для удаления вакансии из JSON-файла по указанным критериям
        pass
