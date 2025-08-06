from rich.panel import Panel
from rich.text import Text
from infoFunctions import display_nmap_results
from infoFunctions import get_system_stats
from getWeather import get_weather

def get_nmap_panel():
    output_list = display_nmap_results()
    if not output_list:
        content = "No devices found."
    else:
        content = "\n".join(output_list)
    return Panel(Text(content), title="Network Scan", border_style="green")

def get_sysstats_panel():
    output_list = get_system_stats()
    if not output_list:
        content = "no stats available"
    else:
        content = "\n".join(output_list)
    return Panel(Text(content), title="System Stats", border_style="green")

weather_data = get_weather('chicago')

def get_weather_panel():
    temp = weather_data.get("temp", "n/a")
    humidity = weather_data.get("humidity", "n/a")
    wind = weather_data.get("windspeed", "n/a")
    gust = weather_data.get("gust", "n/a")
    rain = weather_data.get("precipitation", "n/a")

    text = Text()
    text.append(f"Temp: {temp} F\n")
    text.append(f"Hum: {humidity}\n")
    text.append(f"Wind: {wind} mph\n")
    text.append(f"Gust: {gust} mph\n")
    text.append(f"Precip: {rain}mm/h")

    return Panel(text, title="Weather", border_style="green")