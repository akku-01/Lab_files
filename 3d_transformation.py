import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def translate_3d_point(point, translation_vector):
    # Ensure the point and translation_vector are both 3D vectors (x, y, z)
    if len(point) != 3 or len(translation_vector) != 3:
        raise ValueError("Both point and translation_vector must be 3D vectors.")

    # Perform translation
    translated_point = [point[0] + translation_vector[0],
                        point[1] + translation_vector[1],
                        point[2] + translation_vector[2]]
    return translated_point

# Original point
point = [1, 2, 3]

# Translation vector
translation_vector = [2, 3, 1]

# Perform 3D translation
translated_point = translate_3d_point(point, translation_vector)

# Create a 3D plot
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Plot the original point
ax.scatter(point[0], point[1], point[2], c='r', label='Original Point')

# Plot the translated point
ax.scatter(translated_point[0], translated_point[1], translated_point[2], c='b', label='Translated Point')

# Set labels and title
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.set_title('3D Translation of a Point')

# Add a legend
ax.legend()

# Show the plot
plt.show()
