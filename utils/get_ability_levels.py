import requests
import json

url = "https://127.0.0.1:2999/liveclientdata/activeplayerabilities"

# Make sure to set 'verify' to False if you're using an HTTPS URL with a self-signed certificate
response = requests.get(url, verify=False)

if response.status_code == 200:
    data = json.loads(response.text)

    # Save the level of each ability in variables
    e_ability_level = data["E"]["abilityLevel"]
    q_ability_level = data["Q"]["abilityLevel"]
    r_ability_level = data["R"]["abilityLevel"]
    w_ability_level = data["W"]["abilityLevel"]

    # Print the ability levels
    print(f"Q ability level: {q_ability_level}")
    print(f"W ability level: {w_ability_level}")
    print(f"E ability level: {e_ability_level}")
    print(f"R ability level: {r_ability_level}")


else:
    print(f"Error: {response.status_code}")
