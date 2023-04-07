import requests
import argparse

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
    temp = str(weather['current_weather']['temperature'])
    time = int(weather['current_weather']['time'][11:13])
    humidity = weather['hourly']['relativehumidity_2m'][time]
    apparent_temperature = weather['hourly']['apparent_temperature'][time]
    print(f"Feels like: {apparent_temperature}")
    print(f"Humidity: {humidity}")

if __name__ == "__main__":
    main()
