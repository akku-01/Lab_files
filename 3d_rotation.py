import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def rotate_3d_point(point, angle_degrees, axis):
    # Ensure the point is a 3D vector (x, y, z)
    if len(point) != 3:
        raise ValueError("The point must be a 3D vector.")
    
    # Convert the angle from degrees to radians
    angle_radians = np.radians(angle_degrees)
    
    # Create a rotation matrix based on the axis and angle
    if axis == 'x':
        rotation_matrix = np.array([[1, 0, 0],
                                    [0, np.cos(angle_radians), -np.sin(angle_radians)],
                                    [0, np.sin(angle_radians), np.cos(angle_radians)]])
    elif axis == 'y':
        rotation_matrix = np.array([[np.cos(angle_radians), 0, np.sin(angle_radians)],
                                    [0, 1, 0],
                                    [-np.sin(angle_radians), 0, np.cos(angle_radians)]])
    elif axis == 'z':
        rotation_matrix = np.array([[np.cos(angle_radians), -np.sin(angle_radians), 0],
                                    [np.sin(angle_radians), np.cos(angle_radians), 0],
                                    [0, 0, 1]])
    else:
        raise ValueError("Invalid rotation axis. Use 'x', 'y', or 'z'.")

    # Perform rotation
    rotated_point = np.dot(rotation_matrix, point)
    return rotated_point

# Original point
point = np.array([1, 2, 3])

# Rotation angle in degrees
angle_degrees = 45

# Rotation axis ('x', 'y', or 'z')
rotation_axis = 'y'

# Perform 3D rotation
rotated_point = rotate_3d_point(point, angle_degrees, rotation_axis)

# Create a 3D plot
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Plot the original point
ax.scatter(point[0], point[1], point[2], c='r', label='Original Point')

# Plot the rotated point
ax.scatter(rotated_point[0], rotated_point[1], rotated_point[2], c='b', label='Rotated Point')

# Set labels and title
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.set_title(f'3D Rotation of a Point (Axis: {rotation_axis}, Angle: {angle_degrees} degrees)')

# Add a legend
ax.legend()

# Show the plot
plt.show()
