import requests
import json

url = "https://127.0.0.1:2999/liveclientdata/playerlist"

response = requests.get(url, verify=False)

if response.status_code == 200:
    data = json.loads(response.text)
    all_player_items = {}

    for player_data in data:
        champion_name = player_data["championName"]
        summoner_name = player_data["summonerName"]
        items = player_data["items"]

        all_player_items[summoner_name] = {
            "champion": champion_name,
            "items": items
        }

    # Print player items
    for player, player_info in all_player_items.items():
        print(f"{player} ({player_info['champion']}): {player_info['items']}")

else:
    print(f"Error: {response.status_code}")
