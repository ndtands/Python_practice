# Giải thuật Tham lam
### 1. Bài toán đặt ra:
<table>
  <thead>
    <tr>
      <th style="text-align: center">ID- Active</th>
      <th style="text-align: center">Time</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="text-align: center">1. Sửa phòng </td>
      <td style="text-align: center">T2, 22:00 đến T3, 1:00</td>
    </tr>
    <tr>
      <td style="text-align: center">2. Du lịch Hawaii</td>
      <td style="text-align: center">T3, 6:00 đến T7,22:00</td>
    </tr>
    <tr>
      <td style="text-align: center">3. Vô địch cuộc thi cờ vua</td>
      <td style="text-align: center">T3, 11:00 đến T3, 21:00</td>
    </tr>
    <tr>
      <td style="text-align: center">4. Thạm dự nhạc hội Rock</td>
      <td style="text-align: center">T3, 19:00 đến T3, 23:00</td>
    </tr>
    <tr>
      <td style="text-align: center">5. Chiến thắng cuộc thi Starcraft</td>
      <td style="text-align: center">T4, 15:00 đến T5, 15:00</td>
    </tr>
    <tr>
      <td style="text-align: center">6. Chơi trò bắn súng nước sơn</td>
      <td style="text-align: center">T5, 10:00 đến T5, 16:00</td>
    </tr>
    <tr>
      <td style="text-align: center">7. Tham gia kỳ thi SRM trên Topcoder</td>
      <td style="text-align: center">T7, 12:00 đến T7, 14:00</td>
    </tr>
    <tr>
      <td style="text-align: center">8. Tắm rửa</td>
      <td style="text-align: center">T7, 20:30 đến T7, 20:45</td>
    </tr>
    <tr>
      <td style="text-align: center">9. Tổ chức tiệc ngủ</td>
      <td style="text-align: center">T7, 21:00 đến CN, 6:00</td>
    </tr>
    <tr>
      <td style="text-align: center">10. Tham gia thử thách "All you can eat" và "All you can drink"</td>
      <td style="text-align: center">T7, 21:01 đến T7, 23:59</td>
    </tr>
  </tbody>
</table>

### Yêu cầu :
- Join có N hoạt động, hoạt động thứ i bắt đầu lúc L[i] và kết thúc vào thời gian R[i]
- Join có thể thực hiện được hoạt động i và hoạt động j, nếu 2 khoảng thời gian là không giao nhau.
- Làm cách nào để anh ta có thể  thực hiện tối đa các hoạt động.

### Giải thuật :
- cách tiếp cận 1: Chọn L[i] nhỏ nhất
- cách tiếp cận 2: Chọn hoạt động có R[i]-L[i] nhỏ nhất
- Cách tiếp cận 3: Chọn hoạt động ít giao với ít hoạt động khác nhất.
=> 3 hướng tiếp cận trên sẽ tồn tại nhược điểm
=> Giải thuật tham lam
```python
    Đặt N là số hoạt động và
    {I} là hoạt động thứ I  (1 <= I <= N)

    Với mỗi {I}, xét S[I] và F[I] lần lượt là thời gian bắt đầu và kết thúc của hoạt động đó.
    Sắp xếp lại các hoạt động theo thứ tự tăng dần của thời gian kết thúc.
    - Có nghĩa là, với I < J ta phải có F [I] <= F [J]

    //  A là tập hợp các hoạt động được chọn
    A = {1}
    //  J là hoạt động cuối cùng được chọn
    J = 1
    For I = 2  to N
    // ta có thể chọn I nếu nó là hoạt động cuối cùng
    // việc chọn lựa đã hoàn thành
    If S [I] >= F [J]
        // lựa chọn hoạt động 'I'
        A = A + {I}

        // hoạt động 'I' giờ trở thành hoạt động cuối cùng được lựa chọn
        J = I
    Endif
    Endfor

    Return A
```

## 1. Bài toán Wold Place
### Bài toán :
Cho n đất nước, mỗi nước có dân số của họ. Hãy chia thành các nhóm có k người không có cùng quốc tịch. Hãy cho biết số lượng tối đa có thể đạt được.
- Hướng tiếp cận thứ 1:
```python
Groups = 0
Repeat
  // sắp xếp lại mảng theo thứ tự giảm dần
  Sort (A)
  Min = A[K]
  If Min > 0
      Groups = Groups + 1
  For I = 1 to K
    A[I] = A[I] - 1
  Endfor
Until  Min = 0
Return Groups
```
=> Hướng giải quyết này cho kế t quả chính xác, nhưng tốc độ sẽ lâu và chậm
- Hướng tiếp cận thứ 2:
```python
Groups = 0
Repeat
  // sắp xếp lại mảng theo thứ tự giảm dần
  Sort (A)
  Min= A[K]
  Groups = Groups + Min
  For I = 1 to K
    A[I] = A[I] - Min
  Endfor
Until Min = 0
Return Groups
```
=> Hướng giải quyết này cho kết quả sai, nhưng tốc độ xử lý nhanh
- Hướng tiếp cận thứ 3
Giải quyết các khuyết điểm ở trên dùng phương pháp vét cạn
```python
Groups = 0
Repeat
// sắp xếp lại mảng theo thứ tự giảm dần
  Sort (A)
  Min = A[K]
  Allowance = (Min+999) / 1000
  Groups = Groups + Allowance
  For I = 1 to K
    A[I] = A[I] - Allowance
  Endfor
Until Min = 0
Return Groups
```
=> Giải thuật này có thể đúng hầu hết các trường hợp, song vẫn tồn tại một vài trường hợp sai

## Tổng kết :
- Giải thuật tham lam không phải lúc nào cũng cho kết quả đúng.
- Rủi ro cao hơn giải thuật quy hoạch động
- Đối với những bài toán mà có dữ liệu đầu vào lớn và rất lớn (kể cả độ phức tạp O(n^2)) thường dược dùng giải thuật tham lam hơn là quy hoạch động
