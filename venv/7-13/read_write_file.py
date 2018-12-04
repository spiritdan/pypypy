file = open('./scores.txt', 'r', encoding='utf8')
file_lines = file.readlines()
file.close

# print(file_lines)
sum_score = []
for i in file_lines:
    # print(i)
    data = i.split()
    # print(data)
    sum = 0
    for j in data[1:]:
        sum = sum + int(j)
    result = data[0] + ' ' + str(sum) + '\n'
    # print(result)
    sum_score.append(result)
    print(sum_score)

winner = open('./winner.txt', 'w', encoding='utf-8')
winner.writelines(sum_score)
winner.close()