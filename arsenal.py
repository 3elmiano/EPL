"""
- Extract Arsenal’s data from each season
- Add the season to each row
- Convert stats to numeric
- Sort and display Arsenal’s performance from 1994 to 2018

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
arsenal_rows = []
for _, row in df.iterrows():
    season_str = row['season']
    season = int(season_str.split('/')[0])
    teams = row['table']
    
    for team_data in teams:
        if team_data['team'] == 'Arsenal':
            team_data['season'] = season
            arsenal_rows.append(team_data)

# Convert to DataFrame
arsenal_df = pd.DataFrame(arsenal_rows)

# Clean column names
arsenal_df.columns = arsenal_df.columns.str.strip().str.lower().str.replace(" ", "_")

# Fix goal_difference signs
arsenal_df['goal_difference'] = arsenal_df['goal_difference'].str.replace('+', '', regex=False)

# Convert numeric columns
numeric_cols = [
    'season', 'position', 'played', 'points', 'goal_difference',
    'won', 'draw', 'loss', 'goals_scored', 'goals_against'
]
arsenal_df[numeric_cols] = arsenal_df[numeric_cols].apply(pd.to_numeric, errors='coerce')

# Filter for seasons 1994–2018
arsenal_df = arsenal_df[(arsenal_df['season'] >= 1994) & (arsenal_df['season'] <= 2018)]

# Sort by season
arsenal_df = arsenal_df.sort_values(by='season')

# Display key stats
print("\n📊 Arsenal Performance (1994–2018):")
print(arsenal_df[['season', 'position', 'points', 'goal_difference', 'goals_scored']])

# Optional: Plot Manchester United's points over time
plt.plot(arsenal_df['season'], arsenal_df['points'], marker='o', color='blue')
plt.title("Arsenal Points (1994–2018)")
plt.xlabel("Season")
plt.ylabel("Points")
plt.grid(True)
plt.tight_layout()
plt.show()