N = []
for i in range(5):
    N.append(int(input())) # 다섯 개의 자연수 리스트로 입력받기
    N.sort() # 오름차순 정렬
    av = int(sum(N)/5) # 평균값 구하기
    
print(av) # 평균값
print(N[2]) # 중앙값