sale_price = 29.99

# Define a lambda function called add_tax
add_tax = (lambda x: x * 1.2)

# Call the lambda function
print(add_tax(sale_price))

sale_price = 29.99

# Call a lambda function adding 20% to sale_price
print((lambda x: x * 1.2) (sale_price))


sales_prices = [29.99, 9.95, 14.50, 39.75, 60.00]

# Create add_taxes to add 20% to each item in sales_prices
add_taxes = map(lambda x: x * 1.2, sales_prices)

# Create the updated list, sales_plus_tax
sales_plus_tax = list(add_taxes)

# Print the new list with updated values
print(sales_plus_tax)
