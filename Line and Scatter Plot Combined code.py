import matplotlib.pyplot as plt

# Data
x = [1, 2, 3, 4]
y = [10, 20, 25, 30]

# Create the figure and axis
plt.figure(figsize=(8, 6))

# Add a line plot
plt.plot(x, y, label="Line Plot", color="blue", linestyle="--", marker="o")

# Add a scatter plot
plt.scatter(x, y, label="Scatter Plot", color="red", s=100)  # s sets the marker size

# Adding title and labels
plt.title("Line and Scatter Plot Combined", fontsize=14)
plt.xlabel("X-axis", fontsize=12)
plt.ylabel("Y-axis", fontsize=12)

# Add legend
plt.legend()

# Add grid
plt.grid(alpha=0.5)

# Show the plot
plt.show()
