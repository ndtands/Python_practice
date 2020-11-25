arr =[10,19,22,33,1]
#Ma trận L hoạt động giống như kiểu cộng dồn
def LIS(arr):
    n= len(arr)
    L=[1]*n
    for i in range(0,n):
        for j in range(0, i):
            if(arr[j]<=arr[i] and (L[i]<L[j]+1)):
                L[i] = L[j]+1
    maximum = 0
    print(L)
    for i in range(n):
        maximum = max(maximum, L[i]) 
    return maximum
print(LIS(arr))