execute as @a if predicate faster_paths:fast run effect give @s speed 1 1 true
execute as @e[type=pig] if predicate faster_paths:fast run effect give @s speed 1 1 true
execute as @e[type=horse] if predicate faster_paths:fast run effect give @s speed 1 1 true
execute as @e[type=mule] if predicate faster_paths:fast run effect give @s speed 1 1 true
execute as @e[type=donkey] if predicate faster_paths:fast run effect give @s speed 1 1 true
execute as @e[type=skeleton_horse] if predicate faster_paths:fast run effect give @s speed 1 1 true
execute as @e[type=llama] if predicate faster_paths:fast run effect give @s speed 1 1 true
execute as @e[type=strider] if predicate faster_paths:fast run effect give @s speed 1 1 true
execute as @e[type=camel] if predicate faster_paths:fast run effect give @s speed 1 1 true
execute as @a if predicate faster_paths:fast run attribute @s step_height base set 1
execute as @a if predicate faster_paths:step run attribute @s step_height base set 0.6