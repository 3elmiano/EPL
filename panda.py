import pandas as pd

df = pd.read_csv(r'C:\Users\Administrator\Downloads\MOCK_DATA.csv')
filtered = df[df["gender"] == "Male"]


print(filtered)
