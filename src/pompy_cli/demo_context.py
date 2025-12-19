from style import Ansi, style
from prompt import prompt_str

def demo_context():
    from CLIContext import CLIContext
    from Header import Header

    ctx = CLIContext(
        header=Header("Pompy CLI Demo"),
        color2=Ansi.FG_BLUE,
        color3=Ansi.FG_CYAN,
    )
    ctx.print("This is a demo of the CLIContext class.", clear=True)
    ctx.print("It supports colored output and headers.", color=Ansi.BG_YELLOW, padding=1)
    ctx.input("(Press anything to continue.)")
    name = ctx.prompt_str("What's your name?")
    ctx.print(f"That's your name huh, {style(name.title(), color=Ansi.BG_YELLOW, padding=1)}.", separate=True)
    ctx.print("Now we'll clear the screen.")
    ctx.input("(Press anything to continue.)")
    ctx.print("See you later!", clear=True)



if __name__ == "__main__":
    demo_context()