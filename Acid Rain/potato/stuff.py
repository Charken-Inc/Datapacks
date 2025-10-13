# Generates a .mcfunction file checking from Y = -64 to 319
start_y = 1
end_y = 383

lines = [f"execute as @a at @s unless block ~ ~{i} ~ minecraft:air run tag @s add under_block" for i in range(start_y, end_y + 1)]

with open("acid_rain_function.mcfunction", "w") as f:
    f.write("\n".join(lines))

print("Generated acid_rain_check_all_above.mcfunction!")

