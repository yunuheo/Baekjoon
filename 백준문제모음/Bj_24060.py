#병합정렬을 이용하여 정렬된 배열tmp[]에 k번째로 저장된 숫자 찾기.

#병합정렬 구현

N,k = map(int,input().split(' '))
A = list(map(int,input().split(' ')))


def merge_sort(A,p,r):
    if p<r:
        q = (p+r)//2
        merge_sort(A,p,q)
        merge_sort(A,q+1,r)
        merge(A,p,q,r)
        
       
def merge(A,p,q,r):
    global cnt  #함수 안에서 전역변수 cnt를 사용하기 위해 global 키워드를 사용!!!!!
    global result
    i = p
    j = q+1
    tmp = []
    
    while i<=q and j <= r:
        if A[i] <= A[j]:
            tmp.append(A[i])
            i += 1
        else:
            tmp.append(A[j])
            j += 1
    while i<=q:
        tmp.append(A[i])
        i += 1
    while j<=r:
        tmp.append(A[j])
        j += 1
    
    i = p
    t = 0
    
    while i<=r:
        A[i] =tmp[t]
        cnt += 1  #정렬된 수가 배열A에 저장될때마다 1씩 증가
        if cnt == k:
            result = A[i]
            break
        
        i += 1
        t += 1
    if cnt < k:
        result = -1

cnt = 0  #cnt는 전역변수임 바로 아래 merge_sort 함수 내에서 사용될 예정(=>global 키워드 사용)
result = 0
merge_sort(A,0,N-1)  
print(result)


