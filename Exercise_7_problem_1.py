#!/usr/bin/env python
# coding: utf-8

# ## Problem 1: Simple scatter plot using random 
# 
# We can generate random numbers using using a method `random.rand()` from the [NumPy package](https://numpy.org/). This example generates 10 random values:
# 
# ```
# import numpy as np
# random_numbers = np.random.rand(10)
# 
# ```
# 
# ### Part 1
# 

# Create an new data frame called `data` and add 1000 random numbers (`float`) into a new column `x` and another 1000 random numbers (`float`) into a new column `y`.

import numpy as np
import pandas as pd

# YOUR CODE HERE 1 to set data
#1000 random numbers row x
random_numbersx=np.random.rand(1000) 
#1000 random numbers row y
random_numbersy=np.random.rand(1000) 
#input dataframe"x"
data=pd.DataFrame({'x':random_numbersx}) 
#append dataframe"y"
data["y"]=random_numbersy

# Check your random values
print(data.head())

# Check that you have the correct number of rows
assert len(data) == 1000, "There should be 1000 rows of data."


# ### Part 2
#create 1000 random colors in variable "colors"
colors=np.random.rand(1000) 

# YOUR CODE HERE 2 to set colors

# This test print should print out 10 first numbers in the variable colors
print(colors[0:10])

# Check that the length matches
assert len(colors) == 1000, "There should be 1000 random numbers for colors"


# ### Part 3 
# 
# #### Part 3.1
# 
# Create a scatter plot of points with random colors
# 
# #### Part 3.2
# 
# #### Part 3.3
# 

# Plot a scatter plot
# YOUR CODE HERE 3
import matplotlib.pyplot as plt
# "cm is a variable of colormap"
cm = plt.cm.get_cmap('Spectral')
#input scatter plot with size, color, edgecolor, and cmap
plt.scatter(random_numbersx,random_numbersy,s=50, c=colors,edgecolors="black",cmap=cm)
# Add labels and title
# YOUR CODE HERE 4
#create title
plt.title("My random candy points")
#create xlabel
plt.xlabel("X-label")
#create ylabel
plt.ylabel("Y-label")
# Save the plot as a png file:
outputfp = "my_first_plot.png"

# YOUR CODE HERE 5
#Save the plot as png file
plt.savefig(outputfp)
# This test print statement should print the output filename of your figure
print("Saved my first plot as:", outputfp)

#Check that the file exists (also go and open the file to check that everything is ok!)
import os

assert os.path.exists(outputfp), "Can't find the output image."


# Remember to commit your changes (including the image file) to your GitHub repo!
# 
# ### Done!
# 
# Now you can move to [problem 2](Exercise-7-problem-2.ipynb).
