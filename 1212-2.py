from mcpi.minecraft import Minecraft
mc = Minecraft.create()

import random , time
while True:
    pos = mc.player.getPos()
    x = pos.x + random.uniform(-10,10)
    y = pos.y+30
    z = pos.z + random.uniform(-10,10)

    mc.spawnEntity(x,y,z,53)
    time.sleep(0,1)