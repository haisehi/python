class Graph:
    def __init__(self, vertices, edges, weights):
        self.V = vertices
        self.E = edges
        self.weights = weights

    # Bước 1: Sắp xếp các cạnh theo trọng số không giảm
    def sort_edges(self):
        sorted_edges = sorted(zip(self.E, self.weights), key=lambda x: x[1])
        self.E, self.weights = zip(*sorted_edges)
        self.E = list(self.E)  # Convert tuple to list
        self.weights = list(self.weights)  # Convert tuple to list

    # Bước 2: Thực hiện thuật toán Kruskal
    def kruskal_algo(self):
        T = []
        total_length = 0
        parent = [-1] * self.V  # Initialize parent array for union-find

        # Utility function to find set of an element (uses path compression)
        def find(parent, i):
            if parent[i] == -1:
                return i
            return find(parent, parent[i])

        # Utility function to perform union of two sets (uses union by rank)
        def union(parent, x, y):
            xroot = find(parent, x)
            yroot = find(parent, y)
            parent[xroot] = yroot

        step = 1
        while len(T) < self.V - 1 and self.E:
            print(f"ITIE={step}<= {self.V} và E<> Ø\n")
            print(f"E = E\{self.E[0]} = {self.E}")
            edge = self.E.pop(0)
            weight = self.weights.pop(0)
            x = find(parent, edge[0] - 1)
            y = find(parent, edge[1] - 1)
            if x != y:
                T.append(edge)
                total_length += weight
                union(parent, x, y)
                print(f"T={T}\n")
            else:
                print(f"Vì cạnh {edge} tạo thành chu trình nên không thêm vào cây.\n")
            step += 1

        return T, total_length


# Cạnh và trọng số tương ứng
edges = [(3, 5), (4, 6), (4, 5), (5, 6), (3, 4), (1, 3), (2, 3), (2, 4), (1, 2)]
weights = [4, 8, 9, 14, 16, 17, 18, 20, 33]

# Khởi tạo đồ thị và sắp xếp các cạnh
g = Graph(6, edges, weights)
g.sort_edges()

# Thực hiện Kruskal
T, total_length = g.kruskal_algo()

# In kết quả
print("Các cạnh trong cây bao trùm nhỏ nhất:")
for edge in T:
    print(edge)
print("Tổng độ dài của cây bao trùm nhỏ nhất:", total_length)
