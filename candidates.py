from utils import *


class Candidates:
    """Класс Candidates содержит:
       Поля:
        - candidates_list                       - список словарей из json-файла

       Методы:
        - Получение словаря ид:имя кандидатов   - get_candidate_names
        - Получение кандидата по ид             - get_candidate_by_id
        - Получение кандидата по имени          - get_candidates_by_name
        - Получение кандидата по навыку         - get_candidates_by_skill
    """

    def __init__(self, candidates_list):
        """Конструктор"""

        self.candidates_list = candidates_list

    def get_candidate_names(self):
        """Получение списка всех имен кандидатов и ид"""

        all_names = {}
        for item in self.candidates_list:
            all_names[item['id']] = item['name']                        # формирование нового словаря

        return all_names

    def get_candidate_by_id(self, candidate_id):
        """Получение кандидата по его id"""

        for candidate in self.candidates_list:                          # перебор элементов списка словаря
            if candidate['id'] == candidate_id:                         # условие проверки id
                name = candidate['name']                                # сохранение данных в переменных name, position, image, skills
                position = candidate['position']
                image = candidate['picture']
                skills = candidate['skills']

        return name, position, image, skills                            # возвращаем кортежем имя, позицию, картинку и навык кандидата

    def get_candidates_by_name(self, candidate_name):
        """Получение кандидата по имени"""

        cand_count = 0                                                  # счетчик
        search_name = {}                                                # результирующий словарь

        for candidate in self.candidates_list:                          # перебор элементов json-файла
            if candidate_name.title() in str(candidate['name']):        # условие проверки name
                cand_count += 1                                         # количество найденных кандидатов
                search_name[candidate['id']] = candidate['name']        # сохранение в словарь имени и ид для передачи в ссылку

        return cand_count, search_name

    def get_candidates_by_skill(self, skill_name):
        """Метод возвращает кандидатов по навыку"""

        cand_count = 0
        search_skill = {}

        for candidate in self.candidates_list:                          # перебор элементов json-файла
            if skill_name.lower() in str(candidate['skills']).lower():  # условие проверки skills
                cand_count += 1                                         # количество найденных кандидатов
                search_skill[candidate['id']] = candidate['name']       # сохранение в словарь имени и ид для передачи в ссылку

        return cand_count, search_skill

