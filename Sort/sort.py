arr = [64, 34, 25, 12, 22, 11, 9]
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
 
#Heap_Sort 
def heapify(arr, n, i):
    largest = i  # Initialize largest as root
    l = 2 * i + 1     # left = 2*i + 1
    r = 2 * i + 2     # right = 2*i + 2
 
    # See if left child of root exists and is
    # greater than root
    if l < n and arr[largest] < arr[l]:
        largest = l
 
    # See if right child of root exists and is
    # greater than root
    if r < n and arr[largest] < arr[r]:
        largest = r
 
    # Change root, if needed
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]  # swap
        # Heapify the root.
        heapify(arr, n, largest)
# The main function to sort an array of given size
def Heap_Sort(arr):
    n = len(arr)
    # Build a maxheap.
    for i in range(n//2 - 1, -1, -1):
        heapify(arr, n, i)
 
    # One by one extract elements
    for i in range(n-1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]  # swap
        heapify(arr, i, 0)
    return arr


# Qick_sort
def partition(arr, low, high):
    i = (low-1)         # index of smaller element
    pivot = arr[high]     # pivot
    for j in range(low, high):
        # If current element is smaller than or
        # equal to pivot
        if arr[j] <= pivot:
            # increment index of smaller element
            i = i+1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i+1], arr[high] = arr[high], arr[i+1]
    return (i+1)
# The main function that implements QuickSort
# arr[] --> Array to be sorted,
# low  --> Starting index,
# high  --> Ending index
# Function to do Quick sort
def Quick_Sort(arr, low, high):
    if len(arr) == 1:
        return arr
    if low < high:
        # pi is partitioning index, arr[p] is now
        # at right place
        pi = partition(arr, low, high)
        # Separately sort elements before
        # partition and after partition
        Quick_Sort(arr, low, pi-1)
        Quick_Sort(arr, pi+1, high)
    return arr

#Radix_Sort
def countingSort(arr, exp1): 
    n = len(arr) 
    # The output array elements that will have sorted arr 
    output = [0] * (n) 
    # initialize count array as 0 
    count = [0] * (10) 
    # Store count of occurrences in count[] 
    for i in range(0, n): 
        index = (arr[i] / exp1) 
        count[int(index % 10)] += 1
    # Change count[i] so that count[i] now contains actual 
    # position of this digit in output array 
    for i in range(1, 10): 
        count[i] += count[i - 1] 
    # Build the output array 
    i = n - 1
    while i >= 0: 
        index = (arr[i] / exp1) 
        output[count[int(index % 10)] - 1] = arr[i] 
        count[int(index % 10)] -= 1
        i -= 1
    # Copying the output array to arr[], 
    # so that arr now contains sorted numbers 
    i = 0
    for i in range(0, len(arr)): 
        arr[i] = output[i] 
# Method to do Radix Sort 
def Radix_Sort(arr): 
    # Find the maximum number to know number of digits 
    max1 = max(arr) 
    # Do counting sort for every digit. Note that instead 
    # of passing digit number, exp is passed. exp is 10^i 
    # where i is current digit number 
    exp = 1
    while max1 / exp > 0: 
        countingSort(arr, exp) 
        exp *= 10
    return arr

print(Quick_Sort(arr,0,len(arr)-1))
print(Radix_Sort(arr))
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
print(a)
(a,t1)=Merge_Sort(arr)
print ('3. Giải Thuật Merge_sort:')
print(a)
print("Tốc độ:") 
print(t1)'''
