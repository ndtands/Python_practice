import numpy as np
a = np.array([1, 2, 3]) # Tạo array 1 chiều
print(type(a)) # Prints "<class 'numpy.ndarray'>"
print(a.shape) # Prints "(3,)"
print(a[0], a[1], a[2]) # Prints "1 2 3"
a[0] = 5 # Thay đổi phần tử vị trí số 0
print(a) # Prints "[5, 2, 3]"
b = np.array([[1,2,3],[4,5,6]]) # Tạo array 2 chiều
print(b.shape) # Prints "(2, 3)"
print(b[0, 0], b[0, 1], b[1, 0]) # Prints "1 2 4"

#In other hand
a = np.zeros((2,2)) # Tạo array với tất cả các phần tử 0
print(a) # Prints "[[ 0. 0.]
         # [ 0. 0.]]"
b = np.ones((1,2)) # Tạo array với các phần tử 1
print(b)            # Prints "[[ 1. 1.]]"
c = np.full((2,2), 7) # Tạo array với các phần tử 7
print(c) # Prints "[[ 7. 7.]
                # [ 7. 7.]]"
d = np.eye(2) # Tạo identity matrix kícch thước 2*2
print(d) # Prints "[[ 1. 0.]
        # [ 0. 1.]]"
e = np.random.random((2,2)) # Tạo array với các phần tử được tạo ngẫu nhiên
print(e) # Might print "[[ 0.91940167 0.08143941]
# [ 0.68744134 0.87236687]]


