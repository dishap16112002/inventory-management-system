products = []

def add_product():
    product = {
        "id": input("Enter Product ID: "),
        "name": input("Enter Product Name: "),
        "category": input("Enter Category: "),
        "quantity": int(input("Enter Quantity: ")),
        "price": float(input("Enter Price: "))
    }

    products.append(product)
    print("\n✅ Product Added Successfully!")
def view_products():
    if len(products) == 0:
        print("\n❌ No Products Found!")
    else:
        print("\n========== PRODUCT LIST ==========")
        for product in products:
            print(f"ID       : {product['id']}")
            print(f"Name     : {product['name']}")
            print(f"Category : {product['category']}")
            print(f"Quantity : {product['quantity']}")
            print(f"Price    : ₹{product['price']}")
            print("-" * 35)


def search_product():
    product_id = input("Enter Product ID to Search: ")

    found = False

    for product in products:
        if product["id"] == product_id:
            print("\n✅ Product Found")
            print(f"ID       : {product['id']}")
            print(f"Name     : {product['name']}")
            print(f"Category : {product['category']}")
            print(f"Quantity : {product['quantity']}")
            print(f"Price    : ₹{product['price']}")
            found = True
            break

    if not found:
        print("\n❌ Product Not Found!")
    def update_product():
         product_id = input("Enter Product ID to Update: ")

    found = False

    for product in products:
        if product["id"] == product_id:

            print("Leave blank if you don't want to change a value.")

            new_name = input("Enter New Name: ")
            new_category = input("Enter New Category: ")
            new_quantity = input("Enter New Quantity: ")
            new_price = input("Enter New Price: ")

            if new_name:
                product["name"] = new_name

            if new_category:
                product["category"] = new_category

            if new_quantity:
                product["quantity"] = int(new_quantity)

            if new_price:
                product["price"] = float(new_price)

            print("\n✅ Product Updated Successfully!")
            found = True
            break

    if not found:
        print("\n❌ Product Not Found!")


def delete_product():
    product_id = input("Enter Product ID to Delete: ")

    found = False

    for product in products:
        if product["id"] == product_id:
            products.remove(product)
            print("\n✅ Product Deleted Successfully!")
            found = True
            break

    if not found:
        print("\n❌ Product Not Found!")
while True:
    print("\n========== INVENTORY MANAGEMENT SYSTEM ==========")
    print("1. Add Product")
    print("2. View Products")
    print("3. Search Product")
    print("4. Update Product")
    print("5. Delete Product")
    print("6. Exit")

    choice = input("Enter Your Choice: ")

    if choice == "1":
        add_product()

    elif choice == "2":
        view_products()

    elif choice == "3":
        search_product()

    elif choice == "4":
        update_product()

    elif choice == "5":
        delete_product()

    elif choice == "6":
        print("\n🙏 Thank You For Using Inventory Management System!")
        break

    else:
        print("\n❌ Invalid Choice! Please Try Again.")