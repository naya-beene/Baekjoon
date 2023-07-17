import sys
input = sys.stdin.readline
N, M = map(int, input().split())

a = set() # 중복이 없는 set의 특성을 활용
for i in range(N):
    a.add(input())

b = set()
for i in range(M):
    b.add(input())
    
result = sorted(list(a & b)) 
# set a, b에 교집합 &을 해서 중복되는 문자열을 선택후 리스트로 묶음
# sorted 사전 순으로 정렬

print(len(result)) # 듣보잡 수
for i in result: # 듣보잡 문자열
    print(i, end = '')
