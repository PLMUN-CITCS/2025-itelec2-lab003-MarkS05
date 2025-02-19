# Mark Somido
# ITELEC2
# Laboratory #03 – Guided Coding Exercise:
# Variables, Literals, and Case-Sensitivity in Python (with Naming Conventions)

# Declare variables with numeric literals
count = 10                   # 'count' is assigned 10 (integer literal)
Count = 15                   # 'Count' (different from 'count') is assigned 15
decimal_value = 3.14         # 'decimal_value' is assigned 3.14 (float literal)

# Declare a variable with a string literal
message = "Hello, Python!"   # String literal

# Declare a variable with a boolean literal
is_active = True             # Boolean literal

# Declare a variable with the None literal
result = None                # None literal represents absence of value

# Additional variable assignment
total_count = 20             # Another integer literal assignment

# Display the variable values with descriptive labels
print(f"Integer (count): {count}")
print(f"Integer (Count): {Count}")
print(f"Integer (total_count): {total_count}")
print(f"Decimal: {decimal_value}")
print(f"Text: {message}")
print(f"Boolean: {is_active}")
print(f"None Value: {result}")

# Example of inline arithmetic with formatting using an f-string:
num1 = 5
num2 = 3
print(f"Sum: {num1 + num2:.2f}")  # The result (8.00) is formatted to 2 decimal places