print("""
**********************************************************************
-----------------Welcome to the Inventory System!---------------------
About us: This system helps you manage your products efficiently.
Contact us: Shreya - 9999999999
**********************************************************************
Let's get started!""")

productId = int(input("Enter the Product Id: "))
productName = input("Enter the Product Name: ")
quantity = int(input("Enter the Quantity: "))
price = float(input("Enter the price per unit: "))
productCategory = int(input("""
                            Enter the product category number:
                            1. Electronics
                            2. Fashion
                            3. Beauty
                            4. Home and Kitchen 
                            5. Sports
                            > 
                            """))

print(f"""
      ProductId: {productId}
      ProductName: {productName}
      Quantity: {quantity}
      Price: {price}
      Product Category: {productCategory}
      """)

