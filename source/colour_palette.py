import numpy as np

from PIL import Image, ImageDraw


class Palette(object):
    """"
    Class Doc

    ...

    Attributes
    ----------
    colour1 : np.ndarray
        the first colour in format [red, green, blue]
    colour2 : np.ndarray
        the second colour in format [red, green, blue]
    nb_tone : int
        the number of tone created by mixing colour1 and colour2
    palette = np.ndarray
        the result of mixing colours, it contains all tones demanded

    Methods
    -------
    createPalette()
        Create the demanded tones
    mixingColours()
        Mix colours to create each demanded tones.
    mixingColoursDarker(shade)
        Take a color and make darker tones of it
    mixingColoursLighter(shade)
        Take a color and make lighter tones of it
    """
    def __init__(self, colour1: np.ndarray, colour2: np.ndarray, nb_tone: int):
        self.colour1 = colour1
        self.colour2 = colour2
        self.nb_tone = nb_tone

        self.middle_palette = self.nb_tone // 2

        self.black = np.full((self.nb_tone, 3), 0)
        self.white = np.full((self.nb_tone, 3), 255)

        self.palette = np.empty((self.nb_tone, self.nb_tone, 3)).astype(int)
        self.colour_palette = None

    def createPalette(self) -> None:
        """Methode which create the demanded tones"""
        self.mixingColours()
        self.mixingColoursDarker()
        self.palette[self.middle_palette] = self.colour_palette
        self.mixingColoursLighter()

    def mixingColours(self):
        """
        Methode which mixes colours to create different tones

        """
        colour_palette = np.empty((self.nb_tone, 3))
        for pos_palette in range(self.middle_palette):
            colour_palette[pos_palette] = ((self.nb_tone - pos_palette) * self.colour1 + pos_palette * self.colour2) // self.nb_tone
            colour_palette[self.nb_tone - 1 - pos_palette] = (pos_palette * self.colour1 + (self.nb_tone - pos_palette) * self.colour2) // self.nb_tone

        colour_palette[self.middle_palette] = (self.colour1 + self.colour2) // 2

        self.colour_palette = colour_palette.astype(int)

    def mixingColoursDarker(self) -> None:
        """
        Methode which takes a color and make darker tones of it
        """
        darker_shade = self.colour_palette // self.middle_palette

        for darker_colour in range(self.middle_palette):
            darker_palette_line = ((self.middle_palette - darker_colour) * self.black + darker_colour * self.colour_palette) // self.middle_palette
            self.palette[darker_colour] = darker_palette_line.clip(min=0)

    def mixingColoursLighter(self) -> None:
        """
        Methode which takes a color and make lighter tones of it
        """
        lighter_shading = self.white // self.middle_palette

        for lighter_colour in range(1, self.middle_palette):
            lighter_palette_line = ((self.middle_palette - lighter_colour) * self.colour_palette + lighter_colour * self.white) // self.middle_palette
            self.palette[self.middle_palette + lighter_colour] = lighter_palette_line.clip(max=255)

        self.palette[self.nb_tone - 1] = self.white

    def generatePaletteLine(self, palette_line: np.ndarray) -> Image:
        """
        Create an image representation of the palette line

        Parameters
        ----------
        palette_line : np.ndarray
            Array containing the different colours of the palete line

        Returns
        -------
        Image
            Image representing the palette line
        """
        width_px = 1000
        image = Image.new(mode='RGB', size=(width_px, 120))

        for pos_color, color in enumerate(palette_line):
            img_color = Image.new(mode='RGB', size=(width_px // 15, 100), color=tuple(color))
            image.paste(img_color, (pos_color * width_px // self.nb_tone, 10))
        return image

    def generatePalette(self) -> Image:
        """
        Create an image representation of the palette

        Returns
        -------
        Image
            Image representing the palette
        """
        width_px = 1000
        height_px = 1000

        image = Image.new(mode='RGB', size=(width_px, height_px))

        for pos_line, palette_line in enumerate(self.palette):
            image_palette_line = self.generatePaletteLine(palette_line)
            image.paste(image_palette_line, (10, pos_line * height_px // self.nb_tone))
        return image
