import requests
import json

def get_all_player_items():
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

        return all_player_items
    else:
        print(f"Error: {response.status_code}")
        return None

if __name__ == "__main__":
    all_items = get_all_player_items()
    if all_items:
        # Print player items
        for player, player_info in all_items.items():
            print(f"{player} ({player_info['champion']}): {player_info['items']}")
    else:
        print("Failed to get player items.")
