words = [input() for i in range(5)] # 리스트 컴프리헨션(list comprehension)

for j in range(15):
    for i in range(5):
        if j < len(words[i]):
            print(words[i][j], end='')