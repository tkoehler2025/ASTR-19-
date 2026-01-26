
import numpy as np
from tabulate import tabulate


x = np.linspace(0, 2*(np.pi) , 1000)
y = np.sin(x)

table_data = [(a, b) for a, b in zip(x, y)]
headers = ["x", "y"]
table = tabulate(table_data, tablefmt="grid", headers=headers, floatfmt=".4f")

print(table)