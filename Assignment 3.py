
# #Assignment 3
# ###Mathematical Applications in Computer Science

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D



# ###Exercise 1:
# #####(a) Complete the following function:

# 1(a)
def lemniscate(f,d=1000):
    #init theta values from 0 to 2*pi with 1000 points
    theta = np.linspace(0, 2 * np.pi, 1000) #theta = 0:0.01:2*pi;
    
   
    #calculation of r according to the equation
    r = f * np.sqrt(2 * np.cos(2 * theta))
    
    #calculation of x and y according to the equation
    x = r * np.cos(theta)
    y = r * np.sin(theta)
    
     #draw the graph
    plt.figure(figsize=(8, 8))
    plt.plot(x + d, y, label=f'f={f}, d={d}', color='blue')  
    plt.scatter([-f, f], [0, 0], color='red', label='מוקדים')  #מוקדים 
    plt.axhline(0, color='black', linewidth=0.5, linestyle='--')  
    plt.axvline(0, color='black', linewidth=0.5, linestyle='--')  
    plt.gca().set_aspect('equal', adjustable='box')
    plt.title("lemniscate")
    plt.legend()
    plt.xlabel("x")
    plt.ylabel("y")
    plt.grid()
    plt.show()
  


# #####(b) Draw the lemniscate for f=5

# 1(b)
#using first function to plot the lemniscate,d is set to 1000
lemniscate(f=5,d=1000)


# #####(c) Is there a problem with the graph above? If so, what is it? What made this problem? How can we fix/minimize this error? (english)

# 1(c) 
# YES,
# there is a problem in our code,because the formula of r is included sqrt and this is some time not legal because of negative number that cos theta get ,so we get runtime error because of this,because root is just for positive numbers and r is positive (in real life).
# so,to fix it we can make it legal and use the formula that makes problems (r=np.sqrt(2 * np.cos(2 * theta))) if thata is positve or zerro...
# or modify the function to handle negative or undefined values 
# the solution depent on the person who use it and for which purpose,so all aove solution depend on the situation we are in..

# #####(d) Draw another example or 2 which show how your solution is beneficial.
#
# our solutin is ok because this doest make problems in the r formula .
# Masking invalid \(\theta\) values ensures that the square root function only evaluates on valid domains, avoiding runtime errors and producing smooth, continuous lemniscate plots. The corrected approach eliminates artifacts or missing regions and supports flexibility for exploring various parameters "f" and "d", allowing accurate visualization of the lemniscate's shape and position.
#
#
#
# the examples:
# The code demonstrates how to visualize a lemniscate curve by adjusting two parameters:  f  and  d . f  represents the distance of the foci from the center. A larger  f  makes the lemniscate wider, while a smaller  f  makes it narrower.  d shifts the graph along the x-axis. Increasing  d  moves the curve to the right, and decreasing it moves the curve to the left. By experimenting with different values of f and  d, you can see how the curve’s shape and position change. For example, smaller  f  values result in a more compact curve, while larger values make the lemniscate expand. Additionally, changing  d  helps reposition the curve to avoid overlap between multiple graphs. Adjusting  f  affects the width of the lemniscate, while d  controls its horizontal position. These adjustments allow for greater flexibility and clarity when plotting multiple curves.
#
#
#
#
# In this example, f = 5  makes the lemniscate wider by positioning the foci 5 units from the center. The larger  f results in a more pronounced curve.  d = 1500  shifts the curve to the right, preventing overlap with other curves or the y-axis. This adjustment helps in creating a clearer, more readable graph, especially when multiple lemniscates are plotted. The combination of adjusting  f  and  d  allows for better visualization, making the graph well-spaced and easy to interpret.
#
#
#
# 2-
# In this example, let's choose f = 3 and d = 500. With  f = 3 , the foci are placed closer together, resulting in a narrower lemniscate curve. This is useful when you want to focus on a smaller, more compact curve and emphasize the central part of the graph. The value  d = 500  shifts the curve to the right along the x-axis, providing ample space to avoid overlap with the y-axis or other elements in the plot. This choice of  f  and  d  is beneficial for creating a graph that highlights the internal structure of the lemniscate, especially in situations where clarity and spacing between curves are important for better visualization and comparison.
#

def lemniscate(f, d=0):
    #initialize theta values from 0 to 2*pi with 1000 points
    theta = np.linspace(0, 2 * np.pi, 1000)
    
    #calculate cos(2*theta) and filter invalid values (but include where r=0)
    
    cos_2theta = np.cos(2 * theta)
    valid_mask = cos_2theta >= 0
    theta = np.append(theta[valid_mask], [0, np.pi/2, np.pi, 3*np.pi/2])  # Add key points
    theta = np.unique(theta)  # Ensure no duplicates
    
    #calculate r according to the equation
    r = np.zeros_like(theta)
    valid_r_mask = np.cos(2 * theta) >= 0
    r[valid_r_mask] = f * np.sqrt(2 * np.cos(2 * theta[valid_r_mask]))
    
    #calculate x and y
    x = r * np.cos(theta) + d  # Include offset d
    y = r * np.sin(theta)
    
    #draw the graph:
    plt.figure(figsize=(8, 8))
    plt.plot(x, y, label=f'f={f}, d={d}', color='blue')  # Adjusted graph
    plt.scatter([-f + d, f + d], [0, 0], color='red', label='Foci')  # Plot foci
    plt.axhline(0, color='black', linewidth=0.5, linestyle='--')  # X-axis
    plt.axvline(0, color='black', linewidth=0.5, linestyle='--')  # Y-axis
    plt.gca().set_aspect('equal', adjustable='box')
    plt.title("Lemniscate of Bernoulli")
    plt.legend()
    plt.xlabel("x")
    plt.ylabel("y")
    plt.grid()
    plt.show()

# Examples:
# 1. Passes through (0, 0) check
lemniscate(2, d=0)  # Example 1:passes through (0, 0)
lemniscate(3, d=1)  # Example 2:correct offset 


# ###Exercise 2:


# #####(a) Complete the following function:

# 2(a)
def torus(r, R):
  


    """
    Function to generate and plot a torus.

    Parameters:
    R (float): The major radius (distance from the center of the tube to the center of the torus).
    r (float): The minor radius (radius of the tube).
    """
    # Define angles for parameterization
    theta = np.linspace(0, 2 * np.pi, 100)
    phi = np.linspace(0, 2 * np.pi, 100)
    theta, phi = np.meshgrid(theta, phi)

    # Parametric equations for the torus
    x = (R + r * np.cos(theta)) * np.cos(phi)
    y = (R + r * np.cos(theta)) * np.sin(phi)
    z = r * np.sin(theta)

    # Create a 3D plot
    fig = plt.figure(figsize=(10, 8))
    ax = fig.add_subplot(111, projection='3d')
    ax.plot_surface(x, y, z, cmap='viridis', edgecolor='k', alpha=0.8)

    #add labels and title to the plot (x,y,z) to make it more clear ...
    ax.set_title("Torus")
    ax.set_xlabel("X")
    ax.set_ylabel("Y")
    ax.set_zlabel("Z")

    #show the plot 
    plt.show()




# #####(b) Draw a torus with r=R=1

# 2(b)
#using the function to plot the torus with R=2 and r=1 from (a)
torus(R=2, r=1)


# #####(c) Increase the values of r and R (separately). What is the meaning of each of these parameters and how can it be seen in the torus' shape? Draw examples that support your claim.

# 2(c) - code for making the examples:

#examples to demonstrate the different torus shapes:
torus(R=3, r=1)  #Thin ring, large hole.
torus(R=3,r=3)   #Thicker ring, smaller hole.
torus(R=5, r=3)  #Larger ring, smaller hole.
torus(R=5, r=1)  #Larger ring, larger hole


# ANSWER: 
# A torus is defined by two parameters: the major radius (R), which controls the distance from the center of the tube to the center of the torus, and the minor radius (r), which controls the thickness of the tube. Increasing R makes the torus larger and moves it farther from the origin, while increasing r makes the tube thicker, reducing the hole in the center. Larger values of R result in a bigger overall shape, while larger r creates a fuller, thicker ring. Adjusting both parameters together can create a variety of torus shapes, from thin rings to large, thick tubes.
#
#
