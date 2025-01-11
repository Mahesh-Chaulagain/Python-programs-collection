# List of color codes corresponding to resistor values
color = ["black", "brown", "red", "orange", "yellow", "green", "blue", "violet", "grey", "white"]

# Get user input for the first, second, and third color bands
n = color.index(input("Enter the first color: "))  # First color: significant digit (multiplier of 10)
m = color.index(input("Enter the second color: "))  # Second color: second significant digit
p = color.index(input("Enter the third color: "))  # Third color: power of 10 (number of zeros)

# Calculate the resistor value
# (n * 10 + m) gives the first two digits of the resistance value
# (10**p) adds the appropriate number of zeros based on the third color band
q = int(((n * 10) + m) * (10 ** p))

# Convert the resistance value to kiloohms (1 kiloohm = 1000 ohms)
z = q / 1000

# Output the resistor value in ohms and kiloohms
print("The Resistor value is :")
print(f"{q} ohms and in kiloohms: {z} kΩ")
