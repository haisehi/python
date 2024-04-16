def orientation(p, q, r):
    val = (q[1] - p[1]) * (r[0] - q[0]) - (q[0] - p[0]) * (r[1] - q[1])
    if val == 0:
        return 0  # thẳng hàng
    elif val > 0:
        return 1  # ngược chiều kim đồng hồ
    else:
        return 2  # cùng chiều kim đồng hồ

def convex_hull(points):
    n = len(points)
    if n < 3:
        return "Ít nhất phải có 3 điểm để tạo thành một bao đóng lồi"

    hull = []

    # Tìm điểm có hoành độ nhỏ nhất
    l = 0
    for i in range(1, n):
        if points[i][0] < points[l][0]:
            l = i

    p = l
    q = 0
    while True:
        hull.append(points[p])

        q = (p + 1) % n
        for i in range(n):
            if orientation(points[p], points[i], points[q]) == 2:
                q = i

        p = q

        if p == l:
            break

    return hull

# Ví dụ về sử dụng
points = [(0, 3), (2, 2), (1, 1), (2, 1), (3, 0), (0, 0), (3, 3)]
result = convex_hull(points)
print("Bao đóng lồi là:")
for point in result:
    print(point)
