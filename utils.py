def load_candidates_from_json(path):
    """Выгружает данные из файла .json"""

    import json                                             # импорт json
    file = open(path, encoding="utf-8")                     # открытие json - файла
    data = json.load(file)                                  # загрузка списка словарей из json - файла

    return data                                             # возвращвем список словарей


