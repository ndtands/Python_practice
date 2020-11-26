import numpy as np
# T⁄o array 2 chi•u với k‰ch thước (3, 4)
# [[ 1 2 3 4]
# [ 5 6 7 8]
# [ 9 10 11 12]]
a = np.array([[1,2,3,4], [5,6,7,8], [9,10,11,12]])
# Dùng slide đ” l§y ra subarray gồm 2 hàng đƒu ti¶n (1 & 2) và 2 cºt (2 & 3).
# Output là array k‰ch thước 2*2
# [[2 3]
# [6 7]]
#row : 0->1
#column: 0->2
b = a[:2, :3]


# Tạo array 2 chiiều kích thước (3, 4)
# [[ 1 2 3 4]
# [ 5 6 7 8]
# [ 9 10 11 12]]
a = np.array([[1,2,3,4], [5,6,7,8], [9,10,11,12]])
row_r1 = a[1, :] # Lấy ra hàng thứ 2 trong a, output array 1 chiều
row_r2 = a[1:2, :] # Lấy ra hàng thứ 1&2 trong a, output array 2 chiều
print(row_r1, row_r1.shape) # Prints "[5 6 7 8] (4,)"
print(row_r2, row_r2.shape) # Prints "[[5 6 7 8]] (1, 4)"