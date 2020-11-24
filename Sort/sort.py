#Bubble sort
def Bubble_sort(arr):
    time = 0
    n=len(arr)
    for i in range(n-1):
        #Bởi vì sau mỗi lần thì số to nhất đã nổi lên cuối rồi.
        for j in range(0,n-1-i):
            time = time +1
            if (arr[j]>arr[j+1]):
                t=arr[j]
                arr[j]=arr[j+1]
                arr[j+1]=t
    return arr,time

#Insertion_sort
def Insertion_Sort(arr):
    time = 0
    n=len(arr)
    for i in range(1,n):
        key=arr[i]
        j=i-1
        #Lấy giá trị thứ i so sánh với các giá trị trước
        # đó trong khoảng từ 0 đến i-1
        while(j>=0 and (key<arr[j])):
            arr[j+1] = arr[j]
            j-=1
            time =time +1
        # Vị trí mà trí trị key chèn vào
        arr[j+1]=key
    return arr,time

#Merge_Sort
def Merge_Sort(arr):
    Time =0
    if len(arr) > 1:
         # Finding the mid of the array
        mid = len(arr)//2
        # Dividing the array elements
        L = arr[:mid]
        print(L)
        # into 2 halves
        R = arr[mid:]
        print (R)
        # Sorting the first half
        Merge_Sort(L)
        # Sorting the second half
        Merge_Sort(R)
        i = j = k = 0
        # Copy data to temp arrays L[] and R[]
        while (i < len(L) and j < len(R)):
            Time =Time +1
            if (L[i] < R[j]):
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1
 
        # Checking if any element was left
        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1
        # Checking if any element was right
        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1
    return arr,Time
arr = [64, 34, 25, 12, 22, 11, 9] 
'''(a,t1)=Bubble_sort(arr)
print ('1. Giải Thuật Bubble_sort:')
print(a)
print("Tốc độ:") 
print(t1)
(a,t1)=Insertion_Sort(arr)
print ('2. Giải Thuật Insertion_sort:')
print(a)
print("Tốc độ:") 
print(t1)
print(a)'''
(a,t1)=Merge_Sort(arr)
print ('3. Giải Thuật Merge_sort:')
print(a)
print("Tốc độ:") 
print(t1)
