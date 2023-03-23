import requests
import json

def get_champion():
    url = "https://127.0.0.1:2999/liveclientdata/activeplayer"

    response = requests.get(url, verify=False)

    if response.status_code == 200:
        data = json.loads(response.text)
        my_champion = data["championName"]
        return my_champion
    else:
        print(f"Error: {response.status_code}")
        return None

if __name__ == "__main__":
    champion_name = get_champion()
    if champion_name:
        print(champion_name)
    else:
        print("Failed to get champion name.")
