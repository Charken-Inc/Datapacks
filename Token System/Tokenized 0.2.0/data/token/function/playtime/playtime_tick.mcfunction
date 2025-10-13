# Increment player ticks every second (20 ticks = 1 second)
execute as @a run scoreboard players add @s play_ticks 1

# Convert ticks to minutes (20 * 60 = 1200 ticks = 1 minute)
execute as @a if score @s play_ticks matches 1200.. run function token:playtime/convert_minute
