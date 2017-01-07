
# teleport-args.py
# Pello Altadill - http://pello.io
# Moves player to given position, using system arguments
#  Usage
#  python teleport-args.py x y z  (x y z are numbers)
import sys
import mcpi.minecraft as minecraft
import mcpi.block as block
import time as time

mc = minecraft.Minecraft.create()

# Simple delay to see things
time.sleep(2)

pos = mc.player.getPos()
mc.postToChat("Our position : %f %f %f " % (pos.x, pos.y, pos.z))

# Now teleport to other position, but using arguments instead
# of fixed values
x = float(sys.argv[1])
y = float(sys.argv[2])
z = float(sys.argv[3])
mc.postToChat("Moving to : %f %f %f " % (x, y, z))
mc.player.setTilePos(x,y,z);

pos = mc.player.getPos()
mc.postToChat("Our new position : %f %f %f " % (pos.x, pos.y, pos.z))