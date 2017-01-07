# bomb.py
# Simple code to set one layer of lava and another layer of TNT on it
import mcpi.minecraft as minecraft
import mcpi.block as block
import time as time

mc = minecraft.Minecraft.create()

# Simple delay to see things
time.sleep(2)

pos = mc.player.getPos()

mc.postToChat('Block ready to fly up')
#mc.player.setPos(pos)

# This goes up
for i in range(0,25):
    mc.setBlock(pos.x,pos.y+i,pos.z,block.AIR)
    mc.setBlock(pos.x,pos.y+i+1,pos.z,block.DIAMOND_BLOCK)
    time.sleep(0.1)

mc.postToChat('Shooting forward')
# This goes forward
for i in range(0,25):
    mc.setBlock(pos.x+i,pos.y+1,pos.z,block.AIR)
    mc.setBlock(pos.x+i+1,pos.y+1,pos.z,block.DIAMOND_BLOCK)
    time.sleep(0.1)