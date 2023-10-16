import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def scale_3d_point(point, scale_factors):
    # Ensure the point and scale_factors are both 3D vectors (x, y, z)
    if len(point) != 3 or len(scale_factors) != 3:
        raise ValueError("Both point and scale_factors must be 3D vectors.")
    
    # Perform scaling
    scaled_point = [point[0] * scale_factors[0],
                    point[1] * scale_factors[1],
                    point[2] * scale_factors[2]]
    return scaled_point

# Original point
point = [1, 2, 3]

# Scaling factors along X, Y, and Z axes
scale_factors = [2, 1.5, 0.5]

# Perform 3D scaling
scaled_point = scale_3d_point(point, scale_factors)

# Create a 3D plot
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Plot the original point
ax.scatter(point[0], point[1], point[2], c='r', label='Original Point')

# Plot the scaled point
ax.scatter(scaled_point[0], scaled_point[1], scaled_point[2], c='b', label='Scaled Point')

# Set labels and title
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.set_title(f'3D Scaling of a Point (Scale Factors: {scale_factors[0]}, {scale_factors[1]}, {scale_factors[2]})')

# Add a legend
ax.legend()

# Show the plot
plt.show()
