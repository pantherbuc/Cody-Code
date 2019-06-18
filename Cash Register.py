from math import *

customer_name = input("Enter your name: ")
price = input("Enter item price: ")
coupon = input("Enter Coupon percentage: ")

price_number = float(price)
coupon_number = float(coupon) / 10
coupon_number = (coupon_number / 10)

tax = .09
tax_text = tax * 100
print("------------------------------------------------------------------------------")
print("Welcome to Walmart " + customer_name + ",")
print("Your total cost with the state tax is " + (str(tax_text)) + "%, bringing your total cost to " + (str(price_number + (price_number * tax))))
print("With your coupon, the price is " + (str(price_number - (price_number * coupon_number) +  (price_number * tax))))
print("By using your coupon, you saved " + (str(price_number * coupon_number)))
