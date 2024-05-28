def find_cell_position(n, k):
    # Hàm này tính vị trí của tế bào tại thời điểm n và vị trí k
    # Ban đầu chỉ có 1 tế bào X, nên tất cả các vị trí từ 1 đến 2^(n-1) là X
    # Các vị trí từ 2^(n-1)+1 đến 2^n là Y
    # Tính toán theo quy luật nhân bản

    # Lặp lại quá trình nhân bản cho đến khi vị trí k được tìm thấy
    while n > 0:
        half_range = 2**(n-1)
        # Nếu k nằm trong phần bên trái của dãy tế bào, đó là phần X
        if k <= half_range:
            # Nếu k là vị trí đầu tiên hoặc là số lẻ, tế bào ở vị trí đó là X
            if k == 1 or k % 2 == 1:
                return 'X'
            # Nếu k là số chẵn, tế bào ở vị trí đó là Y
            else:
                return 'Y'
        # Nếu k nằm trong phần bên phải của dãy tế bào, đó là phần Y
        else:
            # Chuyển vị trí k sang phần bên trái của dãy tế bào
            k -= half_range
            # Đảo ngược nếu k nằm trong phần Y
            k = half_range + 1 - k
            # Giảm giá trị của n đi 1 vì bước nhân bản tiếp theo
            n -= 1
# Đọc số lượng truy vấn
N = int(input())

# Đọc và xử lý từng truy vấn
for _ in range(N):
    n, k = map(int, input().split())
    # Tìm vị trí của tế bào và in ra kết quả tương ứng
    print(find_cell_position(n, k))


