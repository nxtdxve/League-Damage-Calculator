import requests
import json
import os

API_KEY = "your-api-key"  # Replace with your Riot Games API key

VERSION_FILE = "data/version.txt"

def get_saved_version():
    try:
        with open(VERSION_FILE, 'r') as f:
            return f.read().strip()
    except FileNotFoundError:
        return None

def save_version(version):
    with open(VERSION_FILE, 'w') as f:
        f.write(version)

def get_latest_version():
    url = "https://ddragon.leagueoflegends.com/api/versions.json"
    response = requests.get(url)
    versions = response.json()
    return versions[0] if versions else None

def fetch_data_from_riot_api(endpoint, version):
    base_url = "https://ddragon.leagueoflegends.com"
    url = f"{base_url}/{endpoint}"
    url = url.replace("{version}", version)
    response = requests.get(url)
    return response.json()

def save_json_to_file(data, file_path):
    with open(file_path, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)

def main():
    # Get the latest version
    latest_version = get_latest_version()
    if not latest_version:
        print("Failed to get the latest version.")
        return

    saved_version = get_saved_version()
    if saved_version != latest_version:
        # Fetch and save champion data
        champion_data = fetch_data_from_riot_api("cdn/{version}/data/en_US/champion.json", latest_version)
        save_json_to_file(champion_data, os.path.join('data', 'champions.json'))

        # Fetch and save item data
        item_data = fetch_data_from_riot_api("cdn/{version}/data/en_US/item.json", latest_version)
        save_json_to_file(item_data, os.path.join('data', 'items.json'))

        # Fetch and save rune data
        rune_data = fetch_data_from_riot_api("cdn/{version}/data/en_US/runesReforged.json", latest_version)
        save_json_to_file(rune_data, os.path.join('data', 'runes.json'))

        # Save the new version
        save_version(latest_version)
        print("Data updated to the latest version.")
    else:
        print("Data is already up-to-date.")

if __name__ == "__main__":
    main()
