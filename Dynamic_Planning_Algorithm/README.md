# Dynamic Planning Algorimthm
## 1.Dãy con đơn điệu dài nhất.
### Bài toán: Cho dãy A1,A2,…,An. Hãy tìm một dãy con tăng có nhiều phần tử nhất của dãy.
- Vì độ dài dãy con chỉ phụ thuộc vào một yếu tố là dãy ban đầu nên bảng phương án là bảng một chiều. Gọi L_i là độ dài dãy con tăng dài nhất, các phần tử lấy trong miền từ A1 đến A_i và phần tử cuối cùng là A_i.
- Nhận xét với cách làm này ta đã chia 1 bài toán lớn (dãy con của n số) thành các bài toán con cùng kiểu có kích thước nhỏ hơn (dãy con của dãy i số). Vấn đề là công thức truy hồi để phối hợp kết quả của các bài toán con.
Từ yêu cầu bài toán ta có công thức:
    + L_1 = 1
    + L_i = max(1,L_j+1), 0 < j < i và A_j <= A_i
## 2.Bài toán: Cho thuê máy
### Bài toán: Trung tâm tính toán hiệu năng cao nhận được đơn đặt hàng của n khách hàng. Khách hàng i muốn sử dụng máy trong khoảng thời gian từ ai đến bi và trả tiền thuê là ci. Hãy bố trí lịch thuê máy để tổng số tiền thu được là lớn nhất mà thời gian sử dụng máy của 2 khách hàng bất kì được phục vụ đều không giao nhau (cả trung tâm chỉ có một máy cho thuê).
- Nếu sắp xếp các đơn đặt hàng theo thời điểm kết thúc, ta sẽ đưa được về bài toán tìm dãy con có tổng lớn nhất. Bài toán này là biến thể của bài toán tìm dãy con tăng dài nhất, ta có thể cài đặt bằng đoạn chương trình như sau:
```python
for i:=1 to n do
  begin
          L[i]:=C[i];
          for j:=1 to i-1 do
               if (B[j]<=A[i]) and (L[i]<L[j]+C[i]) then L[i]:=L[j]+C[i];
  end;
```