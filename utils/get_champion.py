import requests
import json

url = "https://127.0.0.1:2999/liveclientdata/activeplayer"

response = requests.get(url, verify=False)

if response.status_code == 200:
    data = json.loads(response.text)
    my_champion = data["championName"]
else:
    print(f"Error: {response.status_code}")

if __name__ == "__main__":
    print(my_champion)

