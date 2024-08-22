@@ -0,0 +1,11 @@
#ranpo
Ranpo (Palestine)
School Name: Anabta Girls Secondary School
#Team Members :
Aya Abu-Ammash 
Saba Abu-Al-Own 
Jana Abu-Al-Own 
#Project Overview
We're the Ranpo, a passionate team from Palestine on a mission to conquer the WRO Future Engineers 2024 challenge by building a fully autonomous self-driving car! , our car is designed to navigate a designated track and complete three laps without human intervention. This project embodies our commitment to robotics, innovation, and the future of intelligent transportation.
#The WRO Challenge and Our Focus
The WRO Future Engineers category emphasizes the entire engineering process. Teams earn points for their final product and for documenting their journey within a public GitHub repository. This year's exciting challenge features a randomly changing track, testing our car's adaptability!
We're focusing on these key areas to build our autonomous car:
•	Sensor Fusion and Computer Vision: We'll use ultrasonic ,color sensor, cameras, and computer vision to give our car a real-time understanding of its surroundings.
•	Open-Source Hardware: We're building with readily available components like a Jetson Nano, an RC chassis, and the Adafruit Motor Shield.
•	Action Planning and Kinematic Control: Sophisticated algorithms will enable the car to make decisions and execute maneuvers beyond simple differential drive.
•	Optimization for Stability: Our goal is to create a consistently reliable car capable of navigating the various track layouts.
•	Teamwork and Documentation: Strong collaboration, communication, and a detailed engineering journal will be critical to our success.
#Track Details :
 
#Technical Specifications
#Hardware
Component	Description	Image	Link
RASPBERRY PI	Provides processing power for complex deep learning models.	 	https://bit.ly/3wKg5TG

ULTRASONIC SENSOR	Creates a detailed 3D map of the environment for precise navigation and obstacle detection.	 	https://amzn.to/3SXeS2I

2-3 Raspberry Pi Cameras	Capture rich visual data used for object detection, lane tracking, and path planning.	 	https://amzn.to/4c0Tv9o

RC Car Chassis	The physical foundation for our self-driving elf car.	 	https://amzn.to/3uPM0Bz

TCS34725	Enables precise motor control for smooth and reliable movements and steering.	 	https://bit.ly/4a2cHle

Software
C++: Forms the core of our development, allowing for efficient code and optimal performance.

Open-Source Libraries: We'll utilize established deep learning libraries like TensorFlow or PyTorch for training our autonomous driving model, plus libraries for sensor integration and motor control.
Project Structure
Documentation: Comprehensive guides on project goals, hardware setup, software design, the WRO challenge, our engineering journey, and more!
Code: Well-structured C++ code with clear modularity, informative comments, and adherence to best practices.
Data: Curated training data for the deep learning model.
Collaboration, Contribution, and Community
The Ranpo welcome collaboration! Reach out to us through discussions, pull requests, or issues to share your expertise, suggest improvements, or report any challenges you encounter. We're excited to be part of the WRO community and are committed to sharing our progress and lessons learned.
Important
We may not be able to disclose certain implementation details related to our deep learning model or proprietary algorithms to safeguard our competitive edge.
Installation
Vscode & C++ Installation:
Installing Visual Studio Code
Since the Jetson Nano has an ARM-based architecture, you'll need to get VS Code in a few different ways:
1.	Remote Development:
o	This is the recommended approach for complex development. Install VS Code on a more powerful desktop computer (Windows, macOS, or Linux).
o	On your Jetson Nano, install the Remote Development extensions for VS Code: https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.vscode-remote-extensionpack
o	Connect to your Jetson Nano from your desktop VS Code for a seamless development experience.
2.	Install VS Code Server (Less Recommended):
o	You can install a lightweight version of VS Code that runs directly on the Jetson Nano
Setting Up for C++ Development
1.	Install C/C++ Extension: Follow the same instructions as the general guide.
2.	Install a C++ Compiler:
o	Use Ubuntu's package manager:
sudo apt-get install g++
Testing Your Setup:
•	Follow the same steps as the general guide for creating a test C++ file, compiling, and running it.
Note
Additional Considerations for Jetson Nano
•	Performance: The Jetson Nano has limited resources compared to a desktop. You might experience some limitations in terms of speed for lalrge projects.
•	Cross-Compilation: If you prefer working on a desktop PC, you can set up cross-compilation to build code specifically targeting the Jetson Nano's ARM architecture.
ROS installation guide for NVIDIA jetson
Important
Prerequisites
•	Operating System: Ubuntu 18.04 (Bionic Beaver) or Ubuntu 20.04 (Focal Fossa). Check your OS version using lsb_release -a.
•	NVIDIA Hardware: A compatible NVIDIA device (e.g., Jetson Nano, Jetson Xavier NX, etc.).
•	NVIDIA JetPack: If you're using a Jetson device, ensure you have JetPack installed appropriately for your hardware.
Installation Steps
1.	Set Up Sources
o	Configure your Ubuntu repositories to allow "restricted," "universe," and "multiverse."
o	Add the ROS repository:
o	sudo apt-key adv --keyserver 'hkp://keyserver.ubuntu.com:80' --recv-key C1CF6E31E6BADE8868B172B4F42ED6FBAB17C654
sudo sh -c 'echo "deb http://packages.ros.org/ros/ubuntu $(lsb_release -sc) main" > /etc/apt/sources.list.d/ros-latest.list'
2.	Install ROS
o	Update your package lists:
sudo apt update
o	Choose your desired ROS installation:
	Desktop-Full Install: (Recommended for comprehensive use)
sudo apt install ros-YOUR-DISTRO-desktop-full
	Desktop Install: (Core tools and libraries)
sudo apt install ros-YOUR-DISTRO-desktop 
	Base Install: (Bare bones ROS)
sudo apt install ros-YOUR-DISTRO-ros-base 
o	Replace YOUR-DISTRO with either melodic (Ubuntu 18.04) or noetic (Ubuntu 20.04)
3.	Initialize rosdep
4.	sudo rosdep init
rosdep update
5.	Environment Setup
6.	echo "source /opt/ros/YOUR-DISTRO/setup.bash" >> ~/.bashrc
source ~/.bashrc
7.	(Optional) Build Tools
sudo apt install python3-rosdep python3-rosinstall python3-rosinstall-generator python3-wstool build-essential
Testing Your Installation
1.	New Terminal: Open a new terminal.
2.	roscore:
roscore
Auto Install Script
Here's a bash script that automates the installation of ROS, Visual Studio Code (using the Remote Development approach), and the C++ setup on an Ubuntu-based NVIDIA Jetson Nano.
Important
•	Customization: You'll likely need to adjust paths and versions based on your specific requirements.
•	JetPack: I'm assuming you have JetPack installed.
•	Remote Machine: This script assumes you have a desktop machine ready for remote development with VS Code installed.
•	ROS Distribution: I've used 'melodic' (for Ubuntu 18.04). Replace with 'noetic' if you're using Ubuntu 20.04.
The Script (jetson_setup.sh)
Explain
#!/bin/bash

# ROS Installation
echo "== Installing ROS =="
sudo apt-key adv --keyserver 'hkp://keyserver.ubuntu.com:80' --recv-key C1CF6E31E6BADE8868B172B4F42ED6FBAB17C654
sudo sh -c 'echo "deb http://packages.ros.org/ros/ubuntu $(lsb_release -sc) main" > /etc/apt/sources.list.d/ros-latest.list'
sudo apt update
sudo apt install ros-melodic-desktop-full -y
sudo rosdep init
rosdep update
echo "source /opt/ros/melodic/setup.bash" >> ~/.bashrc
source ~/.bashrc

# VS Code Remote Development Setup
echo "== Setting up VS Code Remote Development =="
sudo apt install openssh-server -y  # Install SSH server if not already present 
sudo apt install -y libssl-dev libxkbfile-dev build-essential # Install dependencies

# Install the Remote Development Extensions on your Jetson Nano (refer to the official documentation for the latest URLs)
wget -O vscode_remote.deb "https://update.code.visualstudio.com/latest/linux-arm64-deb/stable" # Replace with the latest version URL
sudo apt install ./vscode_remote.deb

# C++ Setup
echo "== Installing C++ Compiler =="
sudo apt install g++ -y

echo "== Installation Complete =="
echo "**Important:**"
echo "- On your desktop VS Code, connect to your Jetson Nano using Remote Development."
echo "- Ensure necessary C++ build tools are configured on your desktop machine."
How to Use
1.	Create the Script: Copy the code above and save it as jetson_setup.sh on your Jetson Nano.
2.	Make it Executable:
chmod +x jetson_setup.sh
3.	Run the Script:
./jetson_setup.sh
Note
Remember to adjust versions, paths, and setup your desktop VS Code for Remote Development to complete the process!
Stay Tuned!
This repository is a work in progress. Follow our development journey as we build and refine our self-driving car for the WRO Future Engineers 2024 challenge!

