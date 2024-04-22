N = 0
A = []

def inkq():
    global A
    for i in range(1, N + 1):
        print(A[i], end="")
    print()

def Try(i):
    global A
    for j in range(2):
        print("Try(", i, ") j=", j, end=" ") 
        A[i] = j
        print("x[", i, "]=", j, end=" ")
        if i == N:
            print("i=", i, "= n =", N, "nên xuất ", end="")
            inkq()
        else:
            print("i=", i, "< n =", N, "nên gọi")
            Try(i + 1)
    if i == 1:
        print("                  j = 2 > 1 nên thoát khỏi Try(", i, ") dừng lại")
    else:
        print("                  j = 2 > 1 nên thoát khỏi Try(", i, ") và quay lui đến Try(", i - 1, ")")

if __name__ == "__main__":
    N = int(input())
    A = [0] * (N + 1)
    Try(1)
