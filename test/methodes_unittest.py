import unittest2
import numpy as np

from source.colour_palette import ColourPalette


class TestColourMixer(unittest2.TestCase):
    """"Test Class Doc"""
    def testSimpleColorRedGreen11(self):
        """"Unit Test mixing 11 tone of simple colours : red & green"""
        red = np.array([255, 0, 0])
        green = np.array([0, 255, 0])

        colour_palette = ColourPalette(red, green, 11)

        expected_color_palette = np.array([[255, 0, 0], [231, 23, 0], [208, 46, 0], [185, 69, 0], [162, 92, 0],
                                           [127, 127, 0],
                                           [92, 162, 0], [69, 185, 0], [46, 208, 0], [23, 231, 0], [0, 255, 0]])

        colour_palette.mixingColours()

        self.assertTrue((expected_color_palette == colour_palette.palette).all())

    def testSimpleColorRedBlue11(self):
        """"Unit Test mixing 11 tone of simple colours : red & blue"""
        red = np.array([255, 0, 0])
        blue = np.array([0, 0, 255])

        colour_palette = ColourPalette(red, blue, 11)

        expected_color_palette = np.array([[255, 0, 0], [231, 0, 23], [208, 0, 46], [185, 0, 69], [162, 0, 92],
                                           [127, 0, 127],
                                           [92, 0, 162], [69, 0, 185], [46, 0, 208], [23, 0, 231], [0, 0, 255]])

        colour_palette.mixingColours()

        self.assertTrue((expected_color_palette == colour_palette.palette).all())

    def testSimpleColorGreenBlue11(self):
        """"Unit Test mixing 11 tone of simple colours : green & blue"""
        green = np.array([0, 255, 0])
        blue = np.array([0, 0, 255])

        colour_palette = ColourPalette(green, blue, 11)

        expected_color_palette = np.array([[0, 255, 0], [0, 231, 23], [0, 208, 46], [0, 185, 69], [0, 162, 92],
                                           [0, 127, 127],
                                           [0, 92, 162], [0, 69, 185], [0, 46, 208], [0, 23, 231], [0, 0, 255]])

        colour_palette.mixingColours()

        self.assertTrue((expected_color_palette == colour_palette.palette).all())

    def testSimpleColorGreenBlue11False(self):
        """"Unit Test mixing 11 tone of simple colours : green & blue, with a false expected palette"""
        green = np.array([0, 255, 0])
        blue = np.array([0, 0, 255])

        colour_palette = ColourPalette(green, blue, 11)

        expected_color_palette = np.array([[0, 0, 0], [0, 0, 23], [0, 208, 46], [0, 185, 0], [0, 162, 92],
                                           [0, 127, 0],
                                           [0, 92, 162], [0, 69, 185], [0, 46, 208], [0, 0, 231], [0, 0, 255]])

        colour_palette.mixingColours()

        self.assertFalse((expected_color_palette == colour_palette.palette).all())

    def testSimpleColorGreenBlue5(self):
        """"Unit Test mixing 5 tone of simple colours : green & blue"""
        green = np.array([0, 255, 0])
        blue = np.array([0, 0, 255])

        colour_palette = ColourPalette(green, blue, 5)

        expected_color_palette = np.array([[0, 255, 0], [0, 204, 51],
                                           [0, 127, 127],
                                           [0, 51, 204], [0, 0, 255]])

        colour_palette.mixingColours()

        self.assertTrue((expected_color_palette == colour_palette.palette).all())


