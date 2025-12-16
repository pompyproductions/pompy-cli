import util
from style import Ansi
from Header import Header

class CLIContext:
    def __init__(
            self, *, 
            header=None, 
            color1=None,
            color2=Ansi.FG_CYAN,
            color3=Ansi.FG_PURPLE,
            separator="-"
            ):
        self.color1 = color1
        self.color2 = color2
        self.color3 = color3
        self.separator = separator
        self.header = header
        self.is_cleared = True

    def clear(self):
        util.clear()
        if self.header:
            self.header.render()
        self.is_cleared = True

