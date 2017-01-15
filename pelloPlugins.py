# helloworld.py
# Simple code to show a message in the chat
import mcpi.minecraft as minecraft
import mcpi.entity as Entity

mc = minecraft.Minecraft.create()

mc.showWarning("My first warning")

pos = mc.player.getPos()
x = y = z = 100
mc.showWarning("Howly crap, creating entities")

for i in range(0,20):
    mc.setEntity(pos.x, pos.y, pos.z, Entity.VILLAGER)
#mc.setMob(pos.x,pos.y,pos.z, Entity.CREEPER)