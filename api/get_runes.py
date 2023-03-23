import requests
import json

url = "https://127.0.0.1:2999/liveclientdata/activeplayerrunes"

response = requests.get(url, verify=False)

if response.status_code == 200:
    data = json.loads(response.text)

    # Save general rune ids
    general_rune_ids = [rune["id"] for rune in data["generalRunes"]]

    # Save stat rune shard ids
    stat_rune_shard_ids = [shard["id"] for shard in data["statRunes"]]

    # Print the rune ids
    print(f"General Rune IDs: {general_rune_ids}")
    print(f"Stat Rune Shard IDs: {stat_rune_shard_ids}")

else:
    print(f"Error: {response.status_code}")
