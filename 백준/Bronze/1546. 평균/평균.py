N = int(input())
scores = list(map(int, input().split()))
M = max(scores) #점수들 중 최댓값 대입

for i in range(N):
    scores[i] = scores[i]/M*100 #제시한 수식에 따른 점수 변경
    
print(sum(scores)/N) #sum()함수를 이용하여 합을 구하고 평균 출력
