import sys

sys.path +=['..']

import readline
from das_oszi.das_oszi import DasOszi
import matplotlib.pyplot as plt
import time
import sys

#readline.parse_and_bind('tab: complete')
#readline.parse_and_bind('set editing-mode vi')
channel = int(sys.argv[1])
dso = DasOszi(  0x049f, 0x505a, debug=True )
if dso is None:
    exit(1)
# to run GUI event loop
plt.ion()
# here we are creating sub plots
fig = plt.figure()  # Create figure
axes = fig.add_subplot(111) # Add subplot (dont worry only one plot appears)


axes.set_autoscale_on(True) # enable autoscale
axes.autoscale_view(True,True,True)
l, = plt.plot([], [], 'r-') # Plot blank data
plt.xlabel('x')         # Set up axes
plt.title('')

while(True):
 if dso is None:
    break
 r=dso.ReadSampleData(int(channel))
 length = len(r)
 if False: ## Math Functions
  length = (624 if channel==3 else len(r))
 
 l.set_data(range(0,length),r[0:length])
 
 axes.relim() # Recalculate limits
 axes.autoscale_view(True,True,True) #Autoscale
 fig.canvas.draw()
 fig.canvas.flush_events()


###################################
#  plt.plot(r)
#  plt.grid()
#  plt.show()
#  time.sleep(10)
#  plt.close()