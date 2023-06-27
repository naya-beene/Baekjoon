N, k = map(int, input().split()) # 학생 수 상 받는 사람 수 입력 받기
x = list(map(int, input().split())) # 점수 입력 받기

x.sort(reverse=True) # reverse=True 는 내림차순 정렬
print(x[k-1]) # 커트라인 k-1로 출력
