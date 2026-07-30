def discount_price(item_name, original_price, promotional_code):

#    item_name = 0
#    original_price = 0
#    promotional_code = 0


    if(promotional_code == "SAVE10"):
        discount = 0.10
    elif(promotional_code == "HALFOFF"):
        discount = 0.50
    else:
        discount = 0


    discount_price = original_price - (original_price * discount)
    return discount_price

item_name = input("enter item name: ")

original_price = float(input("enter origial price: "))

promotional_code = input("enter promotional code: ")


price = discount_price(item_name, original_price, promotional_code)


print(f"Item Name: {item_name}")

print(f"Original Price: {original_price}")

print(f"discount_price: {price}")







        
