import matplotlib.pyplot as plt
import numpy as np
import porespy as ps
import inspect
from PIL import Image
inspect.signature(ps.metrics.two_point_correlation)

im = Image.open('捕获.JPG')
data = ps.metrics.two_point_correlation(im)
fig, ax = plt.subplots(1, 1, figsize=[6, 6])
ax.plot(data.distance, data.probability, 'r.')
ax.set_xlabel("distance")
ax.set_ylabel("two point correlation function");
plt.show()
