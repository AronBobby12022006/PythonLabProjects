inventory=[
    ("Laptop",10,35000.00),
    ("Mobile Phone",35,15000),
    ("Headphones",80,500),
    ("Monitor",8,3000),
]
highest_stock_value=0
item_with_highest_stock_value=None
for item in inventory:
    item_name,quantity,cost=item
    stock_value=quantity*cost
    print(f" Item name:{item_name},the stock value is:{stock_value}")
    if stock_value>highest_stock_value:
        highest_stock_value=stock_value
        item_with_highest_stock_value=item_name
print(f"highest stock valueis:{highest_stock_value}")
print(f"Item with highest stock value is :{item_with_highest_stock_value}")