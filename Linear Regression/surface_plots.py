# %% [markdown]
# # Surface Plots | Visualization

# %%
import matplotlib.pyplot as plt
import numpy as np

# %%
# a = np.array([1, 2, 3])
# b = np.array([4, 5, 6, 7])

a = np.arange(-1, 1, 0.02)
b = a


a, b = np.meshgrid(a, b)
# a --> Repeated size(b) times along the first axis
# b --> Repeated size(a) times along the second axis
# print(a)
# print(b)

# %%
fig = plt.figure()
axes = fig.gca(projection='3d')
axes.plot_surface(a, b, a**2+b**2, cmap='rainbow')
plt.show()

# %%
fig = plt.figure()
axes = fig.gca(projection='3d')
axes.contour(a, b, a**2+b**2, cmap='rainbow')
plt.title("CONTOUR PLOT")
plt.show()

# %%



