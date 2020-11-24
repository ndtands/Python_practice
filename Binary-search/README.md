# Giải thuật Binary-search 
## Using Đệ quy 
### Step1: So sánh x với phần tử ở giữa.
### Step2: Nếu x khớp với phần tử ở giữa, chúng ta trả về chỉ số ở giữa.
### Step3: Ngược lại, nếu x lớn hơn phần tử ở giữa thì nó sẽ lấy nữa mảng phía trên và ngược lại. Nếu tục lặp lại Step2 với mảng đầu vào mới cập nhật
=> Để có thể dùng được đệ quy ta phải cần một hàm với đầu vào có index_start và index_stop, arr_input và giá trị x tìm kiếm x.
=> Tốc độ sẽ được cải thiện thành O(Log2(N))

