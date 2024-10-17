from csv import reader


#row:
# 1 - название
# 2 - aвтор
# 6 - цена

output = open('result.txt', 'w',encoding='windows-1251')

while True:
    flag = 0
    search = input('Введите автора: ').lower()
    if search == "book-author":
        print("Неверный запрос")
        break
    with open('books-en.csv', 'r', encoding='windows-1251') as csvfile:
        table = reader(csvfile, delimiter=';')
        for row in table:
            author = row[2].lower()
            if author == search:
                if float(row[6].replace(",", ".")) <= 150: #цена до 150 руб 
                    line = f'{row[1]}.{row[2]} Цена {row[6]} руб.\n'
                    output.write(line)
                    print(line.strip())
                    flag += 1
        if flag == 0:
            print('Ничего не найдено.')
        else:
            print(f'Найдено {flag} результатов.')
            break
output.close()