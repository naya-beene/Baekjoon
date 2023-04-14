N = int(input())
cnt = N
for _ in range(N):
    word = input()
    for i in range(len(word)-1):
        if  word[i] == word[i+1]: # 앞뒤 단어가 같으면 패스
            pass
        elif word[i] in word[i+1:]: # 앞의 단어가 포함 되었으면 cnt -1
            cnt -= 1
            break
print(cnt)