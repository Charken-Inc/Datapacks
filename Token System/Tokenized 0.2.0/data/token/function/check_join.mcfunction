# 1️⃣ Store current gametime
execute as @s store result score @s tempGametime run time query gametime

# 2️⃣ Compute next eligible tick
scoreboard players operation @s cooldownThreshold = @s lastReward
scoreboard players add @s cooldownThreshold 72000
# 3️⃣ Run reward only if current gametime >= threshold
execute as @s if score @s tempGametime >= @s cooldownThreshold run function token:main
