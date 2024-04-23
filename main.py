from src.api import HhVacancyAPI


def interact_with_user() -> None:
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
            # Проверяем, что api.get_vacancies() вернул список вакансий
            vacancies = api.get_vacancies()
            if vacancies is not None:
                for vacancy in vacancies:
                    print(vacancy)
            else:
                print("Не удалось получить вакансии. Попробуйте еще раз.")
        elif choice == "2":
            try:
                n = int(input("Введите количество вакансий для отображения: "))
                # Получаем топ N вакансий по зарплате
                top_vacancies = get_top_n_vacancies(api, n)
                if top_vacancies:
                    for vacancy in top_vacancies:
                        print(vacancy)
                else:
                    print("Не удалось получить топ вакансий. Попробуйте еще "
                          "раз.")
            except ValueError:
                print("Ошибка: введите корректное число.")
        elif choice == "3":
            keyword = input("Введите ключевое слово для поиска в описании: ")
            # Получаем вакансии с ключевым словом в описании
            keyword_vacancies = get_keyword_vacancies(api, keyword)
            if keyword_vacancies:
                for vacancy in keyword_vacancies:
                    print(vacancy)
            else:
                print("Не удалось получить вакансии с заданным ключевым "
                      "словом. Попробуйте еще раз.")
        elif choice == "4":
            print("До свидания!")
            break
        else:
            print("Ошибка: выберите корректное действие.")


def parse_salary(salary_str: str) -> float:
    """
    Парсит строку с зарплатой и возвращает среднее значение.
    """
    parts = salary_str.split('-')
    salary_values = [float(part.replace(',', '.'))
                     for part in parts if part.isdigit()]
    return sum(salary_values) / len(salary_values) if salary_values else 0


def get_top_n_vacancies(api: HhVacancyAPI, n: int) -> list:
    """
    Получает топ N вакансий по зарплате.
    """
    vacancies = api.get_vacancies()
    if vacancies:
        sorted_vacancies = sorted(vacancies,
                                  key=lambda x: parse_salary(x.salary),
                                  reverse=True)
        return sorted_vacancies[:n]
    else:
        return []


def get_keyword_vacancies(api: HhVacancyAPI, keyword: str) -> list:
    vacancies = api.get_vacancies()
    if vacancies:
        keyword_vacancies = [vacancy for vacancy in vacancies if
                             keyword.lower() in vacancy.description.lower() and
                             vacancy.description.strip()]
        if keyword_vacancies:
            for vacancy in keyword_vacancies:
                print(f"Описание вакансии: {vacancy.description}")
        else:
            print(
                f"В описаниях вакансий не найдено ключевое слово '{keyword}'.")
    else:
        print("Не удалось получить вакансии. Попробуйте еще раз.")


if __name__ == "__main__":
    interact_with_user()
