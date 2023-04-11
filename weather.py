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

def resolve_weather_code(code, is_night):
    match code:
        case 0: return (WeatherCodeLocales['clear_sky'], '☼' if is_night else '☼')
        case 1: return (WeatherCodeLocales['mostly_clear'], '☼' if is_night else '☼')
        case 2: return (WeatherCodeLocales['partly_cloudy'], '☼' if is_night else '☼')
        case 3: return (WeatherCodeLocales['overcast'], '☼')
        case 45: return (WeatherCodeLocales['fog'], '☼' if is_night else '☼')
        case 48: return (WeatherCodeLocales['depositing_rime_fog'], '☼'),
        case 51: return (WeatherCodeLocales['light_drizzle'], '☼' if is_night else '☼')
        case 53: return (WeatherCodeLocales['moderate_drizzle'], '☼' if is_night else '☼')
        case 55: return (WeatherCodeLocales['dense_drizzle'], '☼' if is_night else '☼')
        case 56: return (WeatherCodeLocales['light_freezing_drizzle'], '☼' if is_night else '☼')
        case 57: return (WeatherCodeLocales['dense_freezing_drizzle'], '☼' if is_night else 'ﭽ')
        case 61: return (WeatherCodeLocales['slight_rain'], '☼' if is_night else '☼')
        case 63: return (WeatherCodeLocales['moderate_rain'], '☼' if is_night else '☼')
        case 65: return (WeatherCodeLocales['heavy_rain'], '☼' if is_night else '☼')
        case 66: return (WeatherCodeLocales['light_freezing_rain'], '☼' if is_night else '☼')
        case 67: return (WeatherCodeLocales['heavy_freezing_rain'], '☼' if is_night else '☼')
        case 71: return (WeatherCodeLocales['slight_snow_fall'], '☼' if is_night else '☼')
        case 73: return (WeatherCodeLocales['moderate_snow_fall'], '☼' if is_night else '☼')
        case 75: return (WeatherCodeLocales['heavy_snow_fall'], '☼' if is_night else '☼')
        case 77: return (WeatherCodeLocales['snow_grains'], '☼')
        case 80: return (WeatherCodeLocales['slight_rain_showers'], '☼' if is_night else '☼')
        case 81: return (WeatherCodeLocales['moderate_rain_showers'], '☼' if is_night else '☼')
        case 82: return (WeatherCodeLocales['violent_rain_showers'], '☼' if is_night else '☼')
        case 85: return (WeatherCodeLocales['slight_snow_showers'], '☼' if is_night else '☼')
        case 86: return (WeatherCodeLocales['heavy_snow_showers'], '☼' if is_night else '☼')
        case 95: return (WeatherCodeLocales['thunderstorm'], '☼' if is_night else '☼')
        case 96: return (WeatherCodeLocales['thunderstorm_slight_hail'], '☼' if is_night else '☼')
        case 99: return (WeatherCodeLocales['thunderstorm_heavy_hail'], '☼' if is_night else '☼')
        case _ : return ("Unknown weather code", '0')
