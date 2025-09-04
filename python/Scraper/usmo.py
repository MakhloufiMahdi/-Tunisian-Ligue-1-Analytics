import requests
import pandas as pd

team_id = 59638
competition_id = 984  
season_id = 65503     

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:139.0) Gecko/20100101 Firefox/139.0",
    "Accept": "*/*",
    "Accept-Language": "en-US,en;q=0.5",
    "Accept-Encoding": "gzip, deflate, br, zstd",
    "Referer": "https://www.sofascore.com/team/football/us-monastir/59638",
    "X-Requested-With": "2bcc7c"
}

url_top_players = f"https://www.sofascore.com/api/v1/team/{team_id}/unique-tournament/{competition_id}/season/{season_id}/top-players/overall"
res = requests.get(url_top_players, headers=headers)

if res.status_code == 200:
    data = res.json()
    players_stats = []
    stats_types = ["goals", "assists", "yellowCards", "redCards"]

    for stat in stats_types:
        for p in data["topPlayers"].get(stat, []):
            name = p["player"]["name"]
            position = p["player"].get("position", "")
            value = p["statistics"].get(stat)

            entry = next((e for e in players_stats if e["Player"] == name), None)
            if entry:
                entry[stat] = value
            else:
                players_stats.append({
                    "Player": name,
                    "Position": position,
                    stat: value
                })

    df_players = pd.DataFrame(players_stats)
    df_players.to_excel("usmo_top_playyers.xlsx", index=False)
else:
    print(res.text)
