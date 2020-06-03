import numpy as np
import matplotlib.pyplot as plt


# set period of grpah
start = 0
end = 2*np.pi
period = np.arange(start, end, 0.02)                    

# calculate sine and cosine
sin = np.sin(period)
cos = np.cos(period)     

#plot graph
plt.plot(period, sin, period, cos)     

#set axis
plt.axis([start, end, -1, 1])


plt.show()

