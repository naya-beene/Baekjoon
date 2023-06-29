import sys

N = int(sys.stdin.readline())
arr = [0] * 10001

for _ in range(N):
    arr[int(sys.stdin.readline())] += 1

for i in range(10001):
    if arr[i] != 0:
        for j in range(arr[i]):
            print(i)

'''
for 문 속에서 append를 사용하게 되면 메모리 재할당이 
이루어져 메모리를 효율적으로 사용하지 못한다.
입력값만큼의 리스트를 만들어 놓고 요소마다 0을 할당
입력값을 받을 때마다 그 입력값과 같은 인덱스에 +1을 해준다.
입력을 다 받고나면 0보다 큰 요소를 갖는 인덱스들을 찾아
그 수만큼 인덱스를 출력
'''