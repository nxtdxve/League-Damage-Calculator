import importlib

# Call the get_champion function to get the champion name
champion_name = "Garen"

try:
    # Import the module for the given champion
    champion_module = importlib.import_module(f"modules.{champion_name.lower()}")
except ImportError:
    print("Champion not supported.")

# Call the desired function from the imported module
level = 1
champion_module.garen(level)
champion_module.optimal_usage(2000, level)
