# Subtract 1200 ticks
scoreboard players remove @s play_ticks 1200

# Add one minute
scoreboard players add @s play_minutes 1

# Every 60 minutes, convert to 1 hour
execute as @s if score @s play_minutes matches 60.. run function token:playtime/convert_hour
