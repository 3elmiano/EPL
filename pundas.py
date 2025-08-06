import pandas as pd

# Data represented as a dictionary
data = {
    'Name': ['Steve', 'Lia', 'Vin', 'Katie'],
    'Age': [32, 28, 45, 38],
    'Gender': ['Male', 'Female', 'Male', 'Female'],
    'Rating': [3.45, 4.6, 3.9, 2.78]
}

# Creating the DataFrame
df = pd.DataFrame(data)

# Display the DataFrame
print(df)