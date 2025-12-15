from style import style, Ansi
import util

class Option:
    def __init__(self, long, short, aliases=[], description="No description."):
        self.long = long
        self.short = short
        self.aliases = aliases
        self.description = description


def prompt_str(text=str, case_insensitive=False):
    print(style("------", color=Ansi.FG_BLUE))
    print(text)
    user_input = util.get_input("(Enter any string.)")
    print()
    if case_insensitive:
        return user_input.lower()
    return user_input


def prompt_bool(text=str):
    print(style("------", color=Ansi.FG_BLUE))
    print(text)
    user_input = util.get_input("(Y|N)").lower()
    while True:
        print()
        if user_input in ("y", "yes", "1", "true"):
            return True
        elif user_input in ("n", "no", "0", "false"):
            return False
        print(style("It's a yes or no question.", color=Ansi.FG_RED))
        user_input = util.get_input("(Y|N)").lower()


def prompt_opt(text=str, options=list[Option]):
    print()
    print(style("------", color=Ansi.FG_BLUE))
    print(text)

    display = f"({"|".join([opt.short for opt in options])})"
    valid = []
    for opt in options:
        valid += (opt.short, opt.long, *opt.aliases)
    user_input = util.get_input(display).lower()
    while user_input not in valid:
        print(style("That's not a valid option.", color=Ansi.FG_RED))
        user_input = util.get_input(display).lower()

    return user_input


# Demo

if __name__ == "__main__":
    util.clear()
    print("Your name is " + style(prompt_str("What's your name?", True), color=Ansi.BG_YELLOW, decoration=Ansi.BOLD, padding=1))
    user_input = prompt_bool("Are you gae?")
    if user_input:
        print("You are gae")
    else:
        print("Who says I'm gae?")
    user_input = prompt_opt("What will you do?", options=[
        Option("quit", "q", ("exit", "close"), "Quit the program."),
        Option("restart", "r")
    ])
    print(user_input)