import math
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patches

# Subroutine for the modified function.
# It is only called within or near the interval [-pi/2, pi/2].
def g(x, k):
    return math.atan2(k * math.sin(x), math.cos(x))

# MODIFIED VERSION OF THE FUNCTION f(x) = arctan(k*tan(x))
# The modified version agrees with arctan(k*tan(x)) on (-pi/2, pi/2).
# It is defined for all real x, and has derivative k/( cos^2(x) + k^2*sin^2(x) )
def arctanktan_modified(x, k):
    pi = math.pi
    n = round(x / pi)
    npi = n*pi
    if k > 0:
        return g(x - npi, k) + npi
    elif k < 0:
        return g(x - npi, k) - npi
    else:
        return 0
    
# Plot the modified function for a given value of k.
def plot_arctanktan_modified(k):
    # Start a new graph.
    plt.figure()
    
    # Let the title show the value k.
    plt.title('k = '+ str(k))
    
    # Set horizonatal and vertical axes.
    plt.axhline(0, color='black', linewidth=0.5)
    plt.axvline(0, color='black', linewidth=0.5)
    
    # Let the aspect ratio be 1:1.
    plt.gca().set_aspect('equal', adjustable='box')
    
    # Plot 1000 points (x,y) where y = arctanktan_modified(x, k),
    # and the x values are equally spaced in the range -5pi/2 to 5pi/2.
    x_list = np.linspace(-5*math.pi/2, 5*math.pi/2, 1000)
    y_list = [arctanktan_modified(x, k) for x in x_list]
    plt.plot(x_list, y_list)
    
    # Label ticks on the axes.
    strPI = '\u03C0'
    ticks = [v*math.pi/2 for v in[-5,-3,-1,1,3,5]]
    labels = ['-5'+strPI+'/2','-3'+strPI+'/2','-'+strPI+'/2', strPI+'/2','3'+strPI+'/2','5'+strPI+'/2']
    plt.xticks(ticks, labels)
    plt.yticks(ticks, labels)
    
    # Plot a central square around the graph where it agrees with arctan(k*tan(x)).
    square = patches.Rectangle((-math.pi/2, -math.pi/2), width=math.pi, height=math.pi, linewidth=0.5, edgecolor='red', facecolor='none')
    plt.gca().add_patch(square)
    
    # Plot diagonally translated squares to highlight the symmetry.
    if k > 0:
        square = patches.Rectangle((-5*math.pi/2, -5*math.pi/2), width=math.pi, height=math.pi, linewidth=0.5, edgecolor='red', facecolor='none')
        plt.gca().add_patch(square)
        square = patches.Rectangle((-3*math.pi/2, -3*math.pi/2), width=math.pi, height=math.pi, linewidth=0.5, edgecolor='red', facecolor='none')
        plt.gca().add_patch(square)
        square = patches.Rectangle((math.pi/2, math.pi/2), width=math.pi, height=math.pi, linewidth=0.5, edgecolor='red', facecolor='none')
        plt.gca().add_patch(square)
        square = patches.Rectangle((3*math.pi/2, 3*math.pi/2), width=math.pi, height=math.pi, linewidth=0.5, edgecolor='red', facecolor='none')
        plt.gca().add_patch(square)
    if k < 0:
        square = patches.Rectangle((-5*math.pi/2, 3*math.pi/2), width=math.pi, height=math.pi, linewidth=0.5, edgecolor='red', facecolor='none')
        plt.gca().add_patch(square)
        square = patches.Rectangle((-3*math.pi/2, math.pi/2), width=math.pi, height=math.pi, linewidth=0.5, edgecolor='red', facecolor='none')
        plt.gca().add_patch(square)
        square = patches.Rectangle((math.pi/2, -3*math.pi/2), width=math.pi, height=math.pi, linewidth=0.5, edgecolor='red', facecolor='none')
        plt.gca().add_patch(square)
        square = patches.Rectangle((3*math.pi/2, -5*math.pi/2), width=math.pi, height=math.pi, linewidth=0.5, edgecolor='red', facecolor='none')
        plt.gca().add_patch(square)
    
# Study behavior of the modified function.
# Since x1 and x2 are near, so should be y1 and y2,
# even though n is different in the two calculations.    
x1 = 3*math.pi/2 - 0.001 # n will be 1
y1 = arctanktan_modified(x1, 2)
x2 = 3*math.pi/2 + 0.001 # n will be 2
y2 = arctanktan_modified(x2, 2)

# DO PLOTS FOR VARIOUS k VALUES.
plot_arctanktan_modified(2)
plot_arctanktan_modified(1)
plot_arctanktan_modified(1/2)
plot_arctanktan_modified(0)
plot_arctanktan_modified(-1/2)
plot_arctanktan_modified(-1)
plot_arctanktan_modified(-2)

# Show all the plots.
plt.show()

pass
