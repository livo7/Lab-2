from csv import reader


#row:
# 1 - название
# 3 - автор
# 4 -  ФИО aвтор
# 7 - цена

output = open('result.txt', 'w',encoding='windows-1251')
flag = 0

while flag!=20:
    with open('books.csv', 'r', encoding='windows-1251') as csvfile:
        table = reader(csvfile, delimiter=';')
        for row in table:
                if float(row[7]) <= 150: #цена до 150 руб
                    line = f'{row[1]}.{row[3]} Цена {row[7]} руб.\n'
                    output.write(line)
                    print(line.strip())
                    flag += 1
output.close()