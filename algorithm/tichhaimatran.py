#đoạn code dùng để chia để trị
def matrix_multiply(A, B):
    if len(A[0]) != len(B):
        return "Không thể nhân hai ma trận này"

    result = [[0 for _ in range(len(B[0]))] for _ in range(len(A))]

    for i in range(len(A)):
        for j in range(len(B[0])):
            for k in range(len(B)):
                result[i][j] += A[i][k] * B[k][j]

    return result

def input_matrix(size):
    matrix = []
    print(f"Nhập ma trận {size}:")
    for i in range(size[0]):
        row = list(map(int, input(f"Nhập hàng {i + 1} (các số cách nhau bằng dấu cách): ").split()))
        matrix.append(row)
    return matrix

num_matrices = int(input("Nhập số ma trận cần tính tích: "))

# Nhập kích thước của mỗi ma trận
sizes = []
for i in range(num_matrices):
    rows = int(input(f"Nhập số hàng của ma trận {i + 1}: "))
    cols = int(input(f"Nhập số cột của ma trận {i + 1}: "))
    sizes.append((rows, cols))

# Nhập và tính tích của các ma trận
matrices = []
for i in range(num_matrices):
    matrix = input_matrix(sizes[i])
    matrices.append(matrix)

# Tính tích của các ma trận
result_matrix = matrices[0]
for i in range(1, num_matrices):
    result_matrix = matrix_multiply(result_matrix, matrices[i])

# In kết quả của tích hai ma trận
print("Kết quả của tích các ma trận:")
for row in result_matrix:
    print(row)
