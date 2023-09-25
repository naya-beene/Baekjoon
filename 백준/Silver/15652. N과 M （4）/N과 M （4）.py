import sys
input = sys.stdin.readline

N, M = list(map(int, input().split()))

s = [] # 재귀함수를 이용하여 m개의 수열을 저장하기 위한 리스트

def dfs(start):
    if len(s) == M: # 리스트에 들어간 수열들이 m개가 되면 리스트에 들어있는 숫자들을 모두 출력하고 함수를 나옴
        print(' '.join(map(str, s)))
        return
    
    for i in range(start, N+1): # N까지의 모든 숫자를 확인하지만 뒤의 숫자보다 작은 경우를 제외하기 위해 start부터 n까지
        s.append(i) 
        dfs(i) 
        s.pop()
dfs(1)