def cell_identity_at_time(t, k):
    # Hàm tính xác định tế bào tại thời điểm và vị trí cụ thể
    # Sử dụng đệ quy để giải quyết bài toán theo quy luật nhân bản tế bào

    # Base case: nếu thời điểm là 1, chỉ có một tế bào X
    if t == 1:
        return 'X'
    
    # Tính toán số lượng tế bào ở thời điểm trước đó
    prev_count = 2 ** (t - 2)
    
    # Nếu vị trí k lớn hơn hoặc bằng số lượng tế bào ở thời điểm trước đó,
    # thì vị trí k sẽ nằm trong phần sau khi tế bào Y bắt đầu xuất hiện
    if k >= prev_count:
        # Đối với phần này, vị trí k sẽ được tính lại theo phần sau khi tế bào Y bắt đầu xuất hiện
        new_k = k - prev_count
        # Nếu vị trí k chẵn, tế bào tại vị trí đó sẽ là X
        if new_k % 2 == 0:
            return 'X'
        # Ngược lại, nếu vị trí k lẻ, tế bào tại vị trí đó sẽ là Y
        else:
            return 'Y'
    # Nếu vị trí k nhỏ hơn số lượng tế bào ở thời điểm trước đó,
    # thì vị trí k sẽ nằm trong phần trước khi tế bào Y bắt đầu xuất hiện
    else:
        # Nếu vị trí k chẵn, tế bào tại vị trí đó sẽ là X
        if k % 2 == 0:
            return 'X'
        # Ngược lại, nếu vị trí k lẻ, tế bào tại vị trí đó sẽ là Y
        else:
            return 'Y'

# Đọc số lượng truy vấn
N = int(input())

# Đọc và xử lý từng truy vấn
for _ in range(N):
    a, b = map(int, input().split())
    # Gọi hàm để tính toán xác định tế bào
    result = cell_identity_at_time(a, b)
    # In kết quả
    print(result)
