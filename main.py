from src.models import HhVacancyAPI, JSONStorage, Vacancy

def interact_with_user() -> str:
    query = input("Введите поисковый запрос: ")
    api = HhVacancyAPI(query)
    while True:
        print("\nВыберите действие:")
        print("1. Поиск вакансий по ключевому слову")
        print("2. Получить топ N вакансий по зарплате")
        print("3. Получить вакансии с ключевым словом в описании")
        print("4. Выйти")

        choice = input("Введите номер действия: ")

        if choice == "1":
            query = input("Введите поисковый запрос: ")
            vacancies = api.get_vacancies()
            vacancy: str
            for vacancy in vacancies:
                print(vacancy)
        elif choice == "2":
            try:
                n = int(input("Введите количество вакансий для отображения: "))
                # Реализуйте логику для получения топ N вакансий по зарплате
            except ValueError:
                print("Ошибка: введите корректное число.")
        elif choice == "3":
            keyword = input("Введите ключевое слово для поиска в описании: ")
            # Реализуйте логику для получения вакансий с ключевым словом в описании
        elif choice == "4":
            print("До свидания!")
            break
        else:
            print("Ошибка: выберите корректное действие.")


if __name__ == "__main__":
    interact_with_user()
