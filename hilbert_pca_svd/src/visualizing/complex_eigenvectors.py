from matplotlib.patches import Circle
import matplotlib.pyplot as plt
import numpy as np

def plotting_complex_plane(complex_array, title, rad1=0.1, rad2=0.2, rad3=0.3):

    # Extract the real and imaginary parts and modulus
    real_part = np.real(complex_array)
    imaginary_part = np.imag(complex_array)
    #modulus = np.abs(complex_array)

    # Create a figure and axis
    fig, ax = plt.subplots()

    # Plot the complex array
    ax.scatter(real_part, imaginary_part, color='blue', marker='o')

    # Create a circle patch
    circle1 = Circle((0, 0), radius=rad1, edgecolor='grey', facecolor='none', linewidth=1, linestyle = '--')
    circle2 = Circle((0, 0), radius=rad2, edgecolor='grey', facecolor='none', linewidth=1, linestyle = '--')
    circle3 = Circle((0, 0), radius=rad3, edgecolor='grey', facecolor='none', linewidth=1, linestyle = '--')
    ax.add_patch(circle1)
    ax.add_patch(circle2)
    ax.add_patch(circle3)

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

def plotting_complex_plane_nocircle(complex_array, title):

    # Extract the real and imaginary parts and modulus
    real_part = np.real(complex_array)
    imaginary_part = np.imag(complex_array)
    #modulus = np.abs(complex_array)

    # Create a figure and axis
    fig, ax = plt.subplots()

    # Plot the complex array
    ax.scatter(real_part, imaginary_part, color='blue', marker='o')

    # Set labels and title
    ax.set_xlabel('Real')
    ax.set_ylabel('Imaginary')
    ax.set_title(title)

    # Display the plot
    plt.grid(True)
    plt.show()