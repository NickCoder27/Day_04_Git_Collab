


"""
So very confusing, please work

So confusing
To use this notebook for your in-class assignment, you will need these 
files, which you shoujld have downloaded:
* mhu.csv -- Lake Michigan and Lake Huron
* sup.csv -- Lake Superior
* eri.csv -- Lake Erie
* ont.csv -- Lake Ontario

As instructed in the in-class activity notebook for today, you are 
only expected to complete one PART below. Do not worry if your group 
is not big enough to finish all parts below, but if you have extra 
"""


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


# PART 1
# Using the Michigan/Huron Dataset, plot the Water Level, the second 
# column, as a function of time years



# PART 2
# Using the Superior Dataset, plot the Water Level, the second column, 
# as a function of time years

# +
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
ds = pd.read_csv("sup.csv")

wtr_lvl = ds['lake levels']
year = ds['year']

plt.plot(wtr_lvl,year)
# -

# PART 3
# Using the Erie Dataset, plot the Water Level, the second column, 
# as a function of time years

plt.plot(erie.csv[2], erie.csv[1])
plt.show()



# PART 4
# Using the Ontario Dataset, plot the Water Level, the second column, 
# as a function of time years
These are Connor Sugrues changes 


# PART 5
# Using the Michigan/Huron and Superior Datasets, plot the 
# Michigan/Hurion Water Level vs Superior Water Level to see if there 
# is any correlation between the water levels.



# PART 6
# Using the Michigan/Hurion and Erie Datasets, plot the 
# Michigan/Huron Water Level vs Erie Water Level to see if there is 
# any correlation between the water levels.



# PART 7
# Using the Superior and Ontario Datasets, plot the Superior Water 
# Level vs Ontario Water Level to see if there is any correlation 
# between the water levels.


