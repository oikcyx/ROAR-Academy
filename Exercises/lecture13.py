#Exercise 1:
from datetime import datetime
import matplotlib.pyplot as plt
import os
import numpy as np
import time

# Initialization, define some constant
path = os.path.dirname(os.path.abspath(__file__))
filename = path + '/airplane.bmp'
background = plt.imread(filename)

second_hand_length = 200
second_hand_width = 2
minute_hand_length = 150
minute_hand_width = 6
hour_hand_length = 100
hour_hand_width = 10
gmt_hand_length = 200
gmt_hand_width = 8
center = np.array([256, 256])

def clock_hand_vector(angle, length):
    return np.array([length * np.sin(angle), -length * np.cos(angle)])

# draw an image background
fig, ax = plt.subplots()

while True:
    plt.imshow(background)

    # First retrieve the time
    now_time = datetime.now()
    second = now_time.second + now_time.microsecond/10**6
    minute = now_time.minute +  second/60
    hour = now_time.hour + minute/60
    if hour>12: hour = hour - 12

    gmt = time.gmtime()
    gmt_hour = gmt.tm_hour

    # Calculate end points of hour, minute, second
    gmt_vector = clock_hand_vector(gmt_hour/12*2*np.pi, gmt_hand_length)
    hour_vector = clock_hand_vector(hour/12*2*np.pi, hour_hand_length)
    minute_vector = clock_hand_vector(minute/60*2*np.pi, minute_hand_length)
    second_vector = clock_hand_vector(second/60*2*np.pi, second_hand_length)

    plt.arrow(center[0], center[1], hour_vector[0], hour_vector[1], head_length = 3, linewidth = hour_hand_width, color = 'black')
    plt.arrow(center[0], center[1], minute_vector[0], minute_vector[1], linewidth = minute_hand_width, color = 'black')
    plt.arrow(center[0], center[1], second_vector[0], second_vector[1], linewidth = second_hand_width, color = 'red')
    plt.arrow(center[0], center[1], gmt_vector[0], gmt_vector[1], linewidth = gmt_hand_width, color = 'yellow')
    plt.axis('off')
    plt.pause(0.1)
    plt.clf()

#Exercise 2:
import matplotlib.pyplot as plt

x = [1, 2, 3]
y = [2, 4, 1]

plt.plot(x,y)
plt.xlabel("x axis")
plt.ylabel("y axis")
plt.title("Sample Graph")
plt.xticks([1, 1.5 , 2, 2.5, 3])
plt.show()