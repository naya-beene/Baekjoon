import sys, math
input = sys.stdin.readline

def is_prime(x):
    if x == 0 or x == 1: # N이 0 또는 1 이면 False 리턴후 +1 반복
        return False
    for i in range(2, int(math.sqrt(x))+1): # math.sqrt(x) : x의 제곱근 반환
        if x % i == 0: 
            return False
    return True

T = int(input())
for i in range(T):
    N = int(input())
    while True: 
        if is_prime(N): # N이 √n 보다 작거나 같은 약수를 가지지 않으면 N출력
            print(N)
            break
        else:   
            N += 1