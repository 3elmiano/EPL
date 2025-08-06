import pandas as pd
import matplotlib.pyplot as plt

# Load JSON
df = pd.read_json('EPL.json')

# Get data for Arsenal
chelsea_data = df[df["team"] == "Chelsea"]
print(chelsea_data)