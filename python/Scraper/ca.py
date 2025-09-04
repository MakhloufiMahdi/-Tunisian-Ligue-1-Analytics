import requests
import pandas as pd

team_id = 39618            
competition_id = 984       
season_id = 65503          

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:139.0) Gecko/20100101 Firefox/139.0",
    "Accept": "*/*",
    "Accept-Language": "en-US,en;q=0.5",
    "Accept-Encoding": "gzip, deflate, br, zstd",
    "Referer": f"https://www.sofascore.com/team/football/club-africain/{team_id}",
    "X-Requested-With": "05dd9c"
}

url_top_players = f"https://www.sofascore.com/api/v1/team/{team_id}/unique-tournament/{competition_id}/season/{season_id}/top-players/overall"

response = requests.get(url_top_players, headers=headers)

if response.status_code == 200:
    data = response.json()
    players_stats = []
    stats_types = ["goals", "assists", "yellowCards", "redCards"]

    for stat in stats_types:
        for player_data in data["topPlayers"].get(stat, []):
            name = player_data["player"]["name"]
            position = player_data["player"].get("position", "")
            value = player_data["statistics"].get(stat)

            existing = next((item for item in players_stats if item["Player"] == name), None)
            if existing:
                existing[stat] = value
            else:
                players_stats.append({
                    "Player": name,
                    "Position": position,
                    stat: value
                })

    df = pd.DataFrame(players_stats)
    df.to_excel("club_africain_top_players.xlsx", index=False)
else:
    print(f" Erreur {response.status_code}")
    print(response.text)
