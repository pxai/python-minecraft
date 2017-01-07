# bomb.py
# Simple code to set one layer of lava and another layer of TNT on it
import mcpi.minecraft as minecraft
import mcpi.block as block
import time as time

mc = minecraft.Minecraft.create()

# Simple delay to see things
time.sleep(2)

pos = mc.player.getPos()

mc.postToChat('Ready to Explode')

for i in range(0,30):
    for j in range(0,30):
        mc.setBlock(pos.x+i,pos.y-1,pos.z+j,block.LAVA_STATIONARY)

# A cube of TNT
for i in range(0,30):
    for j in range(0,30):
        for k in range(0,30):
            mc.setBlock(pos.x+i,pos.y+j,pos.z+k,block.TNT)
