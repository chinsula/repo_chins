users = ['user1', 'user2', 'user3', 'user1', 'user4', 'user2']

# TODO Добавьте словарь и замените в нем нулевые значения статисчикой посещений
site_visits = {
    "Общее количество": 0,
    "Уникальные посещения": 0,
}
site_visits["Общее количество"] = len(users)
site_visits["Уникальные посещения"] = len(set(users))
print(site_visits)
