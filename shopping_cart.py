# shopping_cart.py

# Requirements 

#grocery store name of your choice
#grocery store phone number and/or website URL and/or address of choice
#date and time of the beginning of the checkout process, formatted in a human-friendly way (e.g. 2020-02-07 03:54 PM)
#name and price of each shopping cart item, price being formatted as US dollars and cents (e.g. $3.50, etc.)
#total cost of all shopping cart items (i.e. the "subtotal"), formatted as US dollars and cents (e.g. $19.47), calculated as the sum of their prices
#amount of tax owed (e.g. $1.70), calculated by multiplying the total cost by a New York City sales tax rate of 8.75% (for the purposes of this project, groceries are not exempt from sales tax)
#total amount owed, formatted as US dollars and cents (e.g. $21.17), calculated by adding together the amount of tax owed plus the total cost of all shopping cart items
#friendly message thanking the customer and/or encouraging the customer to shop again

products = [
    {"id":1, "name": "Chocolate Sandwich Cookies", "department": "snacks", "aisle": "cookies cakes", "price": 3.50},
    {"id":2, "name": "All-Seasons Salt", "department": "pantry", "aisle": "spices seasonings", "price": 4.99},
    {"id":3, "name": "Robust Golden Unsweetened Oolong Tea", "department": "beverages", "aisle": "tea", "price": 2.49},
    {"id":4, "name": "Smart Ones Classic Favorites Mini Rigatoni With Vodka Cream Sauce", "department": "frozen", "aisle": "frozen meals", "price": 6.99},
    {"id":5, "name": "Green Chile Anytime Sauce", "department": "pantry", "aisle": "marinades meat preparation", "price": 7.99},
    {"id":6, "name": "Dry Nose Oil", "department": "personal care", "aisle": "cold flu allergy", "price": 21.99},
    {"id":7, "name": "Pure Coconut Water With Orange", "department": "beverages", "aisle": "juice nectars", "price": 3.50},
    {"id":8, "name": "Cut Russet Potatoes Steam N' Mash", "department": "frozen", "aisle": "frozen produce", "price": 4.25},
    {"id":9, "name": "Light Strawberry Blueberry Yogurt", "department": "dairy eggs", "aisle": "yogurt", "price": 6.50},
    {"id":10, "name": "Sparkling Orange Juice & Prickly Pear Beverage", "department": "beverages", "aisle": "water seltzer sparkling water", "price": 2.99},
    {"id":11, "name": "Peach Mango Juice", "department": "beverages", "aisle": "refrigerated", "price": 1.99},
    {"id":12, "name": "Chocolate Fudge Layer Cake", "department": "frozen", "aisle": "frozen dessert", "price": 18.50},
    {"id":13, "name": "Saline Nasal Mist", "department": "personal care", "aisle": "cold flu allergy", "price": 16.00},
    {"id":14, "name": "Fresh Scent Dishwasher Cleaner", "department": "household", "aisle": "dish detergents", "price": 4.99},
    {"id":15, "name": "Overnight Diapers Size 6", "department": "babies", "aisle": "diapers wipes", "price": 25.50},
    {"id":16, "name": "Mint Chocolate Flavored Syrup", "department": "snacks", "aisle": "ice cream toppings", "price": 4.50},
    {"id":17, "name": "Rendered Duck Fat", "department": "meat seafood", "aisle": "poultry counter", "price": 9.99},
    {"id":18, "name": "Pizza for One Suprema Frozen Pizza", "department": "frozen", "aisle": "frozen pizza", "price": 12.50},
    {"id":19, "name": "Gluten Free Quinoa Three Cheese & Mushroom Blend", "department": "dry goods pasta", "aisle": "grains rice dried goods", "price": 3.99},
    {"id":20, "name": "Pomegranate Cranberry & Aloe Vera Enrich Drink", "department": "beverages", "aisle": "juice nectars", "price": 4.25}
] # based on data from Instacart: https://www.instacart.com/datasets/grocery-shopping-2017

from datetime import datetime
now = datetime.now()

def to_usd(my_price):
    return f"${my_price:,.2f}" #> $12,000.71

#
# INFO CAPTURE 
#

#must ensure selected ID from the input function and the "id" are same datatype
subtotal = 0
selected_ids = [] 

while True: 
    selected_id = input("Please input a product identifier or DONE if there are no more items:")
    if selected_id == "DONE": 
        break
    else: 
        selected_ids.append(selected_id)

# 
# INFO DISPLAY / OUTPUT 
# 

#print(selected_ids)
for selected_id in selected_ids: 
    matching_products = [i for i in products if str(i["id"]) == str(selected_id)]
    matching_product = matching_products[0]
    subtotal = subtotal + matching_product["price"]
    print("SELECTED PRODUCT:", matching_product["name"], to_usd(matching_product["price"]))

print()
print("SUBTOTAL:", to_usd(subtotal))

#
# LET'S FIND TAX 
# Multiply total cost by NYC sales tax rate of 8.75% 

tax = subtotal * 0.0875

print("TAX:", (to_usd(tax)))

#
# OUR RECEIPT 
#

print("---------------------------------")
print("VILLA MARKET GROCERIES")
print("WWW.VILLA-MARKET-GROCERIES.COM")
print("------------------------------")

print("CHECKOUT AT:", now.strftime("%Y-%m-%d %H:%M:%S"))
print("------------------------------")


#> SELECTED PRODUCTS:
#>  ... Chocolate Sandwich Cookies ($3.50)
#>  ... All-Seasons Salt ($4.99)
#>  ... Robust Golden Unsweetened Oolong Tea ($2.49)
#>  ... All-Seasons Salt ($4.99)
#>  ... Chocolate Sandwich Cookies ($3.50)
#> ---------------------------------


#> SUBTOTAL: $19.47
#> TAX: $1.70
#> TOTAL: $21.17


print("THANKS, SEE YOU AGAIN SOON!")
print("--------------------------------")