import matplotlib.pyplot as plt
import numpy as np
import os

# Create a simple plot
fig, ax = plt.subplots()
x = np.linspace(0, 10, 100)
y = np.sin(x)
ax.plot(x, y)
ax.set_title("Placeholder Chart")
ax.set_xlabel("X-axis")
ax.set_ylabel("Y-axis")

# Ensure the static directory exists
output_dir = 'core/static/core'
os.makedirs(output_dir, exist_ok=True)

# Save the plot
plt.savefig(os.path.join(output_dir, 'placeholder_chart.png'))

print("Placeholder chart saved.")
