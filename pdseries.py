import pandas as pd
s = pd.Series([1,2,3,4,5],index = ['a','b','c','d','e'])

# Display the Input Series
print('Input Series\n',s)

# Apply all Arithmetic Operation and Display the Results
print('\nAddition:\n',s+2)
print('\nSubtraction:\n', s-2)
print('\nMultiplication:\n', s * 2)
print('\nDivision:\n', s/2)
print('\nExponentiation:\n', s**2)
print('\nModulus:\n', s%2)
print('\nFloor Division:\n', s//2)