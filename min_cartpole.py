import numpy as np
import mujoco
import mujoco.viewer
import time

model = mujoco.MjModel.from_xml_path('cartpole.xml')
data = mujoco.MjData(model)

timestep = 0.02

# TODO Understand data.ctrl, model.geom, data.qpos, data.qvel
data.ctrl = [1]
mujoco.mj_step(model, data)

with mujoco.viewer.launch_passive(model, data) as viewer:
    while viewer.is_running():
        #TODO Add control logic
        start = time.time()
        if data.qpos[1] > 0:
            data.ctrl = [1]
        else:
            data.ctrl = [-1]
        
        mujoco.mj_step(model, data)
        viewer.sync()

        curr = time.time()
        while curr - start < timestep:
            time.sleep(0.001)
            curr = time.time()

# close
viewer.close()
