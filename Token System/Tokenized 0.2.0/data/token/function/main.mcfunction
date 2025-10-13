# Give reward
tellraw @s "You Got a Token!"
scoreboard players add @s token_storage 1
# Update lastReward to current gametime
execute as @s store result score @s lastReward run time query gametime
