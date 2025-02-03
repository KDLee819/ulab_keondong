# Module name: Planet_analyser
'''
What this module does:
contains function(s) that analyse the planetary motions

Function 1:
calculate_period(a)
    Input: semi-major axis a, in units of AU
    Output: orbital period T, in units of years
'''

def calculate_period(a):
    '''
    Function name: calculate_period
    Input: semi-major axis a, in units of AU
    Output: orbital period T, in units of years
    
    '''
    # Calculate period using the given Kepler's third law, and name it orbital_period
    orbital_period = a ** 1.5

    # return this as the output of the function 
    return orbital_period