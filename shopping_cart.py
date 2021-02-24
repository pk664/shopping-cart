# shopping_cart.py

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

from dotenv import load_dotenv
load_dotenv()
import os 

def to_usd(my_price):
    return f"${my_price:,.2f}" 

#
# INFO CAPTURE 
#

print("Welcome to Villa Market Groceries!")
print()

TAX_RATE = os.getenv("TAX_RATE", default = 0.0875)

# This code was adapted from Prof Rossetti's screencast 

subtotal = 0
selected_ids = [] 

while True: 
    selected_id = input("Please input a product identifier or DONE if there are no more items:")
    if selected_id == "DONE" or selected_id == "done":
        break
    if int(selected_id) >= 1 and int(selected_id) <= 20:
        selected_ids.append(selected_id)
    else: 
        print("Oops, that's an invalid input. Please try again!")


# 
# INFO DISPLAY / OUTPUT 
# 

print("---------------------------------")
print("VILLA MARKET GROCERIES")
print("WWW.VILLA-MARKET-GROCERIES.COM")
print("------------------------------")

print("CHECKOUT AT:", now.strftime("%Y-%m-%d %H:%M:%S"))
print("------------------------------")

print("SELECTED PRODUCTS:")

for selected_id in selected_ids: 
    matching_products = [i for i in products if str(i["id"]) == str(selected_id)]
    if (len(matching_products) != 0):
        matching_product = matching_products[0]
        subtotal = subtotal + matching_product["price"]
        print("+", matching_product["name"], to_usd(matching_product["price"]))

#
# RECEIPT 
# 

print()
print("SUBTOTAL:", to_usd(subtotal))

x = str(float(TAX_RATE)*100)

print("SELECTED TAX RATE: " + x + "%")
tax_amount = float(subtotal) * float(TAX_RATE)


print("TAX AMOUNT:", (to_usd(tax_amount)))
total_price = tax_amount + subtotal 
print()
print("TOTAL:", to_usd(total_price))


print("--------------------------------")
print("Thanks for visiting Villa! Please come again.")
print("--------------------------------")