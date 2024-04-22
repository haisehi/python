N = int(input())
A = [0] * 100
cot = [1] * 100
d1 = [1] * 100
d2 = [1] * 100
cnt = 0

def Try(i):
    global cnt
    for j in range(1, N + 1):
        print("Gọi Try (", i, "): j =", j)
        if cot[j] == 1 and d1[i - j + N] == 1 and d2[i + j - 1] == 1:
            print("Đặt quân hậu tại vị trí (", i, ",", j, ")")
            A[i] = j
            cot[j] = d1[i - j + N] = d2[i + j - 1] = 0
            if i == N:
                cnt += 1
            else:
                Try(i + 1)
            cot[j] = d1[i - j + N] = d2[i + j - 1] = 1
        else:
            print("Không đặt quân hậu được tại vị trí (", i, ",", j, ")")
    if i == 1:
        print("j =", N + 1, "> ", N, "nên thoát khỏi Try(", i, ") dừng lại")
    else:
        print("j =", N + 1, "> ", N, "nên thoát khỏi Try(", i, ") và quay lui khỏi đến Try(", i - 1, ")")

for i in range(1, 100):
    cot[i] = d1[i] = d2[i] = 1

Try(1)
print(cnt)
