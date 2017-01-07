# bomb.py
# Simple code to set one layer of lava and another layer of TNT on it
import mcpi.minecraft as minecraft
import mcpi.block as block
import time as time

mc = minecraft.Minecraft.create()

# Simple delay to see things
time.sleep(2)

pos = mc.player.getPos()

mc.postToChat('Ready to make a hole')
#mc.player.setPos(pos)

pos.y = pos.y - 5;
# Beware, server may not be able to handle this
for i in range(0,30):
    for j in range(0,30):
        for k in range(0,30):
            mc.setBlock(pos.x+i,pos.y+j,pos.z+k,block.AIR)
