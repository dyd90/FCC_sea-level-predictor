import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress
import os
import numpy as np

def draw_plot():
    # Read data from file
    df = pd.read_csv(os.getcwd() +  "/epa-sea-level.csv")

    x = df['Year']
    y = df['CSIRO Adjusted Sea Level']

    # Create scatter plot
    plt.scatter(x, y)

    # Create first line of best fit
    slope, intercept, r, p, se = linregress(x, y)

    line_x = np.arange(x.min(), 2051)
    line_y = slope*line_x + intercept
    plt.plot(line_x, line_y)

    # Create second line of best fit
    df_p2 = df[df['Year'] >= 2000]
    x2 = df_p2['Year']
    y2 = df_p2['CSIRO Adjusted Sea Level']
    slope, intercept, r, p, se = linregress(x2, y2)

    line_x = np.arange(x2.min(), 2051)
    line_y = slope*line_x + intercept
    plt.plot(line_x, line_y)

    # Add labels and title
    plt.title("Rise in Sea Level")
    plt.xlabel("Year")
    plt.ylabel("Sea Level (inches)")

    plt.xticks(np.arange(1850.0, 2100.0, 25.0))
    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()