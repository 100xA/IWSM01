import matplotlib.pyplot as plt
import numpy as np

# Data points for each service (Criticality, SLA Violations)
services = {
    'CRM Support': (1, 2),
    'Data Analytics': (3, 5),
    'DevOps': (1, 0),
    'Cloud Hosting': (2, 3),
    'Cybersecurity': (5, 6)
}

# Create figure with two subplots side by side
fig = plt.figure(figsize=(15, 6))

# First subplot (scatter plot)
plt.subplot(1, 2, 1)
x = [coord[0] for coord in services.values()]
y = [coord[1] for coord in services.values()]
labels = list(services.keys())

plt.scatter(x, y, marker='x', color='blue', s=100)

# Add labels for each point
for i, label in enumerate(labels):
    plt.annotate(label, (x[i], y[i]), xytext=(5, 5), textcoords='offset points')

# Customize the plot
plt.grid(True, linestyle='--', alpha=0.7)
plt.xlabel('SLA Verletzungen')
plt.ylabel('Kritikalität des Business IT-Services')
plt.xlim(0, 5)
plt.ylim(0, 6)

# Second subplot (heatmap)
plt.subplot(1, 2, 2)
# Define the data
data = np.array([
    [1, 1, 1, 1],  # Business-vital
    [3, 2, 2, 1],  # Business-kritisch
    [4, 3, 3, 2],  # Business-wichtig
    [5, 4, 3, 3],  # Keinen unmittelbaren Einfluss
])

# Create labels for axes
y_labels = ['Business-\nvital', 'Business-\nkritisch', 'Business-\nwichtig', 'Keinen unmittelbaren\nEinfluss auf Business']
x_labels = ['0', '1-2', '3-5', '>5']

# Create heatmap using imshow
im = plt.imshow(data, cmap='Greens_r')  # Reversed green colormap

# Add text annotations
for i in range(len(y_labels)):
    for j in range(len(x_labels)):
        text = plt.text(j, i, str(data[i, j]),
                       ha='center', va='center')

# Customize axes
plt.xticks(range(len(x_labels)), x_labels)
plt.yticks(range(len(y_labels)), y_labels)

plt.xlabel('Anzahl SLA-Verletzungen')
plt.ylabel('Kritikalität des Business IT-Services')

# Add colorbar
plt.colorbar(im, label='Priorität')

plt.tight_layout()
plt.show()
