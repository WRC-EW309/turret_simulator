
# from coppeliasim_zmqremoteapi_client import RemoteAPIClient
import time
import math
import cv2
from turret_interface import turretSim

def main():

    # Create Turret Sim Object to Interact with the Simulation
    turret = turretSim()

    turret.sim.setStepping(True)    # Put simulation into Stepping Mode
    turret.sim.startSimulation()    # Start Simulation
    turret.sim.step()               # Initially Step the Model 

    # Initialize Variables for running sim
    last_shot = 0
    t_old = 0
    run_time = 20
    while(turret.sim.getSimulationTime()<run_time):
        t = turret.sim.getSimulationTime()  # Get time from simulation
        dt = t-t_old                        # Compute Sample time

        bno_data = turret.read_bno()    # Read Imu Data from Simulated BNO
        img = turret.read_image()       # Read Image in Open CV format

        print(bno_data)                 # Print IMU Data to the screen
        # Formated [roll, pitch, yaw, roll_rate, pitch_rate, yaw_rate]
        # pitch = bno_data[1]
        # yaw = bno_data[2]

        # Set Sinusoidal commands for Yaw and Pitch Motors
        T = 5
        yaw_cmd = 0.2*math.sin(2*math.pi*t/T)   
        pitch_cmd = 0.2*math.cos(2*math.pi*t/T)

        
        turret.send_motor_command(-pitch_cmd,yaw_cmd)   # Send Motor command to Sim

        if(t-last_shot > 3.0):  # Shoot a shot every 3 seconds
            last_shot = turret.sim.getSimulationTime()
            turret.send_fire_command()  # Send Fire Command for 1 Round

        t_old = t                       # Age t_old Variable
        
        cv2.imshow('image',img)  
        cv2.waitKey(1)
        turret.step_simulation()
        time.sleep(0.02)
        
    
    turret.send_motor_command(0.0,0.0)  # Set Motors commands to zero
    turret.sim.stopSimulation()         # Stop Simulation


if __name__ == "__main__":
    main()