#profile.py

surname = input ('Фамилия:')
name = input ('имя: ')
group = input ('группа: ')
city = input ('город: ')
age = int (input ('возраст от 1 до 120: '))
sudject = input ('предмет: ')
weekly_hours = float (input (' колличество часов: ' ))
fullname = name + surname
future_age = age + 4
four_weeks_hours = weekly_hours * 4
daily_hours = weekly_hours / 7
print ('Учебная карточка')
print (f'Имя: {fullname}')
print (f'Возраст через четыре года: {future_age}')
print (f'За цетыре недели: {four_weeks_hours:.2f}ч')
print (f'В среднем в день: {daily_hours:.2f}ч')




