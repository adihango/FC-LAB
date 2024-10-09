import numpy as np
import pandas as pd

# Sample temperature data for 5 cities over 7 days
data = {
    'Day': ['Day1', 'Day2', 'Day3', 'Day4', 'Day5', 'Day6', 'Day7'],
    'Pune': [32, 34, 33, 36, 35, 34, 33],
    'Mumbai': [30, 31, 29, 35, 34, 32, 31],
    'Kochi': [34, 35, 36, 37, 38, 36, 35],
    'Nagpur': [33, 34, 32, 36, 37, 36, 35]
}

# Creating a DataFrame
df = pd.DataFrame(data)

# 1. Calculating the average temperature per city
avg_temp_per_city = df[['Pune', 'Mumbai', 'Kochi', 'Nagpur']].mean()
print("Average Temperature per City:")
print(avg_temp_per_city)
print()

# 2. Finding the hottest day overall and in each city
hottest_day_overall = df[['Pune', 'Mumbai', 'Kochi', 'Nagpur']].max().max()
hottest_day_citywise = df[['Pune', 'Mumbai', 'Kochi', 'Nagpur']].max()
hottest_days = df.set_index('Day').idxmax()

print(f"Hottest day overall: {hottest_day_overall}°C")
print("Hottest day in each city:")
print(hottest_day_citywise)
print()

# 3. Identifying the city with the highest average temperature
city_with_highest_avg_temp = avg_temp_per_city.idxmax()
print(f"City with highest average temperature: {city_with_highest_avg_temp}")
print()

# 4. Identifying the days where the temperature in any city exceeded 35°C
days_above_35 = df[df[['Pune', 'Mumbai', 'Kochi', 'Nagpur']].gt(35).any(axis=1)]
print("Days where temperature exceeded 35°C in any city:")
print(days_above_35)
