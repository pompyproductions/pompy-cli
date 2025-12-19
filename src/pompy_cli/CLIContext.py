import prompt
import util
from style import Ansi, style
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
        self.is_cleared = False

    def clear(self):
        util.clear()
        if self.header:
            self.header.render()
        self.is_cleared = True
    
    def input(self, text):
        util.get_input(text, color=self.color3)
    
    def print(self, str, *, 
            separate=False, clear=False, color=None,
        ):
        if clear and not self.is_cleared:
            self.clear()
        elif separate:
            self.print_separator()
        if color:
            str = style(str, color=color)
        elif self.color1:
            str = style(str, color=self.color1)
        print(str)
        self.is_cleared = False

    def print_separator(self):
        if self.separator:
            print(style(self.separator * 40, color=self.color2) + "\n")
    
    def prompt_str(self, text, *, 
            separate=False, clear=False, color=None,
        ):
        self.print(text, separate=separate, clear=clear, color=color)
        return prompt.prompt_str(ctx=True)