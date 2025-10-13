tellraw @s {"text":"⏰ You’ve played for ","color":"aqua","extra":[{"score":{"name":"@s","objective":"play_hours"},"color":"yellow"},{"text":" hour(s) and ","color":"aqua"},{"score":{"name":"@s","objective":"play_minutes"},"color":"yellow"},{"text":" minute(s).","color":"aqua"}]}
scoreboard players set @s playtime 0
