import requests
import argparse
from enum import Enum
import display
from weather import resolve_weather_code
MIN_WIDTH = 34
MIN_CELL_WIDTH = MIN_WIDTH / 2 - 2





class WindDirection(Enum):
    NW = 1
    N = 2
    NE = 3
    E = 4
    SE = 5
    S = 6
    SW = 7
    W = 8
    

    def display_direction(self):
        match self:
            case WindDirection.N: return "N"
            case WindDirection.NE: return "NE"
            case WindDirection.E: return "E"
            case WindDirection.SE: return "SE"
            case WindDirection.S: return "S"
            case WindDirection.SW: return "SW"
            case WindDirection.W: return "W"
            case WindDirection.NW: return "NW"

    
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
    temperature = f"{weather['current_weather']['temperature']}{weather['hourly_units']['temperature_2m']}"
    apparent_temperature = f"Feels like {weather['hourly']['apparent_temperature'][current_hour]}{weather['hourly_units']['temperature_2m']}"

    humidity = f"Humidity: {weather['hourly']['relativehumidity_2m'][current_hour]}{weather['hourly_units']['relativehumidity_2m']}"
    dewpoint = f"Dew Point: {weather['hourly']['dewpoint_2m'][current_hour]}{weather['hourly_units']['dewpoint_2m']}"
    wind_direction = WindDirection.get_direction(weather['current_weather']['winddirection'])
    icon = wind_direction.get_icon()
    wind = f"{icon} {weather['current_weather']['windspeed']}{weather['hourly_units']['windspeed_10m']} {wind_direction.display_direction()}"
    pressure = f"☉ {weather['hourly']['surface_pressure'][current_hour]}{weather['hourly_units']['surface_pressure']}"
    sunrise = f"☉ {sunrise}"
    sunset = f"☉ {sunset}"
    wmo_code = resolve_weather_code(weather['current_weather']['weathercode'], night)

    # Dimensions
    title_width = len(location)
    title_padding = 2 * 2 # 2 spaces on each side
    longest_cell_width = len(humidity)
    width = title_width + title_padding if title_width > MIN_WIDTH else MIN_WIDTH + title_padding
    cell_width = longest_cell_width if longest_cell_width > MIN_CELL_WIDTH else MIN_CELL_WIDTH + 2
    dimensions = (width, cell_width)
    # Border Top
    print(f"{display.Edge.Top.fmt(width, display.BorderStyle.double)}")
    # Address / Title
    address = location[:width].center(width)
    print(f"{display.Border.L.fmt(display.BorderStyle.double)}{address}{display.Border.R.fmt(display.BorderStyle.double)}")
    
    # Separator
    print(f"{display.Separator.Double.fmt(width, display.BorderStyle.double)}")
    
    # Temperature & Weathercode
    temp_wc = f"  {wmo_code[1]} {temperature} {wmo_code[0]}"
    print(f"{display.Border.L.fmt(display.BorderStyle.double)}{temp_wc.ljust(width)}{display.Border.R.fmt(display.BorderStyle.double)}")
    
    # Apparent Temperature
    print(f"{display.Border.L.fmt(display.BorderStyle.double)}  {apparent_temperature.ljust(width-2)}{display.Border.R.fmt(display.BorderStyle.double)}")
    
    # Blank Line
    print(f"{display.Separator.Blank.fmt(width, display.BorderStyle.double)}")

    # Humidity & Dewpoint
    hum_dew = f"  {humidity}".ljust(int(cell_width))+f"{dewpoint}"
    print(f"{display.Border.L.fmt(display.BorderStyle.double)}{hum_dew.ljust(width)}{display.Border.R.fmt(display.BorderStyle.double)}")
    
    # Wind & Pressure
    wind_pres = f"  {wind}".ljust(int(cell_width))+f"{pressure}"
    print(f"{display.Border.L.fmt(display.BorderStyle.double)}{wind_pres.ljust(width)}{display.Border.R.fmt(display.BorderStyle.double)}")
    
    # Sunrise & Sunset
    sun = f"  {sunrise}".ljust(int(cell_width))+f"{sunset}"
    print(f"{display.Border.L.fmt(display.BorderStyle.double)}{sun.ljust(width)}{display.Border.R.fmt(display.BorderStyle.double)}")

    # Border Bottom
    print(f"{display.Edge.Bottom.fmt(width, display.BorderStyle.double)}")


def product(location, weather):
    current(location, weather)
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
