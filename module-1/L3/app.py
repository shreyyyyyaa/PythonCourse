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
                            6. Others
                            > 
                            """))

productCategoryName = ""

if productCategory == 1:
    productCategoryName = "Electronics"
elif productCategory == 2:
    productCategoryName = "Fashion"
elif productCategory == 3:
    productCategoryName = "Beauty"
elif productCategory == 4:
    productCategoryName = "Home and Kitchen"
elif productCategory == 5:
    productCategoryName = "Sports"
else:
    productCategoryName = "Others"

print(f"""
      Product Id: {productId}
      Product Name: {productName}
      Quantity: {quantity}
      Price: {price}
      Product Category: {productCategoryName}
      """)

if quantity <= 5:
    print("Low on stocks")