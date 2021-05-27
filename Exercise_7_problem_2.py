#!/usr/bin/env python
# coding: utf-8

# ## Problem 2 - Plotting temperatures 
# 
# In this problem we will  plot monthly mean temperatures from the Helsinki-Vantaa airpot for the past 30 years.
# 
# ## Input data
# 
# File `data/helsinki-vantaa.csv` monthly average temperatures from Helsinki Vantaa airport. Column descriptions:
# 
# ### Part 1
# 
# Load the Helsinki temperature data (`data/helsinki-vantaa.csv`)
# 
# - Read the data into variable called `data` using pandas
# - Parse dates from the column `'DATE'` and set the dates as index in the dataframe 

# YOUR CODE HERE 1 to read the data into data and parse dates
import numpy as np
import pandas as pd
#"fp" is variable of csv file.
fp = r'data/helsinki-vantaa.csv'
#read the csv file into data. 
data = pd.read_csv(fp,parse_dates=['DATE'], index_col='DATE')

# This test print should print first five rows
print(data.head())

# Check the number of rows in the data frame
print(len(data))

# ### Part 2
# 
# Select data for a 30 year period (January 1988 - December 2018)
# 
# - Store the selection in a new variable `selection`

# YOUR CODE HERE 2
# "selection" is the extracted data in data.
selection = data.loc[(data.index >= '19880101') & (data.index <= '20181231')]
# Check that the data was read in correctly:
selection.head()

# Check how many rows of data you selected:
print("Number of rows:", len(selection))


# ### Part 3
# 
# #### Part 3.1
# 
# Create a line plot that displays the temperatures (`TEMP_C`) for yeach month in the 30 year time period:
#      
# #### Part 3.2
# 
# Save your figure as PNG file called `temp_line_plot.png`.
# 

# YOUR CODE HERE 3
import matplotlib.pyplot as plt
thirty_years_temps = selection['TEMP_C']
#create plot
ax=thirty_years_temps.plot(linestyle="solid",color="black",marker="o",markersize=3,figsize=(14,6))
#create title
ax.set_title('Helsinki-Vantaa Airport')
#create xlabel
ax.set_xlabel('Time')
#create ylabel
ax.set_ylabel('Temperature(Celsius)')
ax.grid()

# Set output file name
outputfp = "temp_line_plot.png"

# Save plot as image
# YOUR CODE HERE 4
#Save the plot as png file
plt.savefig(outputfp)

import os

#Check that output file exists (also open the file and check that the plot looks ok!)
os.path.exists(outputfp)


# **REMINDER**: Don't forget to upload your figure and the modified notebook into your personal GitHub repository!
# 
# ### Done!
