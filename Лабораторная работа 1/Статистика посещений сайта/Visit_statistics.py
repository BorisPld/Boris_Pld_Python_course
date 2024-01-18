users = ['user1', 'user2', 'user3', 'user1', 'user4', 'user2']

# TODO Добавьте словарь и замените в нем нулевые значения статисчикой посещений
document = {
    "Общее количество": 0,
    "Уникальные посещения": 0
}

document["Общее количество"] = len(users)
document["Уникальные посещения"] = len(set(users))

print(document)
