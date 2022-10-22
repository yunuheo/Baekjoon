#병합정렬을 이용하여 정렬된 배열tmp[]에 k번째로 저장된 숫자 찾기.

#병합정렬 구현
def merge_sort(A,p,r):
    if p<r:
        q = p+r//2
        merge_sort(A,p,q)
        merge_sort(A,q+1,r)
        merge(A,p,q,r)

def merge(A,p,q,r):
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
        i += 1
        t += 1


