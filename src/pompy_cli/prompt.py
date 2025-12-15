from style import style, Ansi

def prompt_str(text=str, case_insensitive=False):
    print(text)
    user_input = input(style("(Enter any string.) ", color=Ansi.FG_CYAN))
    if case_insensitive:
        return user_input.lower()
    return user_input

if __name__ == "__main__":
    print("Your name is " + style(prompt_str("What's your name?", True), color=Ansi.BG_YELLOW, decoration=Ansi.BOLD, padding=1))
