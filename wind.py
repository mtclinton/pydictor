from enum import Enum
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
            case WindDirection.N:
                return "N"
            case WindDirection.NE:
                return "NE"
            case WindDirection.E:
                return "E"
            case WindDirection.SE:
                return "SE"
            case WindDirection.S:
                return "S"
            case WindDirection.SW:
                return "SW"
            case WindDirection.W:
                return "W"
            case WindDirection.NW:
                return "NW"

    @staticmethod
    def get_direction(wd):
        wd = wd % 360.0
        if 337.5 <= wd <= 360.0 or 0.0 <= wd < 22.5:
            return WindDirection.N
        elif 22.5 <= wd < 67.5:
            return WindDirection.NE
        elif 67.5 <= wd < 112.5:
            return WindDirection.E
        elif 112.5 <= wd < 157.5:
            return WindDirection.SE
        elif 157.5 <= wd < 202.5:
            return WindDirection.S
        elif 202.5 <= wd < 247.5:
            return WindDirection.SW
        elif 247.5 <= wd < 292.5:
            return WindDirection.W
        elif 292.5 <= wd < 337.5:
            return WindDirection.NW
        else:
            return "Wind from another dimension"

    def get_icon(self):
        match self:
            case WindDirection.N:
                return '↑'
            case WindDirection.NE:
                return '↗'
            case WindDirection.E:
                return '→'
            case WindDirection.SE:
                return '↘'
            case WindDirection.S:
                return '↓'
            case WindDirection.SW:
                return '↙'
            case WindDirection.W:
                return '←'
            case WindDirection.NW:
                return '↖'