"""Weather App – fetches a 3-day humidity forecast and plots it as a bar chart."""

import matplotlib.pyplot as plt
from pyowm import OWM
from datetime import datetime
import pytz

API_KEY = "YOUR_API_KEY"

owm = OWM(API_KEY)
mgr = owm.weather_manager()

def init_plot():
    """Initialize the plot with title and y-label."""
    plt.figure(figsize=(6, 4))
    plt.title("Humidity Forecast")
    plt.ylabel("Humidity (%)")
    plt.xlabel("Day")

def plot_humidity(days, humidities):
    """Create the bar chart for humidity."""
    bars = plt.bar(days, humidities, color='steelblue')
    write_humidity_on_bar_chart(bars, humidities)
    plt.ylim(0, 110)  # extra headroom so the 100 % label fits
    plt.show()

def write_humidity_on_bar_chart(bars, humidities):
    """Write the humidity % on top of each bar."""
    for bar, humidity in zip(bars, humidities):
        plt.text(bar.get_x() + bar.get_width()/2, bar.get_height() - 10,
                 f"{humidity}%", ha='center', color='white', fontsize=12)

def get_three_day_humidity(city_name):
    """Retrieve and return the 3-day average humidity forecast for a city."""
    forecast = mgr.forecast_at_place(city_name, '3h')
    humidity_data = {}
    for weather in forecast.forecast:
        date = weather.reference_time('date').date()
        if date not in humidity_data:
            humidity_data[date] = []
        humidity_data[date].append(weather.humidity)
        if len(humidity_data) == 3 and len(humidity_data[date]) > 8:
            break
    
    days = []
    avg_humidities = []
    for i, (date, hums) in enumerate(humidity_data.items()):
        days.append(date.strftime("%m/%d"))
        avg_humidities.append(int(sum(hums)/len(hums)))
    
    return days, avg_humidities

city = input("Enter city name: ")
days, humidities = get_three_day_humidity(city)
init_plot()
plot_humidity(days, humidities)
