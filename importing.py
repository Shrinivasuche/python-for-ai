#import whole module
import math
math.sqrt(16)

#import specific items from a module
from math import sqrt, pi
sqrt(16)

#common built-in modules
# random module
import random
number = random.randint(1, 10)
print(number)
choice = random.choice(['apple', 'banana', 'cherry'])
print(choice)

# datetime module
import datetime
today = datetime.date.today()
print(today)

# os module
import os
current_directory = os.getcwd()
print(current_directory)

#import with alias
import pandas as np
array = np.array([1, 2, 3])
print(array)