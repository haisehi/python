#quy hoach dong: nhan n ma tran
import sys

# Hàm tính toán tối ưu cho tích của bốn ma trận và hiển thị phân tích kết quả
def optimalMatrixProduct(a, F, split, n):
    for d in range(1, n):
        for i in range(1, n - d + 1):
            j = i + d
            F[i][j] = sys.maxsize
            for k in range(i, j):
                cost = F[i][k] + F[k + 1][j] + a[i - 1] * a[k] * a[j]
                if cost < F[i][j]:
                    F[i][j] = cost
                    split[i][j] = k

    # In phân tích kết quả
    print(f"Ta có a = ({', '.join(map(str, a))}).")
    for d in range(1, n):
        print(f"Với d = {d}:")
        for i in range(1, n - d + 1):
            j = i + d
            print(f"F[{i},{j}] = ", end="")
            if d > 1:
                print("min(", end="")
                for k in range(i, j):
                    print(f"F[{i},{k}] + F[{k + 1},{j}] + {a[i - 1]} x {a[k]} x {a[j]}", end="")
                    if k != j - 1:
                        print(", ", end="\n             ")
                print("", end="\n       = min(")
                for k in range(i, j):
                    print(F[i][k] + F[k + 1][j] + a[i - 1] * a[k] * a[j], end="")
                    if k != j - 1:
                        print(", ", end="")
                print(f") = {F[i][j]}")
            else:
                print(F[i][j])

    return F[1][n]

# Hàm in dấu ngoặc đúng vị trí để nhân các ma trận
def printParenthesis(split, i, j):
    if i == j:
        print(f"A{i}", end="")
        return

    print("(", end="")
    printParenthesis(split, i, split[i][j])
    printParenthesis(split, split[i][j] + 1, j)
    print(")", end="")

a = [20, 2, 30, 12, 8]
n = len(a) - 1

# Khởi tạo ma trận F và split
F = [[0] * (n + 1) for _ in range(n + 1)]
split = [[0] * (n + 1) for _ in range(n + 1)]

# Gọi hàm tính toán và in ra kết quả
minOperations = optimalMatrixProduct(a, F, split, n)

# In ra các ma trận và tích của chúng
print("Ma trận F:")
print("    ", end="")
for j in range(1, n + 1):
    print(j, "  ", end="")
print()
for i in range(1, n + 1):
    print(i, "|", end=" ")
    for j in range(1, n + 1):
        print(F[i][j], end="  ")
    print()

print("Ma trận split:")
print("    ", end="")
for j in range(1, n + 1):
    print(j, "  ", end="")
print()
for i in range(1, n + 1):
    print(i, "|", end=" ")
    for j in range(1, n + 1):
        print(split[i][j], end="  ")
    print()

print("Phép nhân ma trận tối ưu: ", end="")
printParenthesis(split, 1, n)
print(" =", minOperations)
