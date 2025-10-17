user_ids = ["T42YG4KTK", "VTQ39IDQ0", "CRL11YUWX", 
            "K6Y5URXLR", "V4XCBER7V", "IOGQWC61K"]

# Loop through user_ids
for user_id in user_ids:
  # Print the user_id
  print(user_id)

# Create the tickets_sold variable
tickets_sold = 0

# Create the max_capacity variable
max_capacity = 30

# Loop through a range up to and including max_capacity's value

for tickets in range(1, max_capacity + 1):
  
  # Add one to tickets_sold in each iteration
  tickets_sold = tickets_sold + 1

print("Sold out:", tickets_sold, "tickets sold!")

# Loop through the dictionary's keys and values
for key, value in courses.items():
  
  # Check if the value is "AI"
  if value == "AI":
    print(key, "is an AI course")
  
  # Check if the value is "Programming"
  elif value == "Programming":
    print(key, "is a Programming course")
  
  # Otherwise, print that it is a "Data Engineering" course
  else:
    print(key, "is a Data Engineering course")

