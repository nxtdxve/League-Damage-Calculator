def garen(level):
    max_health = 1000
    current_health = 320
    missing_health = max_health - current_health
    base_damage = [150, 300, 450][level - 1]
    missing_health_percentage = [0.25, 0.3, 0.35][level - 1]

    damage = (missing_health_percentage * missing_health) + base_damage
    print(damage)

def optimal_usage(enemy_max_health, level):
    base_damage = [150, 300, 450][level - 1]
    missing_health_percentage = [0.25, 0.3, 0.35][level - 1]

    enemy_current_health = ((missing_health_percentage * enemy_max_health) + base_damage) / (1 + missing_health_percentage)
    print("Enemy current health when damage is equal to current health:", enemy_current_health)

if __name__ == "__main__":
    level = 1
    garen(level)
    optimal_usage(2000, level)
