import sys

the_input = []
horizontal = 0
depth = 0

commands = {
    "up": (0,-1),
    "down": (0, 1),
    "forward": (1, 0),
    "back": (-1, 0)
}

with open(sys.argv[1], "r") as f:
    for movement in f:
        movement = movement.strip()
        movement = movement.split(" ")
        movement_command = movement[0]
        value = int(movement[1])
        command_changes = commands[movement_command]
        horizontal += value * command_changes[0]
        depth += value * command_changes[1] 

print(f"Final horizontal: {horizontal}")
print(f"Final Depth: {depth}")
print(f"Horizontal x Depth = {horizontal * depth}")
        



        