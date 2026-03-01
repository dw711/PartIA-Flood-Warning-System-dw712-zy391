import numpy
import matplotlib.dates

def polyfit(dates: list, levels: list, p)->tuple:
    dates = matplotlib.dates.date2num(dates)
    coeffs = numpy.polyfit([i-dates[0] for i in dates], levels, p)
    poly = numpy.poly1d(coeffs)

    return (poly, dates[0])