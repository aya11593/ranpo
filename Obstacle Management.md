# Our approach for the Obstacle Challenge involves several key steps:
1. ## Define the Obstacle Course:
   -  The course consists of a track with randomly placed green and red traffic signs.
   -  Green signs indicate that the vehicle should keep to the left side of the lane, while red signs indicate that it should keep to the right side.
   -  The final sign encountered in the second round determines whether the vehicle should continue in the same direction (if the sign is green) or turn around and complete the third round in the opposite direction (if the sign is red).
   -  The vehicle must complete three laps without moving or knocking down the traffic signs. The initial direction (clockwise or counterclockwise) and the positions of the traffic signs are randomized for each round.
3. ##	Camera Integration:
   - we utilize a camera connected to the Raspberry Pi to detect and recognize the traffic signs.
   - Computer vision techniques are employed to process the camera feed and identify the color and position of the signs.
   - The camera continuously captures images, which are analyzed to determine the vehicle’s next actions based on the detected traffic signs.
4. ##	Mapping the Course:
   - A digital map or representation of the track and the traffic sign positions is created.
   - The vehicle’s current position and orientation on this map are tracked using data from the camera .
   - This map helps in navigation and decision-making.
5. ##	Obstacle Detection and Avoidance:
   -  The camera feed is processed in real-time to detect the color of the traffic signs.
   -  When a green sign is detected, the vehicle adjusts its position to stay on the left side of the lane.
   -  When a red sign is detected, the vehicle adjusts its position to stay on the right side.
   -  Upon reaching the last sign of the second round, the decision to continue in the same direction or turn around is based on the color of the sign.
6. ##	Motor Control and Navigation:
   - Based on the camera’s analysis of the detected traffic signs, the Raspberry Pi controls the motors or actuators of the vehicle to navigate through the track.
   - Motor control algorithms are implemented in Python to ensure the vehicle follows the planned path and adjusts its position according to the detected signs.
   - Feedback control mechanisms are used to maintain accurate navigation and lane adherence.
7. ##	Iterative Process:
   - The vehicle iteratively processes the camera feed to detect signs, adjust its position, and navigate accordingly.
   - It continuously responds to the detected signs and completes the three laps while avoiding obstacles and following the lane sides.

