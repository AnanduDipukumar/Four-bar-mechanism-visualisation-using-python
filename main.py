import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation,writers
import numpy as np


def plot_initialise():
    plt.xlim(-10, 14)
    plt.ylim(-5, 8)
    plt.title("\u0332".join('4 bar Mechanism ')+'\n\n                                                 -simulation by Anandu Dipukumar',color='cyan',fontsize='20')
    #plt.suptitle('4 bar Mechanism\n-simulation by Anandu Dipukumar',color='cyan')
    ax = plt.gca()
    ax.set_aspect('equal')
    ax.set_facecolor('black')#(.8, .9, 1))


class bar():

    def __init__(self, pos, len, angle='a', color='red'):
        self.color = color
        if angle != 'a':
            self.length = len
            self.coordinates = [pos, [pos[0] + len * np.cos(angle), pos[1] + len * np.sin(angle)]]
        else:
            self.length = (pos[0] - len[0]) ** 2 + (pos[1] - len[1]) ** 2
            self.coordinates = [pos, len]

    def plot(self):
        plt.plot([self.coordinates[0][0], self.coordinates[1][0]], [self.coordinates[0][1], self.coordinates[1][1]],
                 color=self.color, linewidth=5)


theeta = np.linspace(0, 4 * np.pi, 1000)
l1 = 2
l2 = 4
p = 6
q = 7

xt = []
yt = []

xx = []
yy = []

plt.figure(facecolor='brown',figsize=(16,9),dpi=120)
def anim(k):
    i=theeta[k]
    plt.clf()
    plot_initialise()
    bar1 = bar([0, 0], l1, i)
    stationary_bar = bar([0, 0], l2, 0)

    a = bar1.coordinates[1][0]
    b = bar1.coordinates[1][1]
    c = stationary_bar.coordinates[1][0]
    d = stationary_bar.coordinates[1][1]

    # x2=(a**3 - a**2*c + a*b**2 - 2*a*b*d - a*c**2 + a*d**2 - a*p**2 + a*q**2 + b**2*c - 2*b*c*d + c**3 + c*d**2 + c*p**2 - c*q**2 + (((-a**2 + 2*a*c - b**2 + 2*b*d - c**2 - d**2 + p**2 + 2*p*q + q**2)*(a**2 - 2*a*c + b**2 - 2*b*d + c**2 + d**2 - p**2 + 2*p*q - q**2))**0.5)*(-b + d))/(2*(a**2 - 2*a*c + b**2 - 2*b*d + c**2 + d**2))

    x2 = (a ** 3 - a ** 2 * c + a * b ** 2 - 2 * a * b * d - a * c ** 2 + a * d ** 2 - a * p ** 2 + a * q ** 2 + b ** 2
          * c - 2 * b * c * d + c ** 3 + c * d ** 2 + c * p ** 2 - c * q ** 2
          + (((-a ** 2 + 2 * a * c - b ** 2 + 2 * b * d - c ** 2 - d ** 2 + p ** 2 + 2 * p * q + q ** 2)
              * (a ** 2 - 2 * a * c + b ** 2 - 2 * b * d + c ** 2 + d ** 2 - p ** 2 + 2 * p * q - q ** 2)) ** 0.5)
          * (b - d)) / (2 * (a ** 2 - 2 * a * c + b ** 2 - 2 * b * d + c ** 2 + d ** 2))

    y2 = (b ** 2 - d ** 2 - p ** 2 + q ** 2 + (a - x2) ** 2 - (c - x2) ** 2) / (2 * (b - d))

    bar2 = bar(bar1.coordinates[1], [x2, y2])

    bar3 = bar(stationary_bar.coordinates[1], [x2, y2])

    slp = np.arctan(
        (bar2.coordinates[1][1] - bar2.coordinates[0][1]) / (bar2.coordinates[1][0] - bar2.coordinates[0][0]))

    slope = np.arctan(np.pi / 6) + slp

    if slp<0:
        slope+=np.pi

    pen = bar(bar2.coordinates[0], 3, slope)
    pen2 = bar(bar1.coordinates[1], -3, slope)

    xt.append(pen.coordinates[1][0])
    yt.append(pen.coordinates[1][1])

    xx.append(pen2.coordinates[1][0])
    yy.append(pen2.coordinates[1][1])

    bar2.color = 'green'
    stationary_bar.color = 'blue'
    bar3.color = 'orange'
    pen.color = 'magenta'
    pen2.color = 'magenta'

    pen.plot()
    pen2.plot()
    plt.plot(xt, yt, 'yellow')
    plt.plot(xx, yy, 'yellow')
    bar1.plot()
    stationary_bar.plot()
    bar2.plot()
    bar3.plot()

animation = FuncAnimation(plt.gcf(),anim,frames=1000,interval=40)

#To save this animation as mp4
"""
Writer=writers['ffmpeg']
writer=Writer(fps=12.5,metadata={'artist':'Me'},bitrate=5400)#bitrate=36*dpi
animation.save('Four bar mechanism01.mp4',writer,dpi=120)#dpi=resolution/frameheight
"""
plt.show()
"""
for i in theeta:
    plt.clf()
    plot_initialise()
    bar1 = bar([0, 0], l1, i)
    stationary_bar = bar([0, 0], l2, 0)

    a = bar1.coordinates[1][0]
    b = bar1.coordinates[1][1]
    c = stationary_bar.coordinates[1][0]
    d = stationary_bar.coordinates[1][1]

    # x2=(a**3 - a**2*c + a*b**2 - 2*a*b*d - a*c**2 + a*d**2 - a*p**2 + a*q**2 + b**2*c - 2*b*c*d + c**3 + c*d**2 + c*p**2 - c*q**2 + (((-a**2 + 2*a*c - b**2 + 2*b*d - c**2 - d**2 + p**2 + 2*p*q + q**2)*(a**2 - 2*a*c + b**2 - 2*b*d + c**2 + d**2 - p**2 + 2*p*q - q**2))**0.5)*(-b + d))/(2*(a**2 - 2*a*c + b**2 - 2*b*d + c**2 + d**2))

    x2 = (a ** 3 - a ** 2 * c + a * b ** 2 - 2 * a * b * d - a * c ** 2 + a * d ** 2 - a * p ** 2 + a * q ** 2 + b ** 2
          * c - 2 * b * c * d + c ** 3 + c * d ** 2 + c * p ** 2 - c * q ** 2
          + (((-a ** 2 + 2 * a * c - b ** 2 + 2 * b * d - c ** 2 - d ** 2 + p ** 2 + 2 * p * q + q ** 2)
          * (a ** 2 - 2 * a * c + b ** 2 - 2 * b * d + c ** 2 + d ** 2 - p ** 2 + 2 * p * q - q ** 2)) ** 0.5)
          * (b - d)) / (2 * (a ** 2 - 2 * a * c + b ** 2 - 2 * b * d + c ** 2 + d ** 2))

    y2 = (b ** 2 - d ** 2 - p ** 2 + q ** 2 + (a - x2) ** 2 - (c - x2) ** 2) / (2 * (b - d))

    bar2 = bar(bar1.coordinates[1], [x2, y2])

    bar3 = bar(stationary_bar.coordinates[1], [x2, y2])

    slp = np.arctan(
        (bar2.coordinates[1][1] - bar2.coordinates[0][1]) / (bar2.coordinates[1][0] - bar2.coordinates[0][0]))

    slope = np.arctan(np.pi / 6) + slp

    pen = bar(bar2.coordinates[0], 3, slope)
    pen2 = bar(bar1.coordinates[1], -3, slope)

    xt.append(pen.coordinates[1][0])
    yt.append(pen.coordinates[1][1])

    xx.append(pen2.coordinates[1][0])
    yy.append(pen2.coordinates[1][1])

    bar2.color='green'
    stationary_bar.color='blue'
    bar3.color='orange'
    pen.color='magenta'
    pen2.color = 'magenta'

    pen.plot()
    pen2.plot()
    plt.plot(xt, yt, 'yellow')
    plt.plot(xx, yy, 'yellow')
    bar1.plot()
    stationary_bar.plot()
    bar2.plot()
    bar3.plot()
    plt.pause(0.001)

# plt.plot(xt,yt,'blue')
plt.show()

"""