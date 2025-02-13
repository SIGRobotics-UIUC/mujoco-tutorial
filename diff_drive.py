import mujoco
import mujoco.viewer
import time

xml_path = "diff_drive.xml"
model = mujoco.MjModel.from_xml_path(xml_path)
data = mujoco.MjData(model)

timestep = 1/60.0

# control inputs
left_vel = 0
right_vel = 0

def key_callback(keycode):
    global left_vel, right_vel
    if chr(keycode) == " ":
        left_vel = 0
        right_vel = 0
    if chr(keycode) == "W":
        left_vel = 1
        right_vel = 1
    if chr(keycode) == "A":
        left_vel = -1
        right_vel = 1
    if chr(keycode) == "S":
        left_vel = -1
        right_vel = -1
    if chr(keycode) == "D":
        left_vel = 1
        right_vel = -1

with mujoco.viewer.launch_passive(model, data, key_callback=key_callback) as viewer:
    while viewer.is_running():
        start = time.time()
        # control inputs
        data.ctrl[0] = 30 * left_vel
        data.ctrl[1] = 30 * right_vel

        mujoco.mj_step(model, data)

        viewer.sync()

        curr = time.time()
        while curr - start < timestep:
            time.sleep(0.001)
            curr = time.time()


