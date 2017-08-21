# Credits to @Micah on StackOverflow
# got this function from https://stackoverflow.com/questions/22239691/code-for-line-of-best-fit-of-a-scatter-plot-in-python
# Added some of my own code to increase redability and made it work with NaN's in the data

# Function to plot a Line of best Fit (Trendline)
import numpy as np
import matplotlib.pyplot as plt

def trendline(xd, yd, order=1, c='r', alpha=1, Rval=True):
    """Make a line of best fit,
       Set Rval=False to print the R^2 value on the plot"""

    #Only be sure you are using valid input (not NaN)
    idx = np.isfinite(xd) & np.isfinite(yd)

	#Calculate trendline
    coeffs = np.polyfit(xd[idx], yd[idx], order)

    intercept = coeffs[-1]
    slope = coeffs[-2]
    power = coeffs[0] if order == 2 else 0

    minxd = np.min(xd)
    maxxd = np.max(xd)

    xl = np.array([minxd, maxxd])
    yl = power * xl ** 2 + slope * xl + intercept

    #Plot trendline
    plt.plot(xl, yl, c, alpha=alpha)

    #Calculate R Squared
    p = np.poly1d(coeffs)

    ybar = np.sum(yd) / len(yd)
    ssreg = np.sum((p(xd) - ybar) ** 2)
    sstot = np.sum((yd - ybar) ** 2)
    Rsqr = ssreg / sstot

    if not Rval:
        #Plot R^2 value
        plt.text(0.8 * maxxd + 0.2 * minxd, 0.8 * np.max(yd) + 0.2 * np.min(yd),
                 '$R^2 = %0.2f$' % Rsqr)
    else:
        #Return the R^2 value:
        return Rsqr
