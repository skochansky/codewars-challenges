__all__ = (
    "Frame",
    "FrameCreator",
    "FrameTemplate",
)

import typing as tp
from abc import abstractmethod, ABC
from dataclasses import dataclass


@dataclass
class Frame:
    mark: str
    width: int
    text: tp.List[str]
    longest_string: int


class FrameTemplate(ABC):
    def run(self) -> tp.NoReturn:
        """Run the template"""
        top_down_border = self.create_top_down_border()
        inside_content = self.create_inside_content()
        self.show(top_down_border, inside_content)

    @abstractmethod
    def create_top_down_border(self) -> str:
        pass

    @abstractmethod
    def create_inside_content(self) -> str:
        pass

    @staticmethod
    def show(top_down_border, inside_content) -> tp.NoReturn:
        """Print the content inside the frame"""
        print(top_down_border)
        for element in inside_content:
            print(element)
        print(top_down_border)


class FrameCreator(FrameTemplate):
    """Frame and inside data builder."""

    def create_top_down_border(self) -> str:
        """Return a string with the top and bottom border of the frame"""
        return Frame.mark * Frame.width

    def create_inside_content(self) -> tp.List[str]:
        """Return a list of strings with the inside content of the frame."""
        inside_content: tp.List[str] = []
        for element in Frame.text:
            padding = " " * (Frame.longest_string - (len(element)))
            inside_content.append(f"{Frame.mark} {element}{padding} {Frame.mark}")
        return inside_content


def create_frame(frame_template: tp.Type[FrameCreator]) -> tp.NoReturn:
    frame_template().run()


if __name__ == "__main__":
    Frame.mark = "+"
    Frame.text = ["Create", "a", "frame"]
    Frame.longest_string = len(max(Frame.text, key=len))
    Frame.width = Frame.longest_string + 4
    create_frame(FrameCreator)
