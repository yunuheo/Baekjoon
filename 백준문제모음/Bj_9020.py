'''
문제링크: https://www.acmicpc.net/problem/9020
'''
def is_prime_number(x):
    # 2부터 (x - 1)까지의 모든 수를 확인하며
    for i in range(2, x//2+1):
        # x가 해당 수로 나누어떨어진다면
        if x % i == 0:
            return False # 소수가 아님
    return True # 소수임

T = int(input())

for i in range(T):
    n = int(input())
    for j in range((n//2),0,-1):
        if is_prime_number(j) and is_prime_number(n-j):  # n은 처음에 짝수이므로, 2로 나누어준 뒤 1씩 감소시키며 소수인지 판별해줌
                print(j, n-j)
                break
    

                


