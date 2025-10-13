# Generates a .mcfunction file checking from Y = -64 to 319
target_function = "acid_rain:stop"
start_y = -64
end_y = 319

lines = [f"execute unless block ~ ~{i} ~ air run function {target_function}" for i in range(start_y, end_y + 1)]

with open("acid_rain_function.mcfunction", "w") as f:
    f.write("\n".join(lines))

print("Generated acid_rain_check_all_above.mcfunction!")

