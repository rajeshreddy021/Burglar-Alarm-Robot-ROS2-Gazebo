# ROS2 Burglar Alarm Robot 🚨

A ROS2-based burglar alarm system that detects motion using computer vision and triggers an alert in a simulated environment using Gazebo and TurtleBot3.

This project demonstrates the integration of ROS2, Gazebo simulation, TurtleBot3 robot, OpenCV, and Python to create a simple robotic security monitoring system.

---

# Project Overview

This project implements a motion detection system for a security robot.

The system uses a camera sensor mounted on a TurtleBot3 Waffle Pi robot in Gazebo simulation to monitor the environment.  
The camera continuously publishes image frames to a ROS2 topic.

A custom ROS2 node processes these frames using OpenCV motion detection and triggers an alert when movement is detected.

---

# Technologies Used

| Technology | Purpose |
|------------|---------|
| ROS2 (Jazzy) | Robot middleware |
| Gazebo | Robot simulation platform |
| TurtleBot3 | Mobile robot platform |
| Python | Programming language |
| OpenCV | Motion detection and image processing |
| cv_bridge | Converts ROS image messages to OpenCV format |

---

# System Architecture

```
Gazebo Simulation
        ↓
TurtleBot3 Waffle Pi Robot
        ↓
Camera Sensor (Gazebo Plugin)
        ↓
ROS2 Topic: /camera/image_raw
        ↓
MotionDetectorAlarm Node (detector.py)
        ↓
OpenCV Motion Detection
        ↓
Intruder Alert + Bounding Box
```

---

# TurtleBot3 Robot

This project uses the TurtleBot3 Waffle Pi robot model available in the TurtleBot3 Gazebo package.

Available TurtleBot3 models:

- TurtleBot3 Burger
- TurtleBot3 Waffle
- TurtleBot3 Waffle Pi

This project uses:

```
TurtleBot3 Waffle Pi
```

The robot model and sensors are defined in:

```
/opt/ros/jazzy/share/turtlebot3_gazebo/models/turtlebot3_waffle_pi/model.sdf
```

This file defines:

- robot structure
- wheels
- sensors
- camera
- Gazebo plugins

---

# Gazebo World Environment

The simulation environment (world) used in this project is provided by the **TurtleBot3 Gazebo package**.

The Gazebo world files are located in:

```
/opt/ros/jazzy/share/turtlebot3_gazebo/worlds/
```

Example world files:

- turtlebot3_world.world
- turtlebot3_house.world
- empty_world.world

In this project, the following world is used:

```
turtlebot3_world.world
```

This world file defines the simulation environment including:

- ground plane
- lighting
- obstacles
- environment layout

When the launch file is executed, Gazebo automatically loads this world and spawns the TurtleBot3 robot inside it.

---

# Camera Sensor and Plugin

The camera sensor is simulated using a Gazebo ROS camera plugin.

Plugin used:

```
gazebo_ros_camera
```

Plugin file:

```
libgazebo_ros_camera.so
```

This plugin performs the following functions:

- simulates a robot camera sensor
- captures images from the Gazebo environment
- publishes images to a ROS2 topic

Topic used:

```
/camera/image_raw
```

---

# ROS2 Publisher–Subscriber Architecture

| Component | Role | Topic |
|----------|------|------|
| Gazebo Camera Plugin | Publisher | /camera/image_raw |
| MotionDetectorAlarm Node | Subscriber | /camera/image_raw |

The Gazebo camera publishes image frames continuously, and the motion detection node subscribes to this topic to process the images.

---

# Motion Detection Algorithm

Motion detection is implemented using frame differencing.

Processing steps:

1. Receive camera image from ROS topic
2. Convert ROS image to OpenCV format using cv_bridge
3. Convert frame to grayscale
4. Apply Gaussian blur to remove noise
5. Compute difference between consecutive frames
6. Apply threshold to detect motion
7. Apply dilation to connect motion regions
8. Detect contours of moving objects
9. Draw bounding boxes around detected objects
10. Display intruder alert message

---

# Running the Simulation

## Step 1 — Launch Gazebo Simulation

Run the TurtleBot3 simulation world:

```
ros2 launch turtlebot3_gazebo turtlebot3_world.launch.py
```

This command:

- starts Gazebo
- loads the simulation world
- spawns the TurtleBot3 robot
- activates sensors and plugins

---

## Step 2 — Run Motion Detection Node

Run the burglar alarm node:

```
ros2 run burglar_alarm detector
```

This starts the MotionDetectorAlarm ROS2 node, which subscribes to the camera topic and performs motion detection.

---

# Output

The program displays two windows.

### Security Feed

Shows the live camera feed with:

- bounding box around detected motion
- intruder alert message

### Motion Delta

Displays the binary motion detection mask.

White regions represent detected movement.

---

# Project Structure

```
burglar_alarm/
│
├── detector.py
├── setup.py
├── package.xml
└── README.md
```

| File | Description |
|------|-------------|
| detector.py | Motion detection ROS2 node |
| setup.py | Python package configuration |
| package.xml | ROS2 package dependencies |
| README.md | Project documentation |

---

# How the System Works

```
Gazebo loads the TurtleBot3 robot
        ↓
Camera sensor starts
        ↓
Camera plugin publishes images
        ↓
Topic: /camera/image_raw
        ↓
MotionDetectorAlarm node subscribes
        ↓
OpenCV processes frames
        ↓
Motion detected
        ↓
Intruder alert triggered
```

---

# Future Improvements

Possible improvements include:

- autonomous robot patrol system
- face recognition for intruder identification
- IoT-based mobile alerts
- deployment on real TurtleBot3 hardware

