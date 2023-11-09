import pandas as pd
import matplotlib.pyplot as plt

# Putting the data
data = pd.read_csv("world-happiness-report.csv")

# Making the boxplot
plt.figure(figsize=(10, 6))
plt.boxplot(data["Life Ladder"], notch=True, patch_artist=True)
plt.xlabel("Year")
plt.ylabel("Life Ladder")
plt.title("Distribution of Life Ladder in the World Happiness Report")
plt.tight_layout()
plt.show()