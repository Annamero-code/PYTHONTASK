def discount_sales(item_name, original_price, promotional_code):
    item_name = 0
    original_price = 0
    promotional_code = 0

if(promotional_code == "SAVE10"):
    discount = 10
elif(promotion_code == "HALFOFF"):
    dicount = 0.50
else:
    dicount = 0

discount = original_price - (original_price * dicount)
 
item_name = input("enter item name: ")

original_price = int(input("enter the price: "))

promotional_code = input("enter promotional code")


final_price = discount_sales(item_name, original_price, promotional_code)


print(f"Item Name: {item_name}")

print(f"Original Price: {original_price}")

print(f"Promotional Code: {promotional_code}")

print(f"Final Price: {final_price}")



