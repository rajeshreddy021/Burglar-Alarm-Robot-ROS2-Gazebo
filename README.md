# Burglar Alarm Robot (Phase II: Gazebo Simulation)

A ROS 2 Jazzy-based security robot project developed by **Tech Titans**. This system utilizes computer vision to detect motion within a Gazebo simulation environment using a TurtleBot3 Waffle Pi.

## 🚀 Features
- **Real-time Motion Detection**: Uses absolute frame differencing to identify movement.
- **Noise Filtering**: Implements Gaussian Blur to ensure stability in simulated environments.
- **Visual Feedback**: Real-time bounding boxes and "Intruder Alert" overlays.
- **Simulation-Ready**: Designed for the TurtleBot3 Waffle Pi in Gazebo.

## 🛠️ Technical Stack
- **OS**: Ubuntu 24.04 (Noble)
- **Middleware**: ROS 2 Jazzy Jalisco
- **Vision**: OpenCV with `cv_bridge`
- **Language**: Python 3

## 🏃 How to Run
1. **Source your workspace**:
   ```bash
   source /opt/ros/jazzy/setup.bash
   source ~/alarm_ws/install/setup.bash
