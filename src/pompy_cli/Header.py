from dataclasses import dataclass, field
from style import style, Ansi

@dataclass
class Line:
    width: int = 1
    style: str = "o-|o"


@dataclass
class Box:
    color: Ansi = field(default_factory= lambda: Ansi.FG_CYAN)
    left: Line = field(default_factory= lambda: Line(1))
    right: Line = field(default_factory= lambda: Line(1))
    top: Line = field(default_factory= lambda: Line(1))
    bottom: Line = field(default_factory= lambda: Line(1))
    padding_x: int = 2
    padding_y: int = 0


@dataclass
class Header:
    title: str
    color: Ansi = None
    borders: Box = field(default_factory= lambda:Box())

    def render(self,*, subtitle="", display_title=True):
        for _ in range(self.borders.top.width):
            print(
                self.borders.top.style[0] +
                self.borders.top.style[1] * (len(self.title) + self.borders.padding_x * 2) +
                self.borders.top.style[3]
            )
        for _ in range(self.borders.padding_y):
            print(
                self.borders.left.style[2] * self.borders.left.width +
                " " * (len(self.title) + self.borders.padding_x * 2) +
                self.borders.right.style[2] * self.borders.right.width
            )
        print(
            self.borders.left.style[2] * self.borders.left.width +
            self.borders.padding_x * " " +
            self.title +
            self.borders.padding_x * " " +
            self.borders.right.style[2] * self.borders.right.width
        )
        for _ in range(self.borders.padding_y):
            print(
                self.borders.left.style[2] * self.borders.left.width +
                " " * (len(self.title) + self.borders.padding_x * 2) +
                self.borders.right.style[2] * self.borders.right.width
            )
        for _ in range(self.borders.bottom.width):
            print(
                self.borders.bottom.style[0] +
                self.borders.bottom.style[1] * (len(self.title) + self.borders.padding_x * 2) +
                self.borders.bottom.style[3]
            )

