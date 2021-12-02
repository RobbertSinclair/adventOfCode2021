import sys

the_input = []
horizontal = 0
depth = 0
aim = 0

aim_change = {
    "up": -1,
    "down": 1,
}

with open(sys.argv[1], "r") as f:
    for movement in f:
        movement = movement.strip()
        movement = movement.split(" ")
        movement_command = movement[0]
        value = int(movement[1])
        if movement_command == "forward":
            horizontal += value
            depth += value * aim
        else:
            aim += value * aim_change[movement_command]



print(f"Final horizontal: {horizontal}")
print(f"Final Depth: {depth}")
print(f"Final Aim: {aim}")
print(f"Horizontal x Depth = {horizontal * depth}")