S = input()
result = set()
for i in range(len(S)): # 이중 반복문으로 문자열의 부분 문자열 구하기
    for j in range(i, len(S)):
        result.add(S[i : j+1]) # i 번째 문자부터 부분문자열 구하기
        
print(len(result))