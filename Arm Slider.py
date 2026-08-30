import numpy as np
import matplotlib.pyplot as plt
from matplotlib import animation, colors, colormaps
from matplotlib.widgets import Slider, Button

np.set_printoptions(legacy='1.25') # removes the np.float in output
plt.rcParams["font.family"] = "serif"
plt.rcParams["font.serif"] = ["Times New Roman"]

class Arm:

    def __init__(self,arm_length, forearm_length,init_x = 0, init_y = 0, x = 0, y = 0, p=0,q=0):
        self.arm_length = arm_length
        self.forearm_length = forearm_length
        self.init_x = init_x
        self.init_y = init_y
        self.x = x
        self.y = y
        self.p = p
        self.q = q

    def move_arm(self,arm_theta, forearm_theta):
        # the arm itself
        arm_theta = arm_theta*np.pi/180
        forearm_theta = forearm_theta * np.pi / 180

        self.x = self.init_x + self.arm_length * np.cos(arm_theta)
        self.y = self.init_y + self.arm_length * np.sin(arm_theta)

        # the forearm
        self.p = self.x + self.forearm_length * np.cos(forearm_theta)
        self.q = self.y + self.forearm_length * np.sin(forearm_theta)


test = Arm(2,1)

a = test.move_arm(20,45)

x = [test.init_x, test.x, test.p]
y = [test.init_y, test.y, test.q]

plt.plot(x,y, marker='o')

plt.xlim(-3,3)
plt.ylim(-3,3)

plt.show()

# --------------------------------------

fig = plt.figure()
ax = fig.add_subplot(111)
fig.subplots_adjust(left=0.25, bottom=0.25)

animation = Arm(2,1)
animation_move = animation.move_arm(20,45)

x = [animation.init_x, animation.x, animation.p]
y = [animation.init_y, animation.y, animation.q]

plt.xlim(-4,4)
plt.ylim(-4,4)

line, = plt.plot(x,y, marker='o')

theta_slider_ax  = fig.add_axes([0.25, 0.15, 0.65, 0.03])
theta_forearm_ax = fig.add_axes([0.25, 0.10, 0.65, 0.03])
theta_slider = Slider(theta_slider_ax, 'Theta (Arm)', 0, 360.0, valinit=45)
theta_forearm_slider = Slider(theta_forearm_ax, 'Theta (Forearm)', 0, 360.0, valinit=45)

def update(val):
    animation.move_arm(theta_slider.val, theta_forearm_slider.val)
    x = [animation.init_x, animation.x, animation.p]
    y = [animation.init_y, animation.y, animation.q]
    line.set_data(x,y)

theta_slider.on_changed(update)
theta_forearm_slider.on_changed(update)

plt.show()
