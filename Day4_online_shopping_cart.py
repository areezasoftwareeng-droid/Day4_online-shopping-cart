# MINI PROJECT — ONLINE SHOPPING CART 🛒

# This project is INTERVIEW-READY.

# 📌 FEATURES

# ✔ Add products
# ✔ Remove products
# ✔ Apply discount
# ✔ Calculate total
# ✔ Checkout

# ------ Items database ------

items = {
    "Shirts" : {
        "T Shirts" : {
            "Red": {"S": 900, "M": 1000, "L": 1100},
            "White": {"S": 950, "M": 1050, "L": 1150},
            "Black": {"S": 1000, "M": 1100, "L": 1200},
            "Blue" : {"S": 1000, "M": 1100, "L": 1200},
        },
        "Polo Shirts" : {
            "Red": {"S": 900, "M": 1000, "L": 1100},
            "White": {"S": 950, "M": 1050, "L": 1150},
            "Black": {"S": 1000, "M": 1100, "L": 1200},
            "Blue" : {"S": 1000, "M": 1100, "L": 1200},
        },
        "Casual Shirts" : {
            "Red": {"S": 900, "M": 1000, "L": 1100},
            "White": {"S": 950, "M": 1050, "L": 1150},
            "Black": {"S": 1000, "M": 1100, "L": 1200},
            "Blue" : {"S": 1000, "M": 1100, "L": 1200},
        },
        "Baggy Shirts" : {
            "Red": {"S": 900, "M": 1000, "L": 1100},
            "White": {"S": 950, "M": 1050, "L": 1150},
            "Black": {"S": 1000, "M": 1100, "L": 1200},
            "Blue" : {"S": 1000, "M": 1100, "L": 1200},
        }
    },
    "Jeans" : {
        "Straight Jeans" : {
            "Blue": {"30": 2500, "32": 2600, "34": 2700},
            "Black": {"30": 2600, "32": 2700, "34": 2800}
        },
        "Baggy Jeans" : {
            "Blue": {"30": 2800, "32": 2900},
            "Black": {"30": 2900, "32": 3000}
        },
        "Skinny Pants" : {
            "Blue": {"32": 3000, "34": 3200},
            "Black": {"32": 3100, "34": 3300}
        },
        "Dress Pants" :{
            "Black": {"32": 3500, "34": 3700},
            "Grey": {"32": 3400, "34": 3600}
        }
    },
    "Shoes" : {
        "Joggers": {
            "White": {"41": 4000, "42": 4200},
            "Black": {"41": 4100, "42": 4300}
        },
        "Sneakers": {
            "Blue": {"41": 4500, "42": 4700},
            "White": {"41": 4600, "42": 4800}
        },
        "Boots": {
            "Brown": {"42": 6000, "43": 6200},
            "Black": {"42": 6100, "43": 6300}
        },
        "Loafers": {
            "Black": {"41": 5000, "42": 5200},
            "Brown": {"41": 5100, "42": 5300}
        }
    },
    "Jackets" : {
        "Leather Jacket": {
            "Black": {"M": 9000, "L": 9500},
            "Brown": {"M": 9200, "L": 9700}
        },
        "Denim Jacket": {
            "Blue": {"M": 6500, "L": 6800},
            "Black": {"M": 6700, "L": 7000}
        },
        "Puffers Jacket": {
            "Green": {"L": 8000, "XL": 8500},
            "Red": {"L": 8200, "XL": 8700}
        },
        "Coat": {
            "Grey": {"L": 10000, "XL": 11000},
            "Black": {"L": 10500, "XL": 11500}
        }
    }
}

# Cart 

cart = []

# Display all the items

def show_items():

    print("==== Available Items ====")
    
    for category, products in items.items():
        print(f"Category : {category}\n")

        for product_type, colors in products.items():
            print(f"Product_type : {product_type}\n")

            for color, sizes in colors.items():
                print(f"Color : {color}\n")

                for size , price in sizes.items():
                    print(f"Size : {size} | Price : {price}")

                print()

            print("-" * 45 )

# Show Category Menu

def show_menu():
    print("\nWhat do you want to order? ")
    print("1. Shirts")
    print("2. Jeans")
    print("3. Shoes")
    print("4. Jackets")
    print("5. Exit")
    choice = int(input("Enter your choice: "))
    if choice == 1:
        show_selected_items("Shirts")
    elif choice == 2:
        show_selected_items("Jeans")
    elif choice == 3:
        show_selected_items("Shoes")
    elif choice == 4:
        show_selected_items("Jackets")
    elif choice == 5:
        print("Thank you for visiting!")
    else:
        print("Please enter a valid choice")

# Show selected category items

def show_selected_items(category):
    
    print(f"\n=== {category.upper()} ===")

    for product_type, colors in items[category].items():
        print(f"\n{product_type}")

        for color, sizes in colors.items():
            print(f"  Color: {color}")

            for size, price in sizes.items():
                print(f"    Size: {size} | Price: Rs.{price}")

# Add Products to Menu

def add_products():
    print("\n Add Product to cart")

    # Asks for category
    category = input("Enter category (Shirts / Jeans / Shoes / Jackets): ").capitalize()

    if category not in items:
        print("Category not found")
        return
    
    # Asks for product type 
    print("\n Available Product Types")
    for p in items[category]:
        print("-" , p)
    
    product_type = input("Enter product type ").title().strip()
    if product_type not in items[category]:
        print("Product not found")
        return
    
    # Asks for color
    print("\nAvailable colors")
    for c in items[category][product_type]:
        print("-", c)

    color = input("Enter color").capitalize()
    if color not in items[category][product_type]:
        print("Color not found")
        return
    
    # Asks for size
    print("\nAvailable Sizes")
    for s in items[category][product_type][color]:
        print("-", s)

    size = input("Enter Size").capitalize()
    if size not in items[category][product_type][color]:
        print("Size not available")
        return

    # Asks for quantity 
    quantity = int(input("Enter quantity: "))

    price = items[category][product_type][color][size]

    cart.append(
        {
            "Category" : category,
            "Product_type" : product_type,
            "Color" : color,
            "Size" : size,
            "Quantity" : quantity,
            "Price" : price
        }
    )

    print("Product added to cart successfully")

# View Cart

def view_cart():
    if not cart: 
        print("\nYour cart is empty")
        return
    
    print("\n===== YOUR CART =====")

    Total = 0

    for i, item in enumerate(cart, 1):
        item_total = item["Price"] * item["Quantity"]
        Total += item_total

        print(f"\nItem {i}")
        print(f"Category     : {item['Category']}")
        print(f"Product Type : {item['Product_type']}")
        print(f"Color        : {item['Color']}")
        print(f"Size         : {item['Size']}")
        print(f"Quantity     : {item['Quantity']}")
        print(f"Price (each) : Rs.{item['Price']}")
        print(f"Item Total   : Rs.{item_total}")
        print("-" * 30)

    print(f"\nCart Total Amount: Rs.{Total}\n")

# Remove items from cart

def remove_products():
    if not cart:
        print("Your cart is empty. Nothing to remove.")
        return
    
    view_cart()

    choice = int(input("\nEnter item number to remove: "))
    if choice < 1 or choice > len(cart):
        print("Invalid choice")
        return

    removed_item = cart.pop(choice - 1)

    print(f"\n{removed_item['Product_type']} removed from cart successfully!")

# Apply discounts

def apply_discounts():
    if not cart:
        print("\nYour cart is empty. No discount applied.")
        return

    total = 0
    for item in cart:
        total += item["Price"] * item["Quantity"]

    discount_percent = 20
    discount_amount = total * (discount_percent / 100)
    final_amount = total - discount_amount

    print("\n===== DISCOUNT APPLIED =====")
    print(f"Original Total : Rs.{total}")
    print(f"Discount       : {discount_percent}%")
    print(f"You Save       : Rs.{discount_amount}")
    print(f"Final Amount   : Rs.{final_amount}")

#Calculate Total

def calculate_total():
    if not cart:
        print("\nYour cart is empty")
        return

    total_amount = 0

    for item in cart:
        item_total = item["Price"] * item["Quantity"]
        total_amount += item_total

    print(f"\nTotal Amount to Pay: Rs.{total_amount}")

# Checkout

def checkout():
    if not cart:
        print("\nYour cart is empty. Nothing to checkout.")
        return

    print("\n====== CHECKOUT ======")

    # Show final cart
    view_cart()

    # Calculate final total
    total = 0
    for item in cart:
        total += item["Price"] * item["Quantity"]

    print(f"Final Amount to Pay: Rs.{total}")

    # Payment confirmation
    confirm = input("\nProceed to payment? (yes/no): ").lower()

    if confirm == "yes":
        print("\nPayment successful ✅")
        print("Thank you for shopping with us! 🛒")
        cart.clear()
        print("Cart cleared. Goodbye!")
    else:
        print("\nCheckout cancelled. You can continue shopping.")

# -------- <Main Menu ------

print("=== Welcome to Online Shopping Mart ===")
show_items()
show_menu()

while True:
    print("2. Add products")
    print("3. View Cart")
    print("4. Remove Products")
    print("5. Apply discounts")
    print("6. Calculate total")
    print("7. Checkout")
    print("8. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 2:
        add_products()
    elif choice == 3:
        view_cart()
    elif choice == 4:
        remove_products()
    elif choice == 5:
        apply_discounts()
    elif choice == 6:
        calculate_total()
    elif choice == 7:
        checkout()
    elif choice == 8:
        print("Thank You for shopping!")
        break
    else:
        print("Invalid choice")
        