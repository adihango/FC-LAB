class Product:
    def __init__(self, name, price, stock_quantity):
        self.name = name
        self.price = price
        self.stock_quantity = stock_quantity

    def __str__(self):
        return f"{self.name} (Price: ₹{self.price}, Stock: {self.stock_quantity})"

class CartItem:
    def __init__(self, product, quantity):
        self.product = product
        self.quantity = quantity

    def __str__(self):
        return f"{self.product.name} x {self.quantity}"

class ShoppingCart:
    def __init__(self):
        self.cart_items = []

    def add_to_cart(self, product):
        for item in self.cart_items:
            if item.product == product:
                item.quantity += 1
                return
        self.cart_items.append(CartItem(product, 1))

    def remove_from_cart(self, product):
        for i, item in enumerate(self.cart_items):
            if item.product == product:
                if item.quantity > 1:
                    item.quantity -= 1
                else:
                    self.cart_items.pop(i)
                return
        print(f"{product.name} is not in the cart.")

    def view_cart(self):
        print("Your Cart:")
        for item in self.cart_items:
            print(item)
        total_price = sum(item.product.price * item.quantity for item in self.cart_items)
        print(f"Total Price: ₹{total_price}")

    def checkout(self):
        total_price = 0
        for item in self.cart_items:
            if item.product.stock_quantity >= item.quantity:
                item.product.stock_quantity -= item.quantity
                total_price += item.product.price * item.quantity
            else:
                print(f"Insufficient stock for {item.product.name}.")
                return
        print(f"Checkout successful. Total Price: ₹{total_price}")
        self.cart_items = []

# Create some sample products
products = [
    Product("Laptop", 50000, 10),
    Product("Smartphone", 30000, 20),
    Product("Headphones", 5000, 50)
]

# Create a shopping cart
cart = ShoppingCart()

# Add items to the cart
cart.add_to_cart(products[0])
cart.add_to_cart(products[1])
cart.add_to_cart(products[2])
cart.add_to_cart(products[2])

# View the cart
cart.view_cart()

# Checkout
cart.checkout()