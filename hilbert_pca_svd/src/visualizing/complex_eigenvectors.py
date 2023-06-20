from matplotlib.patches import Circle
import matplotlib.pyplot as plt
import numpy as np

def plotting_complex_plane(complex_array, title):

    # Extract the real and imaginary parts and modulus
    real_part = np.real(complex_array)
    imaginary_part = np.imag(complex_array)
    #modulus = np.abs(complex_array)

    # Create a figure and axis
    fig, ax = plt.subplots()

    # Plot the complex array
    ax.scatter(real_part, imaginary_part, color='blue', marker='x')

    # Create a circle patch
    circle1 = Circle((0, 0), radius=0.05, edgecolor='grey', facecolor='none', linewidth=1, linestyle = '--')
    #circle2 = Circle((0, 0), radius=0.1, edgecolor='grey', facecolor='none', linewidth=1, linestyle = '--')

    # Add the circle patch to the plot
    ax.add_patch(circle1)
    #ax.add_patch(circle2)

    # Set the x and y limits
    #ax.set_xlim([-4, 4])
    #ax.set_ylim([-4, 4])

    # Set labels and title
    ax.set_xlabel('Real')
    ax.set_ylabel('Imaginary')
    ax.set_title(title)

    # Display the plot
    plt.grid(True)
    plt.show()