import numpy as np


class ColourPalette(object):
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
    mixingColours()
        Mix colours to create each demanded tones.
    """
    def __init__(self, colour1: np.ndarray, colour2: np.ndarray, nb_tone: int):
        self.colour1 = colour1
        self.colour2 = colour2
        self.nb_tone = nb_tone

        self.palette = np.empty((nb_tone, 3))
        self.middle_palette = self.nb_tone // 2

    def mixingColours(self) -> None:
        """"Methode which mixes colours to create each demanded tones"""
        for pos_palette in range(self.middle_palette):
            self.palette[pos_palette] = ((self.nb_tone - pos_palette) * self.colour1 + pos_palette * self.colour2) // self.nb_tone

            self.palette[self.nb_tone - 1 - pos_palette] = (pos_palette * self.colour1 + (self.nb_tone - pos_palette) * self.colour2) // self.nb_tone #pbl here

        self.palette[self.middle_palette] = (self.colour1 + self.colour2) // 2
