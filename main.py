import requests
import argparse
from enum import Enum

WeatherCodeLocales = {
    "clear_sky": "Clear Sky",
    "mostly_clear": "Mostly Clear",
    "partly_cloudy": "Partly Cloudy",
    "overcast": "Overcast",
    "fog": "Fog",
    "depositing_rime_fog": "Depositing Rime Fog",
    "light_drizzle": "Light Drizzle",
    "moderate_drizzle": "Moderate Drizzle",
    "dense_drizzle": "Dense Drizzle",
    "light_freezing_drizzle": "Light Freezing Drizzle",
    "dense_freezing_drizzle": "Dense Freezing Drizzle",
    "slight_rain": "Slight Rain",
    "moderate_rain": "Moderate Rain",
    "heavy_rain": "Heavy Rain",
    "light_freezing_rain": "Light Freezing Rain",
    "heavy_freezing_rain": "Heavy Freezing Rain",
    "slight_snow_fall": "Slight Snow Fall",
    "moderate_snow_fall": "Moderate Snow Fall",
    "heavy_snow_fall": "Heavy Snow Fall",
    "snow_grains": "Snow Grains",
    "slight_rain_showers": "Slight Rain Showers",
    "moderate_rain_showers": "Moderate Rain Showers",
    "violent_rain_showers": "Violent Rain Showers",
    "slight_snow_showers": "Slight Snow Showers",
    "heavy_snow_showers": "Heavy Snow Showers",
    "thunderstorm": "Thunderstorm",
    "thunderstorm_slight_hail": "Thunderstorm, Slight Hail",
    "thunderstorm_heavy_hail": "Thunderstorm, Heavy Hail"
}



class WindDirection(Enum):
    NW = 1
    N = 2
    NE = 3
    E = 4
    SE = 5
    S = 6
    SW = 7
    W = 8
    
    @staticmethod
    def get_direction(wd):
        wd = wd % 360.0
        if 337.5<=wd<=360.0 or 0.0<=wd<22.5: return WindDirection.N
        elif 22.5<=wd<67.5: return WindDirection.NE
        elif 67.5<=wd<112.5: return WindDirection.E
        elif 112.5<=wd<157.5: return WindDirection.SE
        elif 157.5<=wd<202.5: return WindDirection.S
        elif 202.5<=wd<247.5: return WindDirection.SW
        elif 247.5<=wd<292.5: return WindDirection.W
        elif 292.5<=wd<337.5: return WindDirection.NW
        else: return "Wind from another dimension"

    def get_icon(self):
        match self:
            case WindDirection.N: return '↑'
            case WindDirection.NE: return '↗'
            case WindDirection.E: return '→'
            case WindDirection.SE: return '↘'
            case WindDirection.S: return '↓'
            case WindDirection.SW: return '↙'
            case WindDirection.W: return '←'
            case WindDirection.NW: return '↖'


def current(location, weather):
    current_hour = int(weather['current_weather']['time'][11:13])	
    sunrise_hour = int(weather['daily']['sunrise'][0][11:13])
    sunset_hour = int(weather['daily']['sunset'][0][11:13])
    sunrise = weather['daily']['sunrise'][0][11:16]
    sunset = weather['daily']['sunset'][0][11:16]
    night = current_hour < sunrise_hour or current_hour > sunset_hour
    
    # Display Items
    temperature = f"{weather['current_weather']['temperature']}°{weather['hourly_units']['temperature_2m']}"
    apparent_temperature = f"Feels like {weather['hourly']['apparent_temperature'][current_hour]}{weather['hourly_units']['temperature_2m']}"

    humidity = f"Humidity: {weather['hourly']['relativehumidity_2m'][current_hour]}{weather['hourly_units']['relativehumidity_2m']}"
    dewpoint = f"Dew Point: {weather['hourly']['dewpoint_2m'][current_hour]}{weather['hourly_units']['dewpoint_2m']}"
    wind_direction = WindDirection.get_direction(weather['current_weather']['winddirection'])
    icon = wind_direction.get_icon()
    wind = f"{icon} {weather['current_weather']['windspeed']}{weather['hourly_units']['windspeed_10m']} {wind_direction}"
    pressure = f" {weather['hourly']['surface_pressure'][current_hour]}{weather['hourly_units']['surface_pressure']}"
    sunrise = f"🌅 {sunrise}"
    sunset = f"🌇 {sunset}"
    #wmo_code = resolve_weather_code(weather['current_weather']['weathercode'], night)

    # Dimensions
    title_width = len(location)
    title_padding = 2 * 2 # 2 spaces on each side
    longest_cell_width = len(humidity)
    print(wind)
    print(sunrise)
    print(sunset)
    #print(wmo_code)

def product(location, weather):
    current(location, weather)
    temp = str(weather['current_weather']['temperature'])
    time = int(weather['current_weather']['time'][11:13])
    humidity = weather['hourly']['relativehumidity_2m'][time]
    apparent_temperature = weather['hourly']['apparent_temperature'][time]
    print(f"Feels like: {apparent_temperature}")
    print(f"Humidity: {humidity}")
    CB = '\x1b[1;34;40m'
    CE = '\x1b[0m'
    print(f"{CB}Weather data by Open-Meteo.com{CE}")

def main():
    parser = argparse.ArgumentParser(
                    prog='PyDictor',
                    description='Show the weather in the terminal')
    parser.add_argument('address', help='Address to check the weather')
    args = parser.parse_args()
    l = "en-US"
    x = requests.get(f"https://nominatim.openstreetmap.org/search?q={args.address}&accept-language={l}&limit=1&format=jsonv2")
    location = x.json()[0]
    print(location['display_name'])
    lat = location['lat']
    lon = location['lon']
    temperature_unit = "fahrenheit"
    windspeed_unit = "mph"
    precipitation_unit = "inch"
    url = f"https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={lon}&current_weather=true&temperature_unit={temperature_unit}&windspeed_unit={windspeed_unit}&precipitation_unit={precipitation_unit}&hourly=temperature_2m,relativehumidity_2m,apparent_temperature,surface_pressure,dewpoint_2m,windspeed_10m,weathercode,precipitation,precipitation_probability&daily=weathercode,sunrise,sunset,temperature_2m_max,temperature_2m_min,precipitation_probability_max,apparent_temperature_max,apparent_temperature_min&timezone=auto"

    weather = requests.get(url).json()
    product(location['display_name'], weather)

if __name__ == "__main__":
    main()
