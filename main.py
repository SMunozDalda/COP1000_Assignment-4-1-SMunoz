"""
This program calculates prices for custom house signs.
"""

# Declare and initialize variables here.
charge = 0.00              # Charge for this sign.
numChars = 8              # Number of characters.
color = "gold"            # Color of characters.
woodType = "oak"          # Type of wood.

# Charge for this sign.
charge = 35.00

# Number of characters.
if numChars > 5:
    charge += (numChars - 5) * 4

# Color of characters.
if color.lower() == "gold":
    charge += 15.00
  
# Type of wood.
if woodType.lower() == "oak":
    charge += 20.00
  
# Write assignment and if statements here as appropriate.

# Output Charge for this sign.
print("The charge for this sign is $" + str(charge))
