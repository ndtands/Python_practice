# Là một kỹ thuật cho phép numpy làm việc với các array có shape khác nhau
# Khi thực hiện các phép toán
import numpy as np
# Cộng vector v với mỗi hàng của ma trận x, kết quả lưu ở ma trận y.
x = np.array([[1,2,3], [4,5,6], [7,8,9], [10, 11, 12]])
v = np.array([1, 0, 1])
y = np.empty_like(x) # Tạo 1 array có chiều giống x
# Dùng loop để vector v với mỗi hàng của ma trận
for i in range(4):
    y[i, :] = x[i, :] + v
print(y)
# Kết quả của y
# [[ 2 2 4]
# [ 5 5 7]
# [ 8 8 10]
# [11 11 13]]
# Cộng kiểu broadcasting trong python
print(x + v)
# Kết quả
# [[ 2 2 4]
# [ 5 5 7]
# [ 8 8 10]
# [11 11 13]]
# 2 kết quả cho ra giống nhau