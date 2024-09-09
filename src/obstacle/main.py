from picamera2 import Picamera2
import numpy as np
import cv2

class Cube:
    def __init__(self, color, area, contour):
        self.color = color
        self.area = area
        self.contour = contour

def find_nearest_cube(cubes):
    if not cubes:
        return None
    # Return the cube with the largest area for the nearest approximation
    return max(cubes, key=lambda cube: cube.area)

# Initialize the camera
picam2 = Picamera2()
picam2.configure(picam2.create_preview_configuration())
picam2.start()

while True:
    # Capture an image from the camera
    frame = picam2.capture_array()
    
    # Convert the image to RGB color space
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    
    # Convert the image to HSV color space
    hsv = cv2.cvtColor(rgb_frame, cv2.COLOR_RGB2HSV)

    # Define color ranges for blue and green
    lower_blue = np.array([100, 150, 0])
    upper_blue = np.array([140, 255, 255])
    mask_blue = cv2.inRange(hsv, lower_blue, upper_blue)

    lower_green = np.array([10, 40, 20])
    upper_green = np.array([80, 255, 255])
    mask_green = cv2.inRange(hsv, lower_green, upper_green)

    # Find contours for blue and green masks
    contours_blue, _ = cv2.findContours(mask_blue, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    contours_green, _ = cv2.findContours(mask_green, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    blue_cubes = []
    green_cubes = []

    # Get frame dimensions and center
    height, width, _ = frame.shape
    frame_center = (width // 2, height // 2)

    # Process blue cubes
    for contour in contours_blue:
        if cv2.contourArea(contour) > 120:  # Ignore small areas
            blue_cubes.append(Cube("blue", cv2.contourArea(contour), contour))
            # Draw contours and label on the frame
            cv2.drawContours(rgb_frame, [contour], -1, (0, 0, 255), 2)  # Red contour
            M = cv2.moments(contour)
            if M["m00"] != 0:
                cX = int(M["m10"] / M["m00"])
                cY = int(M["m01"] / M["m00"])
                cv2.circle(rgb_frame, (cX, cY), 5, (0, 0, 255), -1)  # Red center point
                cv2.putText(rgb_frame, "Blue", (cX, cY - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 2)

    # Process green cubes
    for contour in contours_green:
        if cv2.contourArea(contour) > 120:  # Ignore small areas
            green_cubes.append(Cube("green", cv2.contourArea(contour), contour))
            # Draw contours and label on the frame
            cv2.drawContours(rgb_frame, [contour], -1, (0, 255, 0), 2)  # Green contour
            M = cv2.moments(contour)
            if M["m00"] != 0:
                cX = int(M["m10"] / M["m00"])
                cY = int(M["m01"] / M["m00"])
                cv2.circle(rgb_frame, (cX, cY), 5, (0, 255, 0), -1)  # Green center point
                cv2.putText(rgb_frame, "Green", (cX, cY - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

    # Find the nearest blue and green cubes
    nearest_blue_cube = find_nearest_cube(blue_cubes)
    nearest_green_cube = find_nearest_cube(green_cubes)

    # Determine which cube has the largest area
    if nearest_blue_cube and nearest_green_cube:
        if nearest_blue_cube.area > nearest_green_cube.area: 
            if nearest_blue_cube.area > 100000.0:
                print(f"Largest Cube - Blue: Area = {nearest_blue_cube.area} (Turn Right)")
        else:
            if  nearest_green_cube.area > 100000.0:
                print(f"Largest Cube - Green: Area = {nearest_green_cube.area} (Turn Left)")
    elif nearest_blue_cube:
        print(f"Largest Cube - Blue: Area = {nearest_blue_cube.area} (Turn Right)")
    elif nearest_green_cube:
        print(f"Largest Cube - Green: Area = {nearest_green_cube.area} (Turn Left)")
    else:
        print("No Color Detected")

    # Display the frame
    cv2.imshow('Frame', rgb_frame)

    # Exit when 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Clean up
picam2.stop()
cv2.destroyAllWindows()
