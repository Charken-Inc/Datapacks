execute as @a if predicate faster_paths:fast run effect give @s speed 1 1 true
execute as @a if predicate faster_paths:fast run attribute @s step_height base set 1
execute as @a if predicate faster_paths:step run attribute @s step_height base set 0.6