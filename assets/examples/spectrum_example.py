import numpy as np
from matplotlib import cm
from mpl_toolkits.mplot3d import Axes3D  
import matplotlib.pyplot as plt
import csv

row = []
array = []
column_axis = []
index = 0

# Make axis for the spectrums' frequencies
n_bins = 255
frequency = 44100/2
row_axis = np.arange(0,n_bins,1)*frequency/n_bins

with open('screenlog.0', 'r') as file:
	for line in file:
		if '-' in line:
			column_axis.append(index)
			array.append(row)
			index += 1
			row = []
		else:
			try:
				row.append(int(line.strip('\n')))
			except:
				pass

# csv output
with open("out.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerows(array)

# plot
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
X = row_axis
Y = np.array(column_axis).reshape(index, 1)
Z = np.array(array, ndmin = 2)

# Add some colors
colors = cm.jet(Z/np.amax(Z))
ax.plot_surface(X, Y, Z, facecolors = colors, linewidth = 0)

ax.set_xlabel('Frequency (Hz)')
ax.set_ylabel('Spectrum # (-)')
ax.set_zlabel('SPL (-)')

# save the plot
plt.savefig('spectrum.png')