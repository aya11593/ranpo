# Mobility Management



In order to fully maximize the 300mm x 200mm space given, we combined the motors and our chassis in the most optimal way possible.

1. ## Obstacle Detection and Avoidance:
  - Continuously monitor the camera to detect the color of the traffic signs.
  - If a green sign is detected, adjust the vehicle's position to keep to the left side of the lane.
  - If a red sign is detected, adjust the vehicle's position to keep to the right side of the lane.
  - If the last sign of the second round is reached, make the decision to:
    - Continue in the same direction (if the sign was green), or
    - Turn around (if the sign was red).

2. ## Motors:
  - We used one MG996R servo motor and one DC motor.
  - The servo motor was connected to the raspberry pi on the raspbot to allow the robot to turn.
  - The DC motor was connected to the raspberry pi on the raspbot to make the robot move forward or backward.
  - Each motor has its own wheels ( the servo turns 2 wheels that aren't being driven by the DC motor, and the DC motor drives 2 wheels that don't turn).

3. ## Turning mechanism:
  - We wanted very precise movements, so we used the servo motor in conjunction with a long bar to turn both front wheels at the same time.

4. ## Mounting parts:
  - We mounted all of our sensors with hot glue, as it is the most secure way to keep thing where they are without actually weakening the chassis (we don't have 3D printer).
  - Keep track of the vehicle's current position and orientation on the map.

5. ## Motor Control and Navigation:
  - Based on the planned path and the detected traffic signs, control the motors or actuators of the vehicle to navigate through the track.
  - Implement appropriate motor control algorithms to follow the planned path and adjust the position based on the detected signs.
  - Use feedback control mechanisms to ensure accurate navigation and adherence to the lane sides.

6. ## Iterative Process:
  - Continuously iterate through steps 4-6 to dynamically adjust the planned path, respond to the detected signs, and complete three laps while avoiding obstacles and following the lane sides.
    
