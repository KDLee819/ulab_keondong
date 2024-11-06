# Special_relativity.py
# This module performs some necessary calculations in special relativity
# Such as calculating Lorentz factor, time dilation and length contraction
# Also does combination of all above, also known as Lorentz boosting in matrix form
# For convenience and simplicity, only x-axis motion will be considered in this module

import numpy as np

def lorentz_factor(v):
    '''
    Will first define the most important quantity in special relativity, Lorentz factor.
    This function calculates the lorentz factor of an object that travels in speed v
    
    Input: speed in m s^-1
    
    Output: lorentz factor γ, γ should be greater than 1
    '''
    # Define constants
    c = 3e8  # speed of light in m/s
    ß = v/c  # relative speed of object
    γ = 1/np.sqrt(1-ß**2)

    # Will round my final value to 4 decimal places
    return round(γ, 4)


def time_dilation(time, v):
    '''
    Calculates the time dilation in a frame that moves in a speed v
    This means if a time measured in a rest frame is t, time dilation will be t'
    t' is calculated simply by multiplying t and γ
    
    Input: time in s, and speed in m s^-1
    
    Output: dilated time t', and t' has to be greater than t
    '''
    # Define constants
    c = 3e8  # speed of light in m/s
    ß = v/c  # relative speed of object
    γ = lorentz_factor(v)

    # Calculate time dilation
    t_prime = γ * time

    # Will round my final value to 4 decimal places
    return round(t_prime, 4)


def length_contraction(length, v):
    '''
    Calculates the length contraction in a frame that moves in a speed v
    This means if a length measured in a rest frame is L, time dilation will be L'
    L' is calculated simply by dividing L and γ
    
    Input: length in m, and speed in m s^-1
    
    Output: contracted length L', and L' has to be less than t
    '''
    # Define constants
    c = 3e8  # speed of light in m/s
    ß = v/c  # relative speed of object
    γ = lorentz_factor(v)

    # Calculate length contraction
    L_prime = length / γ

    # Will round my final value to 4 decimal places
    return round(L_prime, 4)


def lorentz_boost(four_vec, v):
    '''
    Making both time dilatoion and length contraction, combining the two in a
    single linear transformation of a vector seemed good idea

    Input: a 4-vector with components [ct, x, y, z] --> four-vector, list
    Here, ct denotes the time-related space component, 
    x, y, and z denotes each of the positions before transformation
    
    Output: another 4-vector with components [ct', x', y', z'] --> This will also be list
    Here, ct' denotes the lorentz-boosted spacetime component, 
    x', y', and z' denotes each of the positions after transformation
    '''

    # Define constants
    c = 3e8  # speed of light in m/s
    ß = v/c  # relative speed of object
    γ = lorentz_factor(v)
    
    # Will define an operator called Lorentz matrix, Lambda, given by:
    Lambda = np.array([[ γ, -γ*ß, 0, 0],
                       [-γ*ß, γ,  0, 0],
                       [ 0,   0,  1, 0],
                       [ 0,   0,  0, 1]
                      ])

    # This will be our new transformed 4-vector
    four_vec_prime = []

    # Every rows of the matrix undergo a dot product with the input four-vector
    # This is nothing but matrix multiplication of a vector, 
    # which is what Lorentz transformation is all about
    for rows in Lambda:
        four_vec_prime.append(round(np.dot(np.array(rows), np.array(four_vec))))
                            # For simplicity, I will round values to nearest integer

    return four_vec_prime


        