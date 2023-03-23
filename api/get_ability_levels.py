import requests
import json

def get_ability_levels():
    url = "https://127.0.0.1:2999/liveclientdata/activeplayerabilities"

    response = requests.get(url, verify=False)

    if response.status_code == 200:
        data = json.loads(response.text)

        # Save the level of each ability in variables
        e_ability_level = data["E"]["abilityLevel"]
        q_ability_level = data["Q"]["abilityLevel"]
        r_ability_level = data["R"]["abilityLevel"]
        w_ability_level = data["W"]["abilityLevel"]

        # Return a dictionary with ability levels
        return {
            "Q": q_ability_level,
            "W": w_ability_level,
            "E": e_ability_level,
            "R": r_ability_level
        }
    else:
        print(f"Error: {response.status_code}")
        return None

if __name__ == "__main__":
    ability_levels = get_ability_levels()
    if ability_levels:
        # Print the ability levels
        print(f"Q ability level: {ability_levels['Q']}")
        print(f"W ability level: {ability_levels['W']}")
        print(f"E ability level: {ability_levels['E']}")
        print(f"R ability level: {ability_levels['R']}")
    else:
        print("Failed to get ability levels.")
