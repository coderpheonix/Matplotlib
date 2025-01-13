import matplotlib.pyplot as plt

# Data for the bar chart
x = ["Java", "Python", "C", "C++", "JavaScript"]
y = [30, 90, 20, 60, 80]

# Colors for the bars
colors = ["gold", "skyblue", "red", "magenta", "purple"]

# Creating the bar chart
plt.figure(figsize=(10, 6))  # Adjust the figure size
bars = plt.bar(x, y, width=0.5, color=colors, edgecolor="black", linewidth=1.2)

# Labels and title
plt.xlabel("Programming Language", fontsize=16, labelpad=10)
plt.ylabel("Priority", fontsize=16, labelpad=10)
plt.title("Programming Language Priority Comparison", fontsize=18, fontweight="bold", pad=15)

# Adding grid lines
plt.grid(axis="y", linestyle="--", alpha=0.7)

# Adding annotations for each bar
for bar in bars:
    height = bar.get_height()
    plt.text(
        bar.get_x() + bar.get_width() / 2,  # x-coordinate
        height + 2,                        # y-coordinate (just above the bar)
        f"{height}",                       # Text to display
        ha="center",                       # Horizontal alignment
        va="bottom",                       # Vertical alignment
        fontsize=12, color="black", fontweight="bold"
    )

# Adding a legend
plt.legend(
    ["Priority Scores"], loc="upper left", fontsize=12, frameon=False
)

# Customizing tick marks
plt.xticks(fontsize=12, rotation=30)
plt.yticks(fontsize=12)

# Display the chart
plt.tight_layout()  # Adjust layout to prevent overlap
plt.show()
import matplotlib.pyplot as plt

# Data for the bar chart
x = ["Java", "Python", "C", "C++", "JavaScript"]
y = [30, 90, 20, 60, 80]

# Colors for the bars
colors = ["gold", "skyblue", "red", "magenta", "purple"]

# Creating the bar chart
plt.figure(figsize=(10, 6))  # Adjust the figure size
bars = plt.bar(x, y, width=0.5, color=colors, edgecolor="black", linewidth=1.2)

# Labels and title
plt.xlabel("Programming Language", fontsize=16, labelpad=10)
plt.ylabel("Priority", fontsize=16, labelpad=10)
plt.title("Programming Language Priority Comparison", fontsize=18, fontweight="bold", pad=15)

# Adding grid lines
plt.grid(axis="y", linestyle="--", alpha=0.7)

# Adding annotations for each bar
for bar in bars:
    height = bar.get_height()
    plt.text(
        bar.get_x() + bar.get_width() / 2,  # x-coordinate
        height + 2,                        # y-coordinate (just above the bar)
        f"{height}",                       # Text to display
        ha="center",                       # Horizontal alignment
        va="bottom",                       # Vertical alignment
        fontsize=12, color="black", fontweight="bold"
    )

# Adding a legend
plt.legend(
    ["Priority Scores"], loc="upper left", fontsize=12, frameon=False
)

# Customizing tick marks
plt.xticks(fontsize=12, rotation=30)
plt.yticks(fontsize=12)

# Display the chart
plt.tight_layout()  # Adjust layout to prevent overlap
plt.show()
