import pandas as pd

# Create a Pandas Series
s = pd.Series([1, 2, 3])

# Convert Series to a Python list
result = s.to_list()
result1 = s.to_numpy()
result2 = s.to_dict()
result3 = s.to_frame()
result4 = s.to_string()


print("Output:",result)
print("Output:",result1)
print("Output:",result2)
print("Output:",result3)

