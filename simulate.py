import pybullet as p
import pybullet_data
import time

physicsClient = p.connect(p.GUI)
p.setAdditionalSearchPath(pybullet_data.getDataPath())

planeId = p.loadURDF("plane.urdf")
p.loadSDF("boxes.sdf")
p.setGravity(0, 0, -9.8)

while True:
    p.stepSimulation()
    time.sleep(0.005)
p.disconnect()
