from enum import Enum

class Border(Enum):
    TL = 1
    T = 2
    TR = 3
    R = 4
    BR = 5
    B = 6
    BL = 7
    L = 8
    
    def fmt(self, style):
        match self:
            case Border.TL:
                match style:
                    case BorderStyle.single:
                        return "┌"
                    case BorderStyle.solid :
                        return "┏"
                    case BorderStyle.solid :
                        return "╔"
                    case _:
                    	return "╭"
            case (Border.T | Border.B):
                match style:
                    case BorderStyle.double:
                        return "═"
                    case BorderStyle.solid :
                        return "━"
            case Border.TR:
                match style:
                    case BorderStyle.single:
                        return "┐"
                    case BorderStyle.solid :
                        return "┓"
                    case BorderStyle.solid :
                        return "╗"
                    case _:
                    	return "╮"
            case (Border.R | Border.L):
                match style:
                    case BorderStyle.double: return "║"
                    case BorderStyle.solid: return "┃"
                    case _: return "│"
            case Border.BR:
                match style:
                    case BorderStyle.single:
                        return "┘"
                    case BorderStyle.solid :
                        return "┛"
                    case BorderStyle.solid :
                        return "╝"
                    case _:
                    	return "╯"
            case Border.BL:
                match style:
                    case BorderStyle.single:
                        return "└"
                    case BorderStyle.solid :
                        return "┗"
                    case BorderStyle.solid :
                        return "╚"
                    case _:
                    	return "╰"
    

class BorderStyle(Enum):
    rounded = 1
    single = 2
    solid = 3
    double = 4
    
class Edge(Enum):
    Top = 1
    Bottom = 2
    
    def fmt(self, width, style):
        match self:
            case Edge.Top:
                return f"{Border.TL.fmt(style)}{Border.T.fmt(style)*width}{Border.TR.fmt(style)}"
            case Edge.Bottom:
                return f"{Border.BL.fmt(style)}{Border.B.fmt(style)*width}{Border.BR.fmt(style)}"
                
class Separator(Enum):
    Blank = 1
    Single = 2
    Solid = 3
    Double = 4
    Dashed = 5
    
    def fmt(self, width, style):
        match self:
            case Separator.Blank: 
                sep = " " * width
                return f"{Border.L.fmt(style)}{sep}{Border.R.fmt(style)}"
            case Separator.Single: 
                sep = "┈"*width
                return f"├{sep}┤"
            case Separator.Solid: 
                sep = "─"*width
                return f"├{sep}┤"
            case Separator.Double: 
                sep = "─"*width
                return f"┠{sep}┨"
            case Separator.Dashed: 
                sep = "─"*width
                return f"╟{sep}╢"

if __name__ == "__main__":
    e = Separator.Double
    print(e.fmt(10, BorderStyle.solid))

