# DIY_trig_combo.py
# This is a module I made that contains different types of trig functions
# includes a function that plots the three ordinary trig function, sin cos tan
# includes a function that plots the three inverse trig function, arcsin arccos arctan
# includes a function that plots the three hyperbolic trig function, sinh cosh tanh
# includes a function that plots the three inverse hyperbolic trig function, arcsinh arccosh arctanh

import numpy as np
import matplotlib.pyplot as plt

def plot_ordinary_trig(x_array):
    '''
    This is a function that receives an array with a certain domain,
    and returns a plot of three trig functions, all side-by-side

    Input: array of certain range of domain
    Output: three plots of sin, cos, and tan
    '''
    # Generate three arrays that contain: sin(x) cos(x), and tan(x)
    y_sin = np.sin(x_array)
    y_cos = np.cos(x_array)
    y_tan = np.tan(x_array)

    # Produce plot with three subplots
    plt.figure(figsize=(9,3))
    plt.subplot()

    # First subplot: sin(x)
    plt.subplot(1, 3, 1) # 1 row, 3 columns, 1st plot
    plt.plot(x_array, y_sin, color="red", label=r"$y=sin(x)$")
    plt.xlabel("x-value")
    plt.ylabel("y-value")
    plt.title(r"Plot of $y=sin(x)$")
    plt.legend(loc="upper right")

    # Second subplot: cos(x)
    plt.subplot(1, 3, 2) # 1 row, 3 columns, 2nd plot
    plt.plot(x_array, y_cos, color="green", label=r"$y=cos(x)$")
    plt.xlabel("x-value")
    plt.ylabel("y-value")
    plt.title(r"Plot of $y=cos(x)$")
    plt.legend(loc="upper right")

    # Third subplot: tan(x)
    plt.subplot(1, 3, 3) # 1 row, 3 columns, 3rd plot
    
    # One thing special about tan(x) is its asymptote!
    y_tan[np.abs(y_tan) > 10] = np.nan  # Don't plot for y-values greater than 10
    asymptotes = np.arange(-100.5 * np.pi, 100.5 * np.pi, np.pi)
    
    # Mark asymptotes with dotted vertical lines
    for asymptote in asymptotes:
        plt.axvline(x=asymptote, color="grey", linestyle="--")
        
    plt.plot(x_array, y_tan, color="blue", label=r"$y=tan(x)$")
    plt.xlabel("x-value")
    plt.ylabel("y-value")
    plt.xlim(list(x_array)[0], list(x_array)[-1]) # x-limit always first and last values of the array

    plt.title(r"Plot of $y=tan(x)$")
    plt.legend(loc="upper right")

    plt.tight_layout()
    plt.show()


def plot_inv_trig(x_array):
    '''
    This is a function that receives an array with a certain domain,
    and returns a plot of three inverse trig functions, all side-by-side
    Be mindful to set the range of x from this function,
    because arcsin and arccos is defined only for x values for [-1, 1]

    Input: array of certain range of domain
    Output: three plots of arcsin, arccos, and arctan
    '''
    # Generate three arrays that contain: arcsin(x) arccos(x), and arctan(x)
    y_arcsin = np.arcsin(x_array)
    y_arccos = np.arccos(x_array)
    y_arctan = np.arctan(x_array)

    # Produce plot with three subplots
    plt.figure(figsize=(9,3))
    plt.subplot()

    # First subplot: arcsin(x)
    plt.subplot(1, 3, 1) # 1 row, 3 columns, 1st plot
    x_array[np.abs(x_array) > 1] = np.nan
    plt.plot(x_array, y_arcsin, color="red", label=r"$y=arcsin(x)$")
    plt.xlabel("x-value")
    plt.ylabel("y-value")
    plt.title(r"Plot of $y=arcsin(x)$")
    plt.legend(loc="upper right")

    # Second subplot: arccos(x)
    plt.subplot(1, 3, 2) # 1 row, 3 columns, 2nd plot
    x_array[np.abs(x_array) > 1] = np.nan
    plt.plot(x_array, y_arccos, color="green", label=r"$y=arccos(x)$")
    plt.xlabel("x-value")
    plt.ylabel("y-value")
    plt.title(r"Plot of $y=arccos(x)$")
    plt.legend(loc="upper right")

    # Third subplot: arctan(x)
    plt.subplot(1, 3, 3) # 1 row, 3 columns, 3rd plot
    plt.plot(x_array, y_arctan, color="blue", label=r"$y=arctan(x)$")
    plt.xlabel("x-value")
    plt.ylabel("y-value")
    plt.title(r"Plot of $y=arctan(x)$")
    plt.legend(loc="upper right")

    # Mark asymptotes with dotted horizontal lines
    plt.axhline(-np.pi/2, color="grey", linestyle="--")
    plt.axhline(np.pi/2, color="grey", linestyle="--")

    plt.tight_layout()
    plt.show()


def plot_hyp_trig(x_array):
    '''
    This is a function that receives an array with a certain domain,
    and returns a plot of three hyperbolic trig functions, all side-by-side

    Input: array of certain range of domain
    Output: three plots of hyperbolic trig functions sinh, cosh, tanh
    '''
    # Initialize different hyperbolic functions using np.exp() function
    y_sinh = (np.exp(x_array) - np.exp(-x_array)) / 2
    y_cosh = (np.exp(x_array) + np.exp(-x_array)) / 2
    y_tanh = y_sinh / y_cosh

    # Produce plot with three subplots
    plt.figure(figsize=(9,3))
    plt.subplot()

    # First subplot: sinh(x)
    plt.subplot(1, 3, 1) # 1 row, 3 columns, 1st plot
    plt.plot(x_array, y_sinh, color="red", label=r"$y=sinh(x)$")
    plt.xlabel("x-value")
    plt.ylabel("y-value")
    plt.title(r"Plot of $y=sinh(x)$")
    plt.legend(loc="upper right")

    # Second subplot: cosh(x)
    plt.subplot(1, 3, 2) # 1 row, 3 columns, 2nd plot
    plt.plot(x_array, y_cosh, color="green", label=r"$y=cosh(x)$")
    plt.xlabel("x-value")
    plt.ylabel("y-value")
    plt.title(r"Plot of $y=cosh(x)$")
    plt.legend(loc="upper right")

    # Third subplot: tanh(x)
    plt.subplot(1, 3, 3) # 1 row, 3 columns, 3rd plot
    plt.plot(x_array, y_tanh, color="blue", label=r"$y=tanh(x)$")
    plt.xlabel("x-value")
    plt.ylabel("y-value")
    plt.title(r"Plot of $y=tanh(x)$")
    plt.legend(loc="upper right")

    plt.tight_layout()
    plt.show()


def plot_inv_hyp(x_array):
    '''
    This is a function that receives an array with a certain domain,
    and returns a plot of three inverse hyperbolic trig functions, all side-by-side
    Be mindful for the domain of arccosh and arctanh, each with x >= 1 and -1 < x < 1

    Input: array of certain range of domain
    Output: three plots of inverse hyperbolic trig functions arcsinh, arccosh, arctanh
    '''
    # Initialize inverse hyperbolic functions using np.exp() function
    y_arcsinh = np.arcsinh(x_array)
    y_arccosh = np.arccosh(x_array)
    y_arctanh = np.arctanh(x_array)

    # Produce plot with three subplots
    plt.figure(figsize=(9,3))
    plt.subplot()

    # First subplot: arcsinh(x)
    plt.subplot(1, 3, 1) # 1 row, 3 columns, 1st plot
    plt.plot(x_array, y_arcsinh, color="red", label=r"$y=arcsinh(x)$")
    plt.xlabel("x-value")
    plt.ylabel("y-value")
    plt.title(r"Plot of $y=arcsinh(x)$")
    plt.legend(loc="upper right")

    # Second subplot: arccosh(x)
    plt.subplot(1, 3, 2) # 1 row, 3 columns, 2nd plot
    x_array[x_array < 1] = np.nan
    plt.plot(x_array, y_arccosh, color="green", label=r"$y=arccosh(x)$")
    plt.xlabel("x-value")
    plt.ylabel("y-value")
    plt.title(r"Plot of $y=arccosh(x)$")
    plt.legend(loc="upper right")

    # Third subplot: arctanh(x)
    plt.subplot(1, 3, 3) # 1 row, 3 columns, 3rd plot
    x_array[np.abs(x_array) > 1] = np.nan
    plt.plot(x_array, y_arctanh, color="blue", label=r"$y=arctanh(x)$")
    plt.xlabel("x-value")
    plt.ylabel("y-value")
    plt.title(r"Plot of $y=arctanh(x)$")
    plt.legend(loc="upper right")

    plt.tight_layout()
    plt.show()







