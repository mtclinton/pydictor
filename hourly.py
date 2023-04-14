import display

DISPLAY_HOURS = [0, 3, 6, 9, 12, 15, 18, 21]
WIDTH = 72

class WeatherSummery:
    temp_max_min: str
    precipitation_probability_max: int
class  HourlyForecast:
    heading: str
    temperatures: str
    precipitation: str
    graph: Graph
    summary: WeatherSummery
    time_indicator_col: int

    def render(self):
        print(display.Separator.Blank.fmt(WIDTH, display.BorderStyle.double))
        temperature_unit = "F"
        precipitation_unit = "In"


