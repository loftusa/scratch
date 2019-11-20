#%%
from matplotlib import pyplot as plt
import seaborn as sns; sns.set()

# basic plots
years = [1950, 1960, 1970, 1980, 1990, 2000, 2010]
gdp = [300.2, 543.3, 1075.9, 2862.5, 5979.6, 10289.7, 14958.3]
billions = list(range(0, 14, 2))
billions
len(years)
len(billions)

plt.plot(years, gdp, marker='o', color='green')
plt.title("Nominal GDP")
plt.xlabel("Years")
plt.ylabel("$ (Billions)")
#%%
# bar charts
movies = ["Annie Hall", "Ben-Hur", "Casablanca", "Gandhi", "West Side Story"]
num_oscars = [5, 11, 3, 8, 10]

plt.bar(range(len(movies)), num_oscars)
plt.xticks(range(len(movies)), movies, color='black')
plt.ylabel("# academy awards")