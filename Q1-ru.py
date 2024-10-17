from csv import reader

Name_more_30 = 0

with open('books.csv', 'r', encoding='windows-1251') as csvfile:
    table = reader(csvfile, delimiter=';')
    for row in table:
        if len(row[1]) > 30: #назввание книги больше 30 символов
            Name_more_30 += 1
print(Name_more_30)