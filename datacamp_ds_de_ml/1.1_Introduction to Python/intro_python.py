###############################################################################################
#  Python Basics
###############################################################################################
# area variables (in square meters)
hall = 11.25
kit = 18.0
liv = 20.0
bed = 10.75
bath = 9.50

# Adapt list areas
areas = ["hallway", hall, "kitchen", kit, "living room", liv, "bedroom", bed, "bathroom", bath]

# Print areas
print(areas)

'''
['hallway', 11.25, 'kitchen', 18.0, 'living room', 20.0, 'bedroom', 10.75, 'bathroom', 9.5]
'''

###############################################################################################
#  Lists
###############################################################################################

# area variables (in square meters)
hall = 11.25
kit = 18.0
liv = 20.0
bed = 10.75
bath = 9.50

# house information as list of lists
house = [["hallway", hall],
         ["kitchen", kit],
         ["living room", liv],
         ["bedroom", bed],
         ["bathroom", bath]]

# Print out house
print(house)

# Print out the type of house
print(type(house))

'''
[['hallway', 11.25], ['kitchen', 18.0], ['living room', 20.0], ['bedroom', 10.75], ['bathroom', 9.5]]
<class 'list'>
'''


# Create the areas list
areas = ["hallway", 11.25, "kitchen", 18.0, "living room", 20.0, "bedroom", 10.75, "bathroom", 9.50]

# Correct the bathroom area
areas[-1] = 10.50

# Change "living room" to "chill zone"
areas[4]= "chill zone"


# Create the areas list and make some changes
areas = ["hallway", 11.25, "kitchen", 18.0, "chill zone", 20.0,
         "bedroom", 10.75, "bathroom", 10.50]

# Add poolhouse data to areas, new list is areas_1
areas_1= areas + ["poolhouse", 24.5]

# Add garage data to areas_1, new list is areas_2
areas_2= areas_1 + ["garage", 15.45]


# Create list areas
areas = [11.25, 18.0, 20.0, 10.75, 9.50]

# Create areas_copy
areas_copy = areas[:]

# Change areas_copy
areas_copy[0] = 5.0

# Print areas
print(areas)

'''
[11.25, 18.0, 20.0, 10.75, 9.5]
'''

###############################################################################################
#  Functions and Packages
###############################################################################################

# Create lists first and second
first = [11.25, 18.0, 20.0]
second = [10.75, 9.50]

# Paste together first and second: full
full= first + second

# Sort full in descending order: full_sorted
full_sorted= sorted(full, reverse= True)

# Print out full_sorted
print(full_sorted)

'''
[20.0, 18.0, 11.25, 10.75, 9.5]
'''


# Create list areas
areas = [11.25, 18.0, 20.0, 10.75, 9.50]

# Print out the index of the element 20.0
print(areas.index(20.0))

# Print out how often 9.50 appears in areas
print(areas.count(9.50))

'''
2
1
'''


# Create list areas
areas = [11.25, 18.0, 20.0, 10.75, 9.50]

# Use append twice to add poolhouse and garage size
areas.append(24.5)
areas.append(15.45)

# Pri(nt out areas
print(areas)

# Reverse the orders of the elements in areas
areas.reverse()

# Print out areas
print(areas)

'''
[11.25, 18.0, 20.0, 10.75, 9.5, 24.5, 15.45]
[15.45, 24.5, 9.5, 10.75, 20.0, 18.0, 11.25]
'''


# Definition of radius
r = 192500

# Import radians function of math package
from math import radians

# Travel distance of Moon over 12 degrees. Store in dist.
dist= r*radians(12)

# Print out dist
print(dist)

'''
40317.10572106901
'''

###############################################################################################
#  NumPy
###############################################################################################

# height_in and weight_lb are available as a regular lists

# Import numpy
import numpy as np

# Calculate the BMI: bmi
np_height_m = np.array(height_in) * 0.0254
np_weight_kg = np.array(weight_lb) * 0.453592
bmi = np_weight_kg / np_height_m ** 2

# Create the light array
light= np.array(bmi < 21)

# Print out light
print(light)

# Print out BMIs of all baseball players whose BMI is below 21
print(bmi[light])

'''
[False False False ... False False False]
[20.54255679 20.54255679 20.69282047 20.69282047 20.34343189 20.34343189
 20.69282047 20.15883472 19.4984471  20.69282047 20.9205219 ]
'''


# height_in and weight_lb are available as a regular lists

# Import numpy
import numpy as np

# Store weight and height lists as numpy arrays
np_weight_lb = np.array(weight_lb)
np_height_in = np.array(height_in)

# Print out the weight at index 50
print(np_weight_lb[50])

# Print out sub-array of np_height_in: index 100 up to and including index 110
print(np_height_in[100:111])

'''
200
[73 74 72 73 69 72 73 75 75 73 72]
'''

np_baseball
array([[ 74, 180],
       [ 74, 215],
       [ 72, 210],
       ...,
       [ 75, 205],
       [ 75, 190],
       [ 73, 195]])

# baseball is available as a regular list of lists

# Import numpy package
import numpy as np

# Create a 2D numpy array from baseball: np_baseball
np_baseball= np.array(baseball)

# Print out the shape of np_baseball
print(np_baseball.shape)

np_baseball[:, 1]
'''
array([180, 215, 210, ..., 205, 190, 195])
'''


# baseball is available as a regular list of lists
# updated is available as 2D numpy array

# Import numpy package
import numpy as np

# Create np_baseball (3 cols)
np_baseball = np.array(baseball)
np_baseball + updated

# Create numpy array: conversion
conversion= np.array([0.0254, 0.453592, 1])

# Print out product of np_baseball and conversion
print(np_baseball * conversion)

'''
[[ 1.8796  81.64656 22.99   ]
 [ 1.8796  97.52228 34.69   ]
 [ 1.8288  95.25432 30.78   ]
 ...
 [ 1.905   92.98636 25.19   ]
 [ 1.905   86.18248 31.01   ]
 [ 1.8542  88.45044 27.92   ]]
'''


# np_baseball is available

# Import numpy
import numpy as np

# Create np_height_in from np_baseball
np_height_in= np_baseball[:, 0]

# Print out the mean of np_height_in
print(np.mean(np_height_in))

# Print out the median of np_height_in
print(np.median(np_height_in))


np_baseball
'''
array([[ 74.  , 180.  ,  22.99],
       [ 74.  , 215.  ,  34.69],
       [ 72.  , 210.  ,  30.78],
       ...,
       [ 75.  , 205.  ,  25.19],
       [ 75.  , 190.  ,  31.01],
       [ 73.  , 195.  ,  27.92]])
'''
# np_baseball is available

# Import numpy
import numpy as np

# Print mean height (first column)
avg = np.mean(np_baseball[:,0])
print("Average: " + str(avg))

# Print median height. Replace 'None'
med = np.median(np_baseball[:,0])
print("Median: " + str(med))

# Print out the standard deviation on height. Replace 'None'
stddev = np.std(np_baseball[:,0])
print("Standard Deviation: " + str(stddev))

# Print out correlation between first and second column. Replace 'None'
corr = np.corrcoef(np_baseball[:, 0], np_baseball[:, 1])
print("Correlation: " + str(corr))

'''
Average: 73.6896551724138
Median: 74.0
Standard Deviation: 2.312791881046546
Correlation: [[1.         0.53153932]
 [0.53153932 1.        ]]
'''


'''
np_positions
array(['GK', 'M', 'A', ..., 'D', 'D', 'M'], dtype='<U2')

np_heights
array([191, 184, 185, ..., 183, 179, 179])
'''
# heights and positions are available as lists

# Import numpy
import numpy as np

# Convert positions and heights to numpy arrays: np_positions, np_heights
np_positions= np.array(positions)
np_heights= np.array(heights)

# Heights of the goalkeepers: gk_heights
gk_heights= np_heights[np_positions == 'GK']

# Heights of the other players: other_heights
other_heights= np_heights[np_positions != 'GK']

# Print out the median height of goalkeepers. Replace 'None'
print("Median height of goalkeepers: " + str(np.median(gk_heights)))

# Print out the median height of other players. Replace 'None'
print("Median height of other players: " + str(np.median(other_heights)))

'''
Median height of goalkeepers: 188.0
Median height of other players: 181.0
'''

###############################################################################################