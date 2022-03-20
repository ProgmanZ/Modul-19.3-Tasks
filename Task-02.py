# Задача 2. Игроки

players_dict = dict()

players_dict = {
    1: {'name': 'Vanya', 'team': 'A', 'status': 'Rest'},
    2: {'name': 'Lena', 'team': 'B', 'status': 'Training'},
    3: {'name': 'Maxim', 'team': 'C', 'status': 'Travel'},
    4: {'name': 'Egor', 'team': 'C', 'status': 'Rest'},
    5: {'name': 'Andrei', 'team': 'A', 'status': 'Training'},
    6: {'name': 'Sasha', 'team': 'A', 'status': 'Rest'},
    7: {'name': 'Alina', 'team': 'B', 'status': 'Rest'},
    8: {'name': 'Masha', 'team': 'C', 'status': 'Travel'}
}

command_A = [players_dict.get(i).get('name') for i in players_dict if players_dict.get(i).get('team') == 'A' and players_dict.get(i).get('status') == 'Rest']
command_B = [players_dict.get(i).get('name') for i in players_dict if players_dict.get(i).get('team') == 'B' and players_dict.get(i).get('status') == 'Training']
command_C = [players_dict.get(i).get('name') for i in players_dict if players_dict.get(i).get('team') == 'C' and players_dict.get(i).get('status') == 'Travel']

print('Все члены команды из команды А, которые отдыхают:', command_A)
print('Все члены команды из группы B, которые тренируются:', command_B)
print('Все члены команды из команды C, которые путешествуют:', command_C)
