import matplotlib.pyplot as plt
import pandas as pd

# Load the data from the CSV file into a Pandas DataFrame
df = pd.read_csv("weather_data.csv")

# Extract the time and temperature columns from the DataFrame
time = df["time"]
temperature = df["temperature"]

# Plot the temperature versus time
plt.plot(time, temperature)

# Add axis labels and a title
plt.xlabel("Time")
plt.ylabel("Temperature (°C)")
plt.title("Temperature versus Time")

# Show the plot
plt.show()
