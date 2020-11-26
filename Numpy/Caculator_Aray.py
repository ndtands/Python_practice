import numpy as np
x = np.array([[1,2],[3,4]], dtype=np.float64)
y = np.array([[5,6],[7,8]], dtype=np.float64)
# Tính tổng
# [[ 6.0 8.0]
# [10.0 12.0]]
print(x + y)
print(np.add(x, y))
# Phép trừ
# [[-4.0 -4.0]
# [-4.0 -4.0]]
print(x - y)
print(np.subtract(x, y))
# Phép nhân 
# [[ 5.0 12.0]
# [21.0 32.0]]
print(x * y)
print(np.multiply(x, y))
# Phép chia
# [[ 0.2 0.33333333]
# [ 0.42857143 0.5 ]]
print(x / y)
print(np.divide(x, y))
# Tính căn 
# [[ 1. 1.41421356]
# [ 1.73205081 2. ]]
print(np.sqrt(x))

# In other hand
x = np.array([[1,2],[3,4]])
y = np.array([[5,6],[7,8]])
v = np.array([9,10])
w = np.array([11, 12])
print(v.dot(w))
print(np.dot(v, w))

# Numpy cũng hỗ trợ tính tổng array theo các chiều khác nhau
x = np.array([[1,2],[3,4]])
print(np.sum(x)) # Tính tổng tất cả phần tử trong array; prints "10"
print(np.sum(x, axis=0)) # Tính tổng phần tử mỗi hàng; prints "[4 6]"
print(np.sum(x, axis=1)) # Tính tổng phần tử mỗi cột; prints "[3 7]"
