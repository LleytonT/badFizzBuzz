# Global variable for storing output strings (bad practice)
output = ""

# Loop from 1 to 100 (inclusive)
for num in range(1, 101):
  # Check for divisibility by 3 and 5 using nested if statements (redundant)
  if num % 3 == 0:
    if num % 5 == 0:
      output += "CompClub"  # Append to global variable (avoid globals)
    else:
      output += "Comp"
  elif num % 5 == 0:
    output += "Club"
  else:
    output += str(num)  # Convert number to string inside loop (inefficient)

# Print the final output string (use print within the loop for better readability)
print(output)
