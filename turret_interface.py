
from coppeliasim_zmqremoteapi_client import RemoteAPIClient
import time
import cv2
import numpy as np

class turretSim ():
    def __init__(self) -> None:
        self.img = 0
        self.client = RemoteAPIClient()
        self.sim = self.client.getObject('sim')
        self.camera_h = self.sim.getObject('/oak_camera')
        self.yaw_motor_h = self.sim.getObject('/yaw_motor')
        self.pitch_motor_h = self.sim.getObject('/pitch_motor')
        self.euler = [0.0,0.0,0.0]
        self.gyro = [0.0,0.0,0.0]
        # time.sleep(2)    
        # self.sim.setStepping(True)

    def start_simulation(self):
        self.sim.startSimulation()

    def stop_simulation(self):
        self.sim.stopSimulation()

    def step_simulation(self):
        self.sim.step()

    def read_image(self):
        img, [resX, resY] = self.sim.getVisionSensorImg(self.camera_h)
        img = np.frombuffer(img, dtype=np.uint8).reshape(resY, resX, 3)
        img = cv2.cvtColor(img,cv2.COLOR_RGB2BGR)
        img = cv2.flip(img,0)
        return img

    def read_bno(self):
        bno_msg = self.sim.getStringSignal('bno_data')
        bno_str = bno_msg.decode()
        bno = bno_str.split(',')
        self.bno = [float(bno[1]),float(bno[2]),float(bno[3]),float(bno[4]),float(bno[5]),float(bno[6])]           
        return self.bno
    
    def read_gyros(self):
        bno_msg = self.sim.getStringSignal('bno_data')
        bno = bno_msg.split(',')
        self.gyro = [float(bno[4]),float(bno[5]),float(bno[6])]   
        return self.gyro
    
    def send_motor_command(self,pitch_cmd,yaw_cmd):
        self.sim.setFloatSignal('pitch_cmd',pitch_cmd)
        self.sim.setFloatSignal('yaw_cmd',yaw_cmd)

    def send_fire_command(self):
        self.sim.setInt32Signal('shoot_cmd',1)
