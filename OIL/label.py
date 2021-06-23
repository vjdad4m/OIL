from OIL.color import Color

class Label:
    def __init__(self, name: str, color: Color):
        self.name = name
        self.color = color

    def __repr__(self):
        return f"Label('{self.name}', {self.color})"

def PaletteToLabel(palette):
    # Input is from ParseToPalette() in parser
    labels = []
    for e in palette:
        labels.append(Label(e, palette[e]))
    return labels