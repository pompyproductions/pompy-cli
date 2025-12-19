from style import style, Ansi
import util

class Option:
    def __init__(self, long, short, aliases=[], description="No description."):
        self.long = long
        self.short = short
        self.aliases = aliases
        self.description = description


def prompt_str(text:str="", *, ctx:bool=False, 
        case_sensitive=False, accept_empty=False, trim=True, min=0
        ):
    if not ctx and text:
        print(text)
    while True:
        user_input = util.get_input("(Enter any string.)")
        if trim:
            user_input = user_input.strip()
        if not accept_empty and not user_input:
            print(style("Try entering something.", color=Ansi.FG_RED))
        elif len(user_input) < min:
            print(style(f"Please enter at least {min} characters.", color=Ansi.FG_RED))
        elif not case_sensitive:
            return user_input.lower()
        else:
            return user_input


def prompt_bool(text=str):
    print(text)
    user_input = util.get_input("(Y|N)").lower()
    while True:
        if user_input in ("y", "yes", "1", "true"):
            return True
        elif user_input in ("n", "no", "0", "false"):
            return False
        print(style("It's a yes or no question.", color=Ansi.FG_RED))
        user_input = util.get_input("(Y|N)").lower()


def prompt_opt(text=str, options=list[Option]):
    print(text)

    display = f"({"|".join([opt.short for opt in options])})"
    user_input = util.get_input(display).strip().lower()
    if not user_input:
        print(style("Try entering something.", color=Ansi.FG_RED))

    while True:
        for opt in options:
            if user_input in (opt.short, opt.long, *opt.aliases):
                return opt.long
        print(style("That's not a valid option.", color=Ansi.FG_RED))
        user_input = util.get_input(display).lower()


def prompt_int(text=str, *, min:int, max:int):
    print(text)
    display = "("
    if min is not None:
        display += str(min)
        if max is not None:
            display += f"-{max})"
        else:
            display += " or higher)"
    elif max is not None:
        display += f"up to {max})"
    else:
        display += "any integer)"
    while True:
        user_input = util.get_input(display).strip()
        if not user_input:
            print(style(f"Try entering something.", color=Ansi.FG_RED))
            continue
        try:
            user_input = int(user_input)
            if min is not None and user_input < min:
                print(style(f"Please enter a number bigger than {min}.", color=Ansi.FG_RED))
            elif max is not None and user_input > max:
                print(style(f"Please enter a number smaller than {max}.", color=Ansi.FG_RED))
            else:
                return user_input
        except ValueError:
            print(style("Please only enter numbers.", color=Ansi.FG_RED))
