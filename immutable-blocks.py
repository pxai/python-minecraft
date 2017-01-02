
# immutable-blocks.py
# Pello Altadill - http://pello.io
# Enables/disables the posibility to destroy blocks
import mcpi.minecraft as minecraft
import mcpi.block as block
import time as time

mc = minecraft.Minecraft.create()

# Simple delay to see things
time.sleep(2)

mc.postToChat("Changing world blocks behavior")
mc.setting("world_immutable", True)
