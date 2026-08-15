print("===== Shopping System Cart =====")
print("1. Add Product ")
print("2. View Cart ")
print("3. Remove Product")
print("4. bill ")
print("5. Exit")
product=[]
price=[]
# func to add add_product
def add_product():
    name=input("Enter your product name: ").split(",")
    pay=list(map(int,input("Enter the product prices: ").split(",")))
    for i in range(len(name)):
        product.append(name[i].strip())
        price.append(pay[i])
    print("Product added successfully")
    # func view_cart
def  view_cart():
     if len(product)==0:
          print("Cart is empty")
     else:
          for i in range(len(product)):
             print(f"{product[i]} added to the cart with their prices {price[i]} ")
            # functo  remove_product
def remove_product():
    if len(product) == 0:
        print("Cart is empty")
    else:
        remove = input("Enter the product that you want to remove from the cart: ").strip()

        if remove in product:
            position = product.index(remove)
            product.pop(position)
            price.pop(position)

            print("Product removed successfully")
            print(product)
        else:
            print("Product not found in the cart")
            # func to total_bill
def total_bill():
    if len(product)==0:
        print("Cart is empty")
    else:
        total=sum(price)
        print(f"Your total is {total}")
while True:
     choice=int(input("Enter your choices: "))
     if choice==1:
       add_product()
     elif choice==2:
       view_cart()
     elif choice==3:
         remove_product()
     elif choice==4:
         total_bill()
     elif choice==5:
         print("Exit")
         break
     else:
         print("INVALID COMMANDS")
