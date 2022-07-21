
from matplotlib import projections


import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("Stores.csv")

def showScatterplot(df, x, y):
    fig, ax = plt.subplots()
    ax.scatter(df[x], df[y], alpha=0.1)
    ax.set_xlabel(x)
    ax.set_ylabel(y)
    plt.show()

def show3DScatterplot(df, x, y, z):
    fig = plt.figure()
    ax = fig.add_subplot(111, projection = "3d")
    ax.scatter(df[x], df[y], df[z])
    ax.set_xlabel(x)
    ax.set_ylabel(y)
    ax.set_zlabel(z)
    plt.show()
    fig.savefig("3d.png")

# showScatterplot(df, "Items_Available", "Store_Area")
show3DScatterplot(df, "Items_Available", "Store_Area", "Store_Sales")
