def addProduct():
    
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

    return productId,productName,quantity,price,productCategoryName

def checkStockQuantity(quantity):

    if quantity <= 5:
        print("low on stocks")

def selection():
    selection = int(input("""
    1. Add Product
    2. Search Product by Id 
    > 
          """))
     
    return selection

def searchProductById(pId, productId):
    ind=productId.index(pId)
    return ind


    
def main():
    print("""
**********************************************************************
-----------------Welcome to the Inventory System!---------------------
About us: This system helps you manage your products efficiently.
Contact us: Shreya - 9999999999
**********************************************************************
Let's get started!""")
    
    x = selection()
    product = [
        {
            "productId": 1,
            "productName": "Shoes",
            "quantity": 10,
            "price": 20000,
            "productCategoryName": "Sports"
        },
        {
            "productId": 2,
            "productName": "Flour",
            "quantity": 9,
            "price": 300,
            "productCategoryName": "Home and Kitchen"
        },
        {
            "productId": 3,
            "productName": "Skirt",
            "quantity": 6,
            "price": 5000,
            "productCategoryName": "Fashion"
        }
    ]
    
    if x == 1:
        pId,pName,qty,priceX,pCName = addProduct()

        new_product = {
            "productId": pId,
            "productName": pName,
            "quantity": qty,
            "price": priceX,
            "productCategoryName": pCName

        }

        product.append(new_product)

        print(f"""
            You have added the product 
              {new_product}
              """)

        # displayProduct(new_prod


        # print(f""" You have added the product
        #     Product Id: {pId}
        #     Product Name: {pName}
        #     Quantity: {qty}
        #     Price: {priceX}
        #     Product Category: {pCName}
        #     """)
        checkStockQuantity(qty)
    
    # elif x == 2:
    #     pId=int(input("Enter the product Id: "))

        # ind = searchProductById(pId, productId)
        # print(f"""
        #     Product details: 
        #     Product Id: {pId}
        #     Product Name: {productName[ind]}
        #     Quantity: {quantity[ind]}
        #     Price: {price[ind]}
        #     Product Category: {productCategoryName[ind]}
        #       """)

    else:
        print("wrong input")
        
main()

