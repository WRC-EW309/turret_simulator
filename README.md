# EW309 Turret Simulator
This repository includes the code for the EW309 Turret Simulator. The simulator is built using CoppeliaSim (https://www.coppeliarobotics.com/). CoppeliaSim uses scene files to describe the simulation environment and the objects within it. CoppeliaSim provides an external programming API via a ZeroMQ server that runs whenever the application is running. To interface with the CoppeliaSim simulation, external interface code can be written to make api function calls to the ZeroMQ server. This simulator is not intended to be an exact 1 to 1 replacement for the turret but should allow the student to work on algorithmic aspect of their project without needing the physical system. **You must still use your critical thinking skills to determine what things will and will not translate to the real world**

# Installation

## Installing CoppeliaSim
1. Go to the downloads page of coppeliarobotics.com and download the educational version of CoppeliaSim (https://www.coppeliarobotics.com/downloads) **You must use version 4.6 or the simulator will not work.**
1. Run the installer

## Setting up Python Environment (Windows)
1. Install anaconda navigator from software center
1. Open a Powershell prompt from anaconda navigator. This ensures your environment is loaded automatically. In the terminal execute the following commands to install the required python packages
```
python -m pip install opencv-python
python -m pip install coppeliasim-zmqremoteapi-client
```

## Downloading Code from Github
In order to most easily recevie updates to the software package it is best practice to download the turret-simulator package by cloning the github repositry rather than downloading a zip file. To do this in windows you will need to install github for desktop.
1. Go to the following link and follow the instructions for installing github for desktop (https://docs.github.com/en/desktop/installing-and-authenticating-to-github-desktop/installing-github-desktop) 
1. Open github desktop
1. Under the File tab select 'clone repository'
1. Click the URL tab and paste the repository link (https://github.com/WRC-EW309/turret_simulator.git) in the url field and click the clone button.
1. By default it will clone the repository to C:\Users\<username>\Documents\Github\

## Understanding the Code
1. 'turret_scene.ttt' is the CoppeliaSim scene file that must be loaded from within the CoppeliaSim application.
2. 'turret_interface.py' is a library file which has the turretSim class which handles the low level interactions with the simulator
3. 'turret_demo.py' is a simple example program which shows the basic operations of the turret_interface.py class. 

### turretSim Class methods
To make an instance of the class object one can do the following
```
 turret = turretSim()
```
The turret class has within it the 'sim' (turret.sim) object which can be used to interact directly with the CoppeliaSim scene. This can be used to control the simlation directly via the typical api. Examples of this usage in the demo script are the following:
```
    turret.sim.setStepping(True)    # Put simulation into Stepping Mode
    turret.sim.startSimulation()    # Start Simulation
    turret.sim.stopSimulation()     # Stop Simulation
    turret.sim.step()               # Step the Model one step forward 

```
It should be noted that these steps would likely not have analog function calls in your experimental code since they only relate to running the simulator.

There are two commands that are used to actuate the simulated turret:
```
    turret.send_motor_command(pitch_pwm,yaw_pwm)   # Send Motor pwm command to Sim
    turret.send_fire_command()  # Send Fire Command for 1 Round

```
There are two commands to get feedback from the turret
```
# The bno_data variable returned is formatted as follows [roll, pitch, yaw, roll_rate, pitch_rate, yaw_rate]
    bno_data = turret.read_bno()    # Read Imu Data from Simulated BNO

# The img data is formatted as an Open CV image object
    img = turret.read_image()       # Read Image in Open CV format

```
## Running Turret Demo Program
Provided with the repository is an example program that demonstrates the basic functionality of actuating the turret, firing the turret, getting angle feedback from the IMU, and the camera feed. 
1. From CoppeliaSim open the **turret_scene.ttt** file.
1. From within anaconda navigator open VScode or Pycharm to ensure that the environment is loaded
1. Open the folder for the repository make sure both the **turret_demo.py** and **turret_interface.py** files are there
1. Run the **turret_demo.py** program. You should see the simulation begin, the turret with oscilate back and forth periodically shooting rounds.


