# Задача 1. Член семьи

family_member = dict()

family_member['name'] = 'Jane'
family_member['surname'] = 'Doe'
family_member['hobbies'] = ["running", "sky diving", "singing"]
family_member['age'] = 35
family_member['children'] = [
        {
            "name": "Alice",
            "age": 6
        },
        {
            "name": "Bob",
            "age": 8
        }
    ]

child_dict = [i['name'] for i in family_member.get(['children'][0])]

search_child = input('Введите имя искомого ребенка: ')

print('В семье есть ребенок именем {0}.'.format(search_child) if search_child in child_dict else 'Таких нет')
print('Дети:', child_dict)
print(family_member.get(['children'][0])[0].get('surname', 'Nosurname'))
