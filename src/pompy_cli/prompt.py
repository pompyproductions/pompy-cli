from style import style, Ansi
import util

def prompt_str(text=str, case_insensitive=False):
    print(style("------", color=Ansi.FG_BLUE))
    print(text)
    user_input = util.get_input("(Enter any string.)")
    if case_insensitive:
        return user_input.lower()
    return user_input

def prompt_bool(text=str):
    print(style("------", color=Ansi.FG_BLUE))
    print(text)
    user_input = util.get_input("(Y|N)").lower()
    while True:
        if user_input in ("y", "yes", "1", "true"):
            return True
        elif user_input in ("n", "no", "0", "false"):
            return False
        print(style("It's a yes or no question.", color=Ansi.FG_RED))
        user_input = util.get_input("(Y|N)").lower()
        

# Demo

if __name__ == "__main__":
    util.clear()
    print("Your name is " + style(prompt_str("What's your name?", True), color=Ansi.BG_YELLOW, decoration=Ansi.BOLD, padding=1))
    user_input = prompt_bool("Are you gae?")
    if user_input:
        print("You are gae")
    else:
        print("Who says I'm gae?")