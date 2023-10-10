import sys
n = int(sys.stdin.readline())
graph = [ list(map(int, sys.stdin.readline().split())) for _ in range(n) ]
visit = [ False for _ in range(n) ] # 1차원으로 방문 리스트 생성
min_value = sys.maxsize #최소값을 갱신할 변수 생성

def backTracking(depth, idx): #깊이를 나타내는 변수와 인덱스 변수를 인자로 받아줌
    global min_value
    if depth == n // 2: #N은 짝수로 주어짐, 주어진 수의 절반이 한 팀으로 선택 되었을때 지치기 시작
        power1, power2 = 0, 0
        for i in range(n):
            for j in range(n):
                if visit[i] and visit[j]: # True의 값을 가지는 팀을 스타트라 할때 스타트 팀의 능력치를 모두 power1에 더한다.
                    power1 += graph[i][j]
                elif not visit[i] and not visit[j]: # 나저미 절반 Fasle의 값을 가지는 팀을 링크팀이라 할때 링크 팀의 능력치를 모두 power2에 더한다.
                    power2 += graph[i][j]
        min_value = min(min_value, abs(power1-power2)) # 2중 for문이 끝났을때 그 둘의 차이의 절대값이 변수보다 작으면 변수 갱신
        return

    for i in range(idx, n): #4번의 조건에 걸리기전
        if not visit[i]:
            visit[i] = True
            backTracking(depth+1, i+1) #깊이 +1, 같은 번호 중복을 막기위한 idx + 1로 재귀호출
            visit[i] = False
backTracking(0, 0)
print(min_value)