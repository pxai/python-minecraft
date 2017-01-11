# tower.py
# Simple code to create a tower
import mcpi.minecraft as minecraft
import mcpi.block as block
import time as time

mc = minecraft.Minecraft.create()

# Simple delay to see things
time.sleep(2)

# Get player position
pos = mc.player.getPos()

mc.postToChat('Building to block')
x = pos.x
y = pos.y
z = pos.z

for i in range(0,20):
    for j in range(0,10):
	    mc.setBlock(x, y+i, z+j, block.DIAMOND_BLOCK)

x = pos.x
y = pos.y
z = pos.z + 10
for i in range(0,20):
    for j in range(0,10):
	    mc.setBlock(x+j, y+i, z, block.DIAMOND_BLOCK)

x = pos.x + 10
y = pos.y
z = pos.z + 10
for i in range(0,20):
    for j in range(0,10):
	    mc.setBlock(x, y+i, z-j, block.DIAMOND_BLOCK)

x = pos.x + 10
y = pos.y
z = pos.z
for i in range(0,20):
    for j in range(0,10):
	    mc.setBlock(x-j, y+i, z, block.DIAMOND_BLOCK)