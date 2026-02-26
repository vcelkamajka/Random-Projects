import pandas as pd
import math
import numpy as np
import random
import matplotlib.pyplot as plt
from itertools import combinations
from itertools import permutations
from matplotlib.patches import Rectangle, Polygon
dash = '------------------------------------------------------------------------------'
np.set_printoptions(legacy='1.25') # removes the np.float in output

def area(x,y):
    return x * y

s = input('What s value do you want?: ')
list = np.arange(1,100)
print('S is equal to:',s)

check_list = []
coord_list = []

perm = permutations(list, 2)
for i in perm:
    a = math.prod(i)
    if a == int(s):
        print('X, Y is equal to:',i)
        check_list.append(a)
        coord_list.append(i)
if len(check_list) == 0:
    print('No solutions found!')

#print(coord_list)
dim = []
x_plot = []
y_plot = []
colours = ['skyblue', 'lavender', 'plum']


fig, ax = plt.subplots(figsize=(8,8))
for i in range(len(check_list)):
    x, y = (coord_list[i])
    #print(x, y)
    dim.append(x)
    x_plot.append(x)
    y_plot.append(y)

    ax.set_xlim(0,max(dim))
    ax.set_ylim(0,max(dim))
    rect = Rectangle((0,0), width = x, height = y, alpha = 0.35, facecolor = random.choice(colours))
    ax.add_patch(rect)
    #ax.scatter(x, y, s=20, color='skyblue')
ax.plot(x_plot, y_plot, color='skyblue')


plt.show()

# TO DO - run function to generate all combinations and find index of the max value ! and then plot it :D
