import matplotlib.pyplot as plt
import numpy as np

all = []
y = []
for i in range(22):
    y.append(str(i+2000))
    with open("phone"+str(i+2000)+".txt", "r") as f:
        all.append(float(f.read()))
print(y)
print(len(y))
plt.plot(all)
plt.show()