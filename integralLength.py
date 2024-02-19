import numpy as np
from scipy import integrate
import sys

k0_value = 0
upper_limit_value = 0

if (len(sys.argv) == 2):
    if (sys.argv[1] == "-help") or \
        (sys.argv[1] == "--help") or \
            (sys.argv[1] == "help") or \
                (sys.argv[1] == "-h") or \
                    (sys.argv[1] == "--h") or \
                        (sys.argv[1] == "h"):
        print("Usage: python integralLength.py k0 [upper_limit]")
        print("k0: the value of k0")
        print("upper_limit: the upper limit of the integral (optional, default: infinity)")
        sys.exit()
    k0_value = float(sys.argv[1])
    upper_limit_value = np.inf
elif (len(sys.argv) == 3):
    k0_value = float(sys.argv[1])
    upper_limit_value = float(sys.argv[2])
else:
    raise TypeError("Wrong number of arguments. Provide one argument for k0,or two arguments for k0 and upper limit. Use \n \
                    python integralLength.py -help \n \
                        for more information.")



x0value  = k0_value
# Define the function to be integrated
def denominator(x,x0 = x0value):
    return (x/x0)**4 * np.exp(-2*(x/x0)**2)

def nominator(x,x0 = x0value):
    return (x/x0)**2 * np.exp(-2*(x/x0)**2)*(1/x)

# Set the integration limits from 0 to infinity
lower_limit = 0
upper_limit = upper_limit_value

# Use the quad function for numerical integration
denominator, deError = integrate.quad(denominator, lower_limit, upper_limit)
nominator,   noError = integrate.quad(nominator, lower_limit, upper_limit)

# Print the result and error
print("result:", nominator/denominator)
print("Error:", noError/denominator)
