# ground.py
# Simple code to create a ground next to the player
import mcpi.minecraft as minecraft
import mcpi.block as block
import time as time

mc = minecraft.Minecraft.create()

# Simple delay to see things
time.sleep(2)

pos = mc.player.getPos()



mc.postToChat('Block was set')

for i in range(0,30):
    for j in range(0,30):
        mc.setBlock(pos.x+i,pos.y-1,pos.z+j,block.GLOWSTONE_BLOCK)
        mc.setBlock(pos.x+i,pos.y,pos.z+j,block.AIR)