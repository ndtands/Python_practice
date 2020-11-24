# Các giải thuật Sort
## Sắp xếp nổi bọt (Bubble sort)
- Xét lần lượt các cặp 2 phần tử liên tiếp. Nếu phần tử đứng sau nhỏ hơn phần tử đứng trước, ta đổi chỗ 2 phần tử. Nói cách khác, phần tử nhỏ nhất sẽ nổi lên trên.
- Lặp lại đến khi không còn 2 phần tử nào thỏa mãn. Có thể chứng minh được số lần lặp không quá N−1, do một phần tử chỉ có thể nổi lên trên không quá N−1 lần.
- Độ phức tạp O(N*N)
## Sắp xếp chèn (Insertion Sort)
- Ý tưởng chính của thuật toán là ta sẽ sắp xếp lần lượt từng đoạn gồm 1 phần tử đầu tiên, 2 phần tử đầu tiên, …, N phần tử.
- Giả sử ta đã sắp xếp xong i phần tử của mảng. Để sắp xếp i+1 phần tử đầu tiên, ta tìm vị trí phù hợp của phần tử thứ i+1 và "chèn" nó vào đó.
- Độ phức tạp O(N*N)
## Sắp xếp trộn (Merge sort)
- Chia dữ liệu thành 2 phần và sắp xếp từng phần
- Sau đó gộp 2 phần lại với nhau. Để gộp 2 phần, ta làm như sau:
    + Tạo một dãy A mới để chứa các phần tử đã sắp xếp.
    + So sánh 2 phần tử đầu tiên của 2 phần. Phần tử nhỏ hơn ta cho vào A và xóa khỏi phần tương ứng.
    + Tiếp tục như vậy đến khi ta cho hết các phần tử vào dãy A.
- Độ phức tạp O(N*log(N))
## Sắp xếp vun đống (HeapSort)
- Ta lưu mảng vào CTDL Heap.
- Ở mỗi bước, ta lấy ra phần tử nhỏ nhất trong heap, cho vào mảng đã sắp xếp.
- Độ phức tạp O(N*log(N))
## Sắp xếp nhanh (QuickSort)
- Chia dãy thành 2 phần, một phần "lớn" và một phần "nhỏ".
    + Chọn một khóa pivot
    + Những phần tử lớn hơn pivot chia vào phần lớn
    +Những phần tử nhỏ hơn hoặc bằng pivot chia vào phần nhỏ.
- Gọi đệ quy để sắp xếp 2 phần.
- Độ phức tạp có thể là O(N.N) hoặc O(N.log(N) nếu chia 2 phần không tốt
## Sắp xếp cơ số (RadixSort)
- Khác với tất cả các thuật toán nêu trên, RadixSort không sử dụng việc so sánh 2 phần tử.
    + Đầu tiên, thuật toán sẽ chia các phần tử thành các nhóm, dựa trên chữ số cuối cùng (hoặc dựa theo bit cuối cùng, hoặc vài bit cuối cùng).
    +Sau đó ta đưa các nhóm lại với nhau, và được danh sách sắp xếp theo chữ số cuối của các phần tử. Quá trình này lặp đi lặp lại với chữ số át cuối cho tới khi tất cả vị trí chữ số đã sắp xếp.
- Độ phức tạp O(N*log(max(a_i)))
- Cái này không thể sắp xếp số thực