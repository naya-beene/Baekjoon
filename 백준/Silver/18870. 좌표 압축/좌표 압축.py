import sys
N = int(sys.stdin.readline()) # 좌표 개수
x = list(map(int, sys.stdin.readline().split())) # 좌표값 입력
arr = sorted(set(x)) # 중복제거 및 오름차순 정렬

# list.index(i)의 형태는 시간복잡도 O[N]
# {dict[요소] : 요소index }의 형태 시간 복잡도 O[1]
dict = {arr[i] : i for i in range(len(arr))} # arr의 길이(0~3)를 arr배열의 요소에 넣어줌

for i in x:
    print(dict[i], end = ' ')