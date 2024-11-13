# trigo_subplots.py
# contains two functions that produce two subplots of sin and cos functions
# two functions are different in terms of their arrangement of sin and cos functions
# first function will produce subplots in horizontal arrangement
# second function will produce subplots in vertical arrangement

import numpy as np
import matplotlib.pyplot as plt

def horizontal_subplot(xvals):
    '''
    This is a function that produces sin(x) and cos(x) functions next to each other,
    with sin(x) on the left and cos(x) on the right

    Input: array of the x-range of [0, 2π] with 1000 steps default
    Output: plot of sin(x) on left and cos(x) on right
    '''    
    # Generate two arrays that each contains: sin(x) and cos(x)
    y_sin = np.sin(xvals)
    y_cos = np.cos(xvals)

    # Produce a plot!
    plt.figure(figsize=(10, 5))
    plt.subplot()
    
    # Create subplot
    # h(x)=sin(x)
    plt.subplot(1, 2, 1) # 1 row, 2 columns, 1st plot
    plt.plot(xvals, y_sin, color="green", label=r"$h(x)=sin(x)$")
    plt.xlabel("x-value")
    plt.ylabel("y-value")
    plt.title(r"Plot of $y=h(x)$")
    plt.legend(loc="upper right")

    # k(x)=cos(x)
    plt.subplot(1, 2, 2) # 1 row, 2 columns, 2nd plot
    plt.plot(xvals, y_cos, color="red", label=r"$k(x)=cos(x)$")
    plt.xlabel("x-value")
    plt.ylabel("y-value")
    plt.title(r"Plot of $y=k(x)$")
    plt.legend(loc="upper right")

    plt.tight_layout()
    plt.show()


def vertical_subplot(xvals):
    '''
    This is a function that produces sin(x) and cos(x) functions one above another,
    with sin(x) at the top and cos(x) at the bottom

    Input: array of the x-range of [0, 2π] with 1000 steps default
    Output: plot of sin(x) above and cos(x) below
    '''
    # Generate two arrays that each contains: sin(x) and cos(x)
    y_sin = np.sin(xvals)
    y_cos = np.cos(xvals)

    # Produce a plot!
    plt.figure(figsize=(4, 8))
    plt.subplot()
    
    # Create subplot
    # h(x)=sin(x)
    plt.subplot(2, 1, 1) # 2 rows, 1 column, 1st plot
    plt.plot(xvals, y_sin, color="orange", label=r"$h(x)=sin(x)$")
    plt.xlabel("x-value")
    plt.ylabel("y-value")
    plt.title(r"Plot of $y=h(x)$")
    plt.legend(loc="upper right")

    # k(x)=cos(x)
    plt.subplot(2, 1, 2) # 2 rows, 1 column, 2nd plot
    plt.plot(xvals, y_cos, color="purple", label=r"$k(x)=cos(x)$")
    plt.xlabel("x-value")
    plt.ylabel("y-value")
    plt.title(r"Plot of $y=k(x)$")
    plt.legend(loc="upper right")

    plt.tight_layout()
    plt.show()