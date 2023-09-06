import sys, math
input = sys.stdin.readline

N = int(input())
arr = []

for _ in range(N):
    arr.append(int(input()))
    
arr.sort() # 중앙값을 구하기 위해 정렬

print(round(sum(arr)/len(arr))) # 산술평균
print(arr[len(arr)//2]) # 중앙값

# 최빈값
dic = dict()
for i in arr: # 빈도수 구하기
    if i in dic:
        dic[i] += 1
    else:
        dic[i] = 1
max_num = max(dic.values()) # 최대 빈도수 값
max_dic = [] # 최빈값을 저장할 배열

for i in dic:
    if max_num == dic[i]: # 최빈값의 key 저장
        max_dic.append(i)

if len(max_dic) > 1: #최빈값이 여러개일경우
    print(max_dic[1]) # 두번째로 작은 값
else: # 최빈값이 하나 일 경우
    print(max_dic[0]) # 해당 값 출력
    
print(max(arr) - min(arr)) # 범위