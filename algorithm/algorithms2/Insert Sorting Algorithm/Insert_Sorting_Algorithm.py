import sys

def sort(arrays):
    length = len(arrays)
    # insert_position - 1: Giá trị khởi đầu của vòng lặp là vị trí trước đó của phần tử được chọn.
    # -1: Đây là giới hạn dưới của vòng lặp
    # -1: Đây là bước lùi của vòng lặp
    for i in range(0, length - 1):
        insert_element = arrays[i]  # Lấy phần tử mới chưa được sắp xếp
        insert_position = i  # Vị trí cần chèn
        for j in range(insert_position - 1, -1, -1):
            # Nếu phần tử mới nhỏ hơn phần tử đã sắp xếp, dịch phần tử đã sắp xếp sang phải
            if insert_element < arrays[j]:
                arrays[j + 1] = arrays[j]
                insert_position -= 1
        arrays[insert_position] = insert_element  # Chèn phần tử mới

def main():
    scores = [80, 70, 60, 50, 95]
    sort(scores)
    for score in scores:
        print(score, ",", end="")

if __name__ == "__main__":
    main()
