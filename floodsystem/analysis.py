import matplotlib
import numpy as np

def polyfit(dates, levels, p):
    x = matplotlib.dates.date2num(dates)
    y = levels

    p_coeff = np.polyfit(x, y, p)
    # Convert coefficient into a polynomial that can be evaluated,
    # e.g. poly(0.3)
    poly = np.poly1d(p_coeff)
    return poly

def grad(dates, levels, p):
    x = matplotlib.dates.date2num(dates)
    y = levels

    p_grad = np.polyfit(x, y, p)

    recent=matplotlib.dates.date2num(dates[1])
    later=matplotlib.dates.date2num(dates[2])
    y2 = np.polyval(p_grad,recent)
    y1 = np.polyval(p_grad,later)
    grad=(y2-y1)/(recent-later)
    return grad
