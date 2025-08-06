"""
- Extract Man united’s data from each season
- Add the season to each row
- Convert stats to numeric
- Sort and display Man united’s performance from 1994 to 2018

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
manU_rows = []
for _, row in df.iterrows():
    season_str = row['season']
    season = int(season_str.split('/')[0])
    teams = row['table']
    
    for team_data in teams:
        if team_data['team'] == 'Manchester United':
            team_data['season'] = season
            manU_rows.append(team_data)

# Convert to DataFrame
manU_df = pd.DataFrame(manU_rows)

# Clean column names
manU_df.columns = manU_df.columns.str.strip().str.lower().str.replace(" ", "_")

# Fix goal_difference signs
manU_df['goal_difference'] = manU_df['goal_difference'].str.replace('+', '', regex=False)

# Convert numeric columns
numeric_cols = [
    'season', 'position', 'played', 'points', 'goal_difference',
    'won', 'draw', 'loss', 'goals_scored', 'goals_against'
]
manU_df[numeric_cols] = manU_df[numeric_cols].apply(pd.to_numeric, errors='coerce')

# Filter for seasons 1994–2018
manU_df = manU_df[(manU_df['season'] >= 1994) & (manU_df['season'] <= 2018)]

# Sort by season
manU_df = manU_df.sort_values(by='season')

# Display key stats
print("\n📊 Manchester United Performance (1994–2018):")
print(manU_df[['season', 'position', 'points', 'goal_difference', 'goals_scored']])

# Optional: Plot Manchester United's points over time
plt.plot(manU_df['season'], manU_df['points'], marker='o', color='blue')
plt.title("Manchester United Points (1994–2018)")
plt.xlabel("Season")
plt.ylabel("Points")
plt.grid(True)
plt.tight_layout()
plt.show()