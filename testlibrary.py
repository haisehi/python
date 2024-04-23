# Định nghĩa cấu trúc biểu diễn cạnh
class Edge:
    def __init__(self, src, dest, weight):
        self.src = src
        self.dest = dest
        self.weight = weight

# Định nghĩa một lớp đại diện cho một đồ thị vô hướng có trọng số
class Graph:
    def __init__(self, V):
        self.V = V
        self.edges = []

    # Phương thức thêm cạnh vào đồ thị
    def addEdge(self, src, dest, weight):
        edge = Edge(src, dest, weight)
        self.edges.append(edge)

    # Phương thức tìm cây khung nhỏ nhất của đồ thị bằng thuật toán Kruskal
    def kruskalMST(self):
        # Hiển thị thông báo T = Ø ban đầu
        print("T = {}")

        # Sắp xếp các cạnh theo trọng số tăng dần
        self.edges.sort(key=lambda x: x.weight)

        # Khởi tạo tập T để lưu trữ cây khung nhỏ nhất
        T = []

        # Khởi tạo một vector lưu trữ cha của mỗi đỉnh
        parent = [-1] * self.V

        step = 0

        # Duyệt qua từng cạnh trong tập các cạnh đã sắp xếp
        for edge in self.edges:
            # Hiển thị thông tin về bước thực hiện và trạng thái của E và T
            print(f"T={step} <= {self.V} và E<> Ø")
            print(f"E = E\\({edge.src},{edge.dest},{edge.weight}) = ", end="{")
            
            # Tạo một set để lưu trữ các cạnh đã được chọn trong T
            selected_edges = set()
            for t in T:
                selected_edges.add((min(t.src, t.dest), max(t.src, t.dest)))

            # Xuất các cạnh trong E nếu chưa được chọn vào T
            for e in self.edges:
                if ((min(e.src, e.dest), max(e.src, e.dest)) not in selected_edges) and not (e.src == edge.src and e.dest == edge.dest and e.weight == edge.weight):
                    print(f"({e.src},{e.dest},{e.weight}) ", end="")
            print("}")

            # Tìm cha của đỉnh nguồn và đích của cạnh
            srcParent = self.find(parent, edge.src)
            destParent = self.find(parent, edge.dest)

            # Nếu cha của hai đỉnh này không giống nhau, tức là thêm cạnh này không tạo thành chu trình
            if srcParent != destParent:
                # Thêm cạnh vào cây khung
                T.append(edge)
                # Ghi nhận cha của đỉnh đích là đỉnh nguồn
                parent[srcParent] = destParent

                # Hiển thị T sau khi thêm cạnh mới
                print("T = {", end="")
                for i in range(len(T)):
                    print(f"({T[i].src},{T[i].dest},{T[i].weight})", end="")
                    if i != len(T) - 1:
                        print(", ", end="")
                print("}")

                # Tăng giá trị của step
                step += 1
            else:
                print(f"Vi canh ({edge.src},{edge.dest},{edge.weight}) tao thanh chu trinh nen khong them vao cay.")

            # Nếu số lượng cạnh trong cây khung đã đạt đến (V - 1), dừng thuật toán
            if len(T) == self.V - 1:
                break

        # Hiển thị cây khung nhỏ nhất và tổng trọng số
        print("T = {", end="")
        for i in range(len(T)):
            print(f"({T[i].src},{T[i].dest},{T[i].weight})", end="")
            if i != len(T) - 1:
                print(", ", end="")
        print("}")

        totalWeight = sum(edge.weight for edge in T)
        print(f"Tong trong so: {totalWeight}")

    # Phương thức tìm cha của một đỉnh trong cây
    def find(self, parent, i):
        if parent[i] == -1:
            return i
        return self.find(parent, parent[i])

if __name__ == "__main__":
    # Khởi tạo đồ thị với 6 đỉnh
    graph = Graph(9)

    # Thêm các cạnh vào đồ thị
    graph.addEdge(3, 5, 4)
    graph.addEdge(4, 6, 8)
    graph.addEdge(4, 5, 9)
    graph.addEdge(3, 4, 16)
    graph.addEdge(5, 6, 14)
    graph.addEdge(1, 3, 17)
    graph.addEdge(1, 2, 33)
    graph.addEdge(2, 3, 18)
    graph.addEdge(2, 4, 20)

    # Tìm cây khung nhỏ nhất và hiển thị kết quả
    graph.kruskalMST()
