import pandas as pd
import matplotlib.pyplot as plt

# putting the data
data = pd.read_csv("world-happiness-report.csv")

# Choosing the Ten Countries
top_10_countries = data.sort_values(by="Freedom to make life choices", ascending=False).head(10)

# CMaking the Line-Plot
plt.figure(figsize=(10, 6))
plt.plot(top_10_countries["Country name"], top_10_countries["Freedom to make life choices"])
plt.xlabel("Country name")
plt.ylabel("Freedom to make life choices")
plt.title("Freedom to make life choices of the Top 10 Countries")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()