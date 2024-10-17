from csv import reader


#row:
# 1 - название
# 2 - aвтор
# 3 - дата публикации

output = open('bibliographic_references.txt', 'w',encoding='windows-1251')
flag = 1

while True:
    with open('books-en.csv', 'r', encoding='windows-1251') as csvfile:
        table = reader(csvfile, delimiter=';')
        for row in table:
            author = row[2].lower()
            line =f'{flag} {row[2]}. {row[1]} - {row[3]} год.\n'
            output.write(line)
            print(line.strip())
            flag += 1
            if flag >20:
                output.close()
                break