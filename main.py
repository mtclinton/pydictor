import requests
import argparse

def get_direction(wd):
    pass

def current(location, weather):
    current_hour = weather['current_weather'['time'][11:13]
    sunrise_hour = weather['daily']['sunrise'][0][11:13]
    sunset_hour = weather['daily']['sunset'][0][11:13]
    sunrise = weather['daily']['sunrise'][0][11:16]
    sunset = weather['daily']['sunset'][0][11:16]
    night = current_hour < sunrise_hour or current_hour > sunset_hour
    
    # Display Items
    temperature = f"{weather['current_weather']['temperature']}°{weather['hourly_units']['temperature_2m']}"
    apparent_temperature = f"Feels like {weather['hourly']['apparent_temperature'][current_hour]}{weather['hourly_units']['temperature_2m']}"

    humidity = f"Humidity: {weather['hourly']['relativehumidity_2m'][current_hour]}{weather['hourly_units']['relativehumidity_2m']}"
    dewpoint = f"Dew Point: {weather['hourly']['dewpoint_2m'][current_hour]}{weather['hourly_units']['dewpoint_2m']}"
    wind_direction = get_direction(weather['current_weather']['winddirection'])
    let wind = format!(
        "{} {}{} {}",
        wind_direction.get_icon(),
        weather.current_weather.windspeed,
        weather.hourly_units.windspeed_10m,
        wind_direction
    );
    pressure = f" {weather['hourly']['surface_pressure'][current_hour]}{weather['hourly_units']['surface_pressure']}"
    sunrise = f" {sunrise}"
    sunset = f(" {sunset}"
    let wmo_code = WeatherCode::resolve(weather.current_weather.weathercode, night, &t.weather_code)?;

    # Dimensions
    title_width = len(location)
    title_padding = 2 * 2 # 2 spaces on each side
    longest_cell_width = len(humidity)

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
