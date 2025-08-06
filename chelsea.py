"""
Perfect — that confirms everything! Your 'table' column contains a list of team dictionaries for each season, and Chelsea is one of them. Now you’re ready to extract Chelsea’s stats across all seasons.
Here’s a complete and corrected script that will:
- Extract Chelsea’s data from each season
- Add the season to each row
- Convert stats to numeric
- Sort and display Chelsea’s performance from 1994 to 2018

"""

import pandas as pd
import json
import matplotlib.pyplot as plt

# Load JSON
with open('EPL.json') as f:
    data = json.load(f)

# Convert to DataFrame
df = pd.DataFrame(data)

# ✅ Now loop through each row
chelsea_rows = []
for _, row in df.iterrows():
    season_str = row['season']
    season = int(season_str.split('/')[0])
    teams = row['table']
    
    for team_data in teams:
        if team_data['team'] == 'Chelsea':
            team_data['season'] = season
            chelsea_rows.append(team_data)

# Convert to DataFrame
chelsea_df = pd.DataFrame(chelsea_rows)

# Clean column names
chelsea_df.columns = chelsea_df.columns.str.strip().str.lower().str.replace(" ", "_")

# Fix goal_difference signs
chelsea_df['goal_difference'] = chelsea_df['goal_difference'].str.replace('+', '', regex=False)

# Convert numeric columns
numeric_cols = [
    'season', 'position', 'played', 'points', 'goal_difference',
    'won', 'draw', 'loss', 'goals_scored', 'goals_against'
]
chelsea_df[numeric_cols] = chelsea_df[numeric_cols].apply(pd.to_numeric, errors='coerce')

# Filter for seasons 1994–2018
chelsea_df = chelsea_df[(chelsea_df['season'] >= 1994) & (chelsea_df['season'] <= 2018)]

# Sort by season
chelsea_df = chelsea_df.sort_values(by='season')

# Display key stats
print("\n📊 Chelsea Performance (1994–2018):")
print(chelsea_df[['season', 'position', 'points', 'goal_difference', 'goals_scored']])

# Optional: Plot Chelsea's points over time
plt.plot(chelsea_df['season'], chelsea_df['points'], marker='o', color='blue')
plt.title("Chelsea Points (1994–2018)")
plt.xlabel("Season")
plt.ylabel("Points")
plt.grid(True)
plt.tight_layout()
plt.show()