import random

skins = {
    "forest": {"w":"🌳", "p":"🟫", "f":"🏁", "sprites":["🧙", "🐈", "🧍", "🐕", "🧚"]},
    "castle": {"w":"🔳", "p":"⬜️", "f":"🏁", "sprites":["🧙", "👻", "🧍", "🧛", "🧟"]}
}

skin = random.choice(list(skins.values()))

dimensions = {"easy":13, "regular":19, "hard":25}