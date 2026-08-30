import numpy as np
import matplotlib.pyplot as plt
import random
np.set_printoptions(legacy='1.25') # removes the np.float in output

# EDIT THESE VALUES TO YOUR LIKING -----------------------------------------------------------------
p2x, p2y = 50, 20
p0x, p0y = 35, 2
n = 30
# EDIT THESE VALUES TO YOUR LIKING -----------------------------------------------------------------



p2y_length = np.sqrt((p2x)**2 + (p2y)**2)
# going from P2/P0 to P0/P2 ...
# if P2 = (p, q)
# (P2 -> P0)n = (p - (n-1)x, q + nx)
# x = distance between points
d = p2y_length / n

p_list = []
q_list = []
d_list = []
dy_list = []
zero_list = []

# x values at a given distance x from P2 ...
m = p2y / p2x # assume P1 = 0, 0 - otherwise transform so that it equals 0, 0

def roots(m, p, q):

    a = m ** 2 + 1
    b = (-2 * p) - (2 * m * q)
    c = -(d ** 2 - p ** 2 - q ** 2)

    determinant = np.sqrt((b**2) - 4*a*c)
    x1 = (-b + determinant) / (2 * a)
    x2 = (-b - determinant) / (2 * a)
    y1 = m * x1
    y2 = m * x2
    if x1 > x2:
        return min(x1,x2), min(y1, y2)

# Turns on interactive plot !!
plt.ion()

for i in range(0,n+1,1):
    p = p2x
    q = p2y

    res = roots(m,p2x,p2y)

    m_2 = p0y / p0x

    p2x = res[0]
    p2y = res[1]

    p_list.append(p2x)
    q_list.append(p2y)
    zero_list.append(0)
    dist = (p0x / n * i)
    dist_y = dist * m_2
    dy_list.append(dist_y)
    d_list.append(dist)

    if len(zero_list) <= 1:
        pass
    elif len(zero_list) >= 2:
        plt.plot([p_list[i-1], d_list[i-1]],[q_list[i-1], dy_list[i-1]], color = 'r', alpha = 0.5)

    plt.pause(0.1)

plt.ioff()
plt.show()
