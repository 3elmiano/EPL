import pandas as pd

# Create a sample DataFrame
data = {'A': [1, 2, 3, 4], 'B': [5, 6, 7, 8]}
df = pd.DataFrame(data)

# Display the input DataFrame
print("Input DataFrame:\n", df)

# Perform arithmetic operations
print("\nAddition:\n", df + 2)
print("\nSubtraction:\n", df - 2)
print("\nMultiplication:\n", df * 2)
print("\nDivision:\n", df / 2)
print("\nExponentiation:\n", df ** 2)
print("\nModulus:\n", df % 2)
print("\nFloor Division:\n", df // 2)