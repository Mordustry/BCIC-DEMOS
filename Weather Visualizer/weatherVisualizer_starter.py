"""
WEATHER DATA VISUALIZER
A Python project that uses libraries to fetch and visualize weather data

Learning Goals:
- Use external libraries (requests and matplotlib)
- Make API calls to get real-time data
- Create data visualizations

Author: [Your Name]
Date: [Today's Date]
"""

# ============================================
# STEP 1: IMPORT LIBRARIES
# ============================================
import requests
import matplotlib.pyplot as plt


# ============================================
# STEP 2: CONFIGURATION
# ============================================
# TODO: Replace with your actual API key from OpenWeatherMap
API_KEY = "69895fd7b944e9d19889e17c44ced1de"

# Base URL for the weather API
BASE_URL = "http://api.openweathermap.org/data/2.5/weather"

# Cities we want to compare
cities = ["London", "Tokyo", "New York", "Sydney", "Dubai", "Paris", "Bangkok", "Moscow", "Rio de Janeiro", "Cape Town"]


# ============================================
# STEP 3: FUNCTION TO GET TEMPERATURE
# ============================================
def get_temperature(city_name):
    """
    Fetch current temperature for a given city.
    
    Parameters:
        city_name (str): Name of the city to get weather for
    
    Returns:
        float: Temperature in Celsius, or None if there's an error
    """
    # Create parameters for the API request
    params = {
        'q': city_name,           # City name
        'appid': API_KEY,         # Your API key
        'units': 'metric'         # Get temperature in Celsius
    }
    
    try:
        # TODO: Make the API request using requests.get()
        response = requests.get(BASE_URL, params=params)
        
        # TODO: Convert the response to JSON (a Python dictionary)
        # Hint: use .json() method
        data = response.json()
        
        # TODO: Extract the temperature from the data
        # Hint: Look at data['main']['temp']
        temperature = data['main']['temp']
        
        return temperature
    
    except Exception as e:
        print(f"❌ Error fetching data for {city_name}: {e}")
        return None


# ============================================
# STEP 4: COLLECT DATA FOR ALL CITIES
# ============================================
# TODO: Create two empty lists
# One for city names, one for temperatures
city_names = []
temperatures = []

print("🌍 Fetching weather data...\n")

# TODO: Loop through each city in the cities list
# For each city:
#   1. Call get_temperature(city)
#   2. If temp is not None, add city and temp to your lists
#   3. Print a success message

# Your loop here:
for city in cities:
    temp = get_temperature(city)
    if temp is not None:
        city_names.append(city)
        temperatures.append(temp)
        print(f"✅ {city}: {temp:.1f}°C")
    else:
        print(f"❌ Failed to get temperature for {city}")



# ============================================
# STEP 5: CREATE THE VISUALIZATION
# ============================================
#sort temperatures list from least to greatest and sort city names list in the same order
temperatures, city_names = zip(*sorted(zip(temperatures, city_names)))

# TODO: Create a figure with size 10x6
plt.figure(figsize=(10, 6))


# TODO: Create a bar chart
plt.bar(city_names, temperatures, color='gold', edgecolor='navy')


# TODO: Add labels for x-axis and y-axis
plt.xlabel('City', fontsize=12)
plt.ylabel('Temperature (°C)', fontsize=12)


# TODO: Add a title to the chart
plt.title('The Current Temperatures of my World', fontsize=16)


# TODO: Add temperature values on top of each bar
# Use a for loop with enumerate(temperatures)

for i, temp in enumerate(temperatures):
    plt.text(i, temp + 0.5, f'{temp:.1f}°C', ha='center')


# TODO: Make the chart look nice with a grid
plt.grid(axis='y', alpha=0.3)


# TODO: Use tight_layout to prevent labels from being cut off
plt.tight_layout()


# TODO: Display the chart
plt.show()


# ============================================
# EXTENSION CHALLENGES (Optional)
# ============================================
"""
Once you have the basic chart working, try these challenges:

EASY:
1. Add 3 more cities of your choice to the cities list
2. Change the bar color to 'coral', 'lightgreen', or 'gold'
3. Change the chart title to something creative

MEDIUM:
4. Show temperatures in Fahrenheit instead (change 'metric' to 'imperial')
5. Sort the cities by temperature (coldest to hottest)
6. Add a subtitle showing the current date/time

HARD:
7. Calculate and display the average temperature as a horizontal line
   Hint: avg = sum(temperatures) / len(temperatures)
         plt.axhline(avg, color='red', linestyle='--', label=f'Avg: {avg:.1f}°C')
         plt.legend()

8. Create a second visualization showing humidity instead
   Hint: Humidity is in data['main']['humidity']

9. Add error bars or different colors for temperatures above/below freezing

10. Save the chart as an image file
    Hint: plt.savefig('weather_chart.png')
"""