class Product:
    def __init__(self, name, description, price):
        self.name = name
        self.description = description
        self.price = price
        self.list_rating = []

    def view_info(self):
        print(f"Name: {self.name}\nDescription: {self.description}\nPrice: {self.price}")

    def add_rating(self, rating):
        self.list_rating.append(rating)

    def get_average_rating(self):
        if not self.list_rating:
            return 0
        return sum(self.list_rating) / len(self.list_rating)


class Shop:
    def __init__(self):
        self.list_product = []

    def add_product(self):
        name = input("Enter product name: ")
        description = input("Enter product description: ")
        price = float(input("Enter product price: "))
        product = Product(name, description, price)
        self.list_product.append(product)
        print("Product added successfully.")

    def remove_product(self):
        name = input("Enter product name to remove: ")
        for product in self.list_product:
            if product.name.lower() == name.lower():
                self.list_product.remove(product)
                print(f"{name} removed successfully.")
                return
        print(f"No product with name {name} found.")

    def view_product_list(self):
        print("Product List:")
        for product in self.list_product:
            print(f"Name: {product.name}, Price: {product.price}, Average Rating: {product.get_average_rating()}")

    def search_product(self):
        name = input("Enter product name to search: ")
        for product in self.list_product:
            if product.name.lower() == name.lower():
                print("Product found:")
                product.view_info()
                return
        print(f"No product with name {name} found.")


def main():
    shop = Shop()
    while True:
        print("\nPRODUCT MANAGEMENT SYSTEM")
        print("1. Add new product")
        print("2. Remove product")
        print("3. View product list")
        print("4. Search product")
        print("5. Exit")
        choice = input("Enter your choice: ")
        if choice == '1':
            shop.add_product()
        elif choice == '2':
            shop.remove_product()
        elif choice == '3':
            shop.view_product_list()
        elif choice == '4':
            shop.search_product()
        elif choice == '5':
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
