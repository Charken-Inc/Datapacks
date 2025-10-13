import os

# === CONFIG ===
base_path = "data/token/functions"
shop_path = os.path.join(base_path, "shop")
buying_path = os.path.join(shop_path, "buying")

# Make directories
os.makedirs(buying_path, exist_ok=True)

# Each tuple: (id, give_command, price)
items = [
    ("iron_ingot", "minecraft:iron_ingot 32", 5),
    ("coal", "minecraft:coal 64", 5),
    ("bread", "minecraft:bread 32", 5),
    ("diamond", "minecraft:diamond 1", 12),
    ("ender_pearl", "minecraft:ender_pearl 4", 15),
    ("saddle", "minecraft:saddle 1", 18),
    ("name_tag", "minecraft:name_tag 1", 20),
    ("exp_bottle", "minecraft:experience_bottle 16", 25),
    ("diamond_pack", "minecraft:diamond 8", 40),
    ("netherite_scrap", "minecraft:netherite_scrap 1", 50),
    ("blaze_rod", "minecraft:blaze_rod 8", 60),
    ("trident", "minecraft:trident 1", 75),
    ("elytra", "minecraft:elytra 1", 100),
    ("totem", "minecraft:totem_of_undying 1", 75),
    ("enchanted_book", "minecraft:enchanted_book 1", 60),
    ("shulker_shell", "minecraft:shulker_shell 2", 90),
    ("nether_star", "minecraft:nether_star 1", 125),
    ("beacon", "minecraft:beacon 1", 150),
    ("shulker_box", "minecraft:shulker_box 1", 140),
    ("netherite_ingot", "minecraft:netherite_ingot 1", 150),
    ("elytra_upgraded", 'minecraft:elytra{Enchantments:[{id:"minecraft:unbreaking",lvl:3},{id:"minecraft:mending",lvl:1}]} 1', 200),
    ("dragon_egg", "minecraft:dragon_egg 1", 300),
    ("player_head", "minecraft:player_head 1", 150),
]

# === Generate each shop file ===
for item_id, give_item, price in items:
    file_path = os.path.join(shop_path, f"{item_id}.mcfunction")
    with open(file_path, "w") as f:
        f.write(f"give @s {give_item}\n")
        f.write(f"scoreboard players remove @s token_storage {price}\n")
        f.write(f"scoreboard players set @s shop_{item_id} 0\n")
    print(f"Created: {file_path}")

# === Generate setup_triggers.mcfunction ===
setup_path = os.path.join(base_path, "setup_triggers.mcfunction")
with open(setup_path, "w") as f:
    for item_id, _, _ in items:
        f.write(f"scoreboard objectives add shop_{item_id} trigger\n")
print(f"Created: {setup_path}")

# === Generate shop_handler.mcfunction ===
handler_path = os.path.join(buying_path, "shop_handler.mcfunction")
with open(handler_path, "w") as f:
    for item_id, _, price in items:
        f.write(f"execute as @a[scores={{shop_{item_id}=1..,token_storage={price}..}}] run function token:shop/{item_id}\n")
print(f"Created: {handler_path}")

print("\n✅ All shop + handler files generated successfully!")

