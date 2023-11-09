import pandas as pd
import matplotlib.pyplot as plt

# Putting the data
data = pd.read_csv("world-happiness-report.csv")

# Calculating the Healthy life expectancy at birth
Healthy_life_expectancy_at_birth = data["Healthy life expectancy at birth"].sum()

# The percentage of each country's Life expectancy
data["Percentage"] = (data["Healthy life expectancy at birth"] / Healthy_life_expectancy_at_birth) * 100

# Choosing top 10 countries to know the percentage of Life Expectancy
top_10_countries = data.sort_values(by="Percentage", ascending=False).head(10)

# Making the chart
plt.figure(figsize=(10, 6))
plt.pie(top_10_countries["Percentage"], labels=top_10_countries["Country name"], autopct="%1.1f%%")
plt.title("Percentage of Healthy life expectancy at birth for the Top 10 Countries")
plt.tight_layout()
plt.show()

