stock_list = ["laptop", "mouse", "keyboard", "monitor"]
item = input("Enter item name to buy: ")

if item in stock_list:
    print("Item is in stock!")
else:
    print("Sorry item is out of stock.")