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
    
    @staticmethod
    def get_direction(wd):
        wd = wd % 360.0
        print(wd)
        if 337.5<=wd<=360.0 or 0.0<=wd<22.5: 
            print('hmm')
            return WindDirection.N

if __name__ == '__main__':
    a = WindDirection.get_direction(2)
    print(a==WindDirection.N)
