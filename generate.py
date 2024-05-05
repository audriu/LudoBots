import pyrosim.pyrosim as pyrosim

pyrosim.Start_SDF("boxes.sdf")
pyrosim.Send_Cube(name="Box", pos=[0, 0, 0.5], size=[1, 1, 1])
pyrosim.Send_Cube(name="Box", pos=[1, 0, 1.5], size=[1, 1, 1])

for i in range(10):
    pyrosim.Send_Cube(name="Box", pos=[0, 0, 2 + i], size=[1 - i / 11, 1 - i / 11, 1])

pyrosim.End()
