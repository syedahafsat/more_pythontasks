# Step 1: Store daily temperatures in a list
daily_temperatures = [30.5, 32.0, 33.2, 29.8, 31.4, 34.0, 30.0]  # Example values for 7 days

# Step 2: Define functions to calculate stats
def calculate_average(temps):
    return sum(temps) / len(temps)

def calculate_maximum(temps):
    return max(temps)

def calculate_minimum(temps):
    return min(temps)

# Step 3: Display the results
print("📊 Weekly Temperature Statistics")
print("--------------------------------")
print(f"📅 Daily Temperatures: {daily_temperatures}")
print(f"🌡️ Average Temperature: {calculate_average(daily_temperatures):.2f}°C")
print(f"🔥 Maximum Temperature: {calculate_maximum(daily_temperatures):.2f}°C")
print(f"❄️ Minimum Temperature: {calculate_minimum(daily_temperatures):.2f}°C")