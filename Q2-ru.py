from csv import reader


#row:
# 1 - название
# 3 - автор
# 4 -  ФИО aвтор
# 7 - цена

output = open('result.txt', 'w',encoding='windows-1251')

while True:
    flag = 0
    search = input('Введите ФИО автора: ').lower()
    if search == "автор":
        print("Неверный запрос")
        break
    with open('books.csv', 'r', encoding='windows-1251') as csvfile:
        table = reader(csvfile, delimiter=';')
        for row in table:
            author = row[4].lower()
            if author == search:
                if float(row[7]) <= 150: #цена до 150 руб
                    line = f'{row[1]}.{row[3]} Цена {row[7]} руб.\n'
                    output.write(line)
                    print(line.strip())
                    flag += 1
        if flag == 0:
            print('Ничего не найдено.')
        else:
            print(f'Найдено {flag} результатов.')
            break
output.close()