import json

class JSONSaver:
    def __init__(self, filename="vacancies.json"):
        self.filename = filename

    def add_vacancy(self, vacancy):
        with open(self.filename, "a") as file:
            json.dump(vacancy.__dict__, file)
            file.write("\n")

    def delete_vacancy(self, vacancy):
        # Открываем файл для чтения
        with open(self.filename, "r") as file:
            data = json.load(file)  # Загружаем данные из файла

        for idx, item in enumerate(data):
            if item["link"] == vacancy.link:
                del data[idx]  # Удаляем вакансию из данных
                break

        # Открываем файл для записи и сохраняем обновленные данные
        with open(self.filename, "w") as file:
            json.dump(data, file)
