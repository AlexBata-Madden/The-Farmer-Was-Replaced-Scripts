# Wood Farming

## Prerequisites

- 32x32 World Unlocked
- 32 Drones Unlocked
- Enough Power
- Enough Water
- Enough Fertilizer

## Implementation

The idea is to spawn drones in a grid formation, get the companion of the plant, go to that location, plant the companion plant, and then harvest the tree. Ideally, you want to stock up on power, water, and fertilizer to guarantee the achievement unlock. You can still run it without those, but the rates will be lower.

## Scripts

- `wood_farm.py`: Multi-drone wood farming.
- `wood_farming_single.py`: Single-drone wood farming.
- `wood_farming_polyculture.py`: Polyculture wood farming.

## Achievements

![wood_unlock](./img/wood_unlock.png)

## Leaderboards

### Wood

Note: Using `wood_farming_polyculture.py`. To make the code leaderboard applicable, change the `while True` in the drone functions to `while < 10000000000`.

![wood_leaderboard](./img/wood_leaderboard.png)

### Wood_Single

Note: Using `wood_farming_polyculture.py` and deleting the code that spawns multiple drones. To make the code leaderboard applicable, change the `while True` in the drone functions to `while < 500000000`.

![wood_single_leaderboard](./img/wood_single_leaderboard.png)
