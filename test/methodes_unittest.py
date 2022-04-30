import unittest2
import numpy as np

from source.colour_palette import Palette


class TestColourPalette(unittest2.TestCase):
    """"Test Class Doc"""
    def testSimpleColourRedGreen11(self):
        """"Unit Test mixing 11 tone of simple colours : red & green"""
        red = np.array([255, 0, 0])
        green = np.array([0, 255, 0])

        palette = Palette(red, green, 11)
        palette.mixingColours()

        result_color_palette = palette.colour_palette
        expected_color_palette = np.array([[255, 0, 0], [231, 23, 0], [208, 46, 0], [185, 69, 0], [162, 92, 0],
                                           [127, 127, 0],
                                           [92, 162, 0], [69, 185, 0], [46, 208, 0], [23, 231, 0], [0, 255, 0]])

        self.assertTrue((expected_color_palette == result_color_palette).all())

    def testSimpleColourRedBlue11(self):
        """"Unit Test mixing 11 tone of simple colours : red & blue"""
        red = np.array([255, 0, 0])
        blue = np.array([0, 0, 255])

        palette = Palette(red, blue, 11)
        palette.mixingColours()

        result_color_palette = palette.colour_palette

        expected_color_palette = np.array([[255, 0, 0], [231, 0, 23], [208, 0, 46], [185, 0, 69], [162, 0, 92],
                                           [127, 0, 127],
                                           [92, 0, 162], [69, 0, 185], [46, 0, 208], [23, 0, 231], [0, 0, 255]])

        self.assertTrue((expected_color_palette == result_color_palette).all())

    def testSimpleColourGreenBlue11(self):
        """"Unit Test mixing 11 tone of simple colours : green & blue"""
        green = np.array([0, 255, 0])
        blue = np.array([0, 0, 255])

        palette = Palette(green, blue, 11)
        palette.mixingColours()

        result_color_palette = palette.colour_palette

        expected_color_palette = np.array([[0, 255, 0], [0, 231, 23], [0, 208, 46], [0, 185, 69], [0, 162, 92],
                                           [0, 127, 127],
                                           [0, 92, 162], [0, 69, 185], [0, 46, 208], [0, 23, 231], [0, 0, 255]])


        self.assertTrue((expected_color_palette == result_color_palette).all())

    def testSimpleColourGreenBlue11False(self):
        """"Unit Test mixing 11 tone of simple colours : green & blue, with a false expected palette"""
        green = np.array([0, 255, 0])
        blue = np.array([0, 0, 255])

        palette = Palette(green, blue, 11)
        palette.mixingColours()

        result_color_palette = palette.colour_palette

        expected_color_palette = np.array([[0, 0, 0], [0, 0, 23], [0, 208, 46], [0, 185, 0], [0, 162, 92],
                                           [0, 127, 0],
                                           [0, 92, 162], [0, 69, 185], [0, 46, 208], [0, 0, 231], [0, 0, 255]])

        self.assertFalse((expected_color_palette == result_color_palette).all())

    def testSimpleColourGreenBlue5(self):
        """"Unit Test mixing 5 tone of simple colours : green & blue"""
        green = np.array([0, 255, 0])
        blue = np.array([0, 0, 255])

        palette = Palette(green, blue, 5)
        palette.mixingColours()

        result_color_palette = palette.colour_palette

        expected_color_palette = np.array([[0, 255, 0], [0, 204, 51],
                                           [0, 127, 127],
                                           [0, 51, 204], [0, 0, 255]])

        self.assertTrue((expected_color_palette == result_color_palette).all())

    @staticmethod
    def isEqualArrayLine(array_line1: np.ndarray, array_line2: np.ndarray) -> bool:
        return np.array_equal(array_line1, array_line2)

    def testSimpleDarkerColour(self):
        green = np.array([0, 255, 0])
        blue = np.array([0, 0, 255])

        palette = Palette(green, blue, 11)
        palette.mixingColours()
        palette.mixingColoursDarker()

        result_darker_palette = palette.palette
        expected_darker_palette = np.array([
            [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]],
            [[0, 51, 0], [0, 46, 4], [0, 41, 9], [0, 37, 13], [0, 32, 18], [0, 25, 25], [0, 18, 32], [0, 13, 37], [0, 9, 41], [0, 4, 46], [0, 0, 51]],
            [[0, 102, 0], [0, 92, 8], [0, 82, 18], [0, 74, 26], [0, 64, 36], [0, 50, 50], [0, 36, 64], [0, 26, 74], [0, 18, 82], [0, 8, 92], [0, 0, 102]],
            [[0, 153, 0], [0, 138, 12], [0, 123, 27], [0, 111, 39], [0, 96, 54], [0, 75, 75], [0, 54, 96], [0, 39, 111], [0, 27, 123], [0, 12, 138], [0, 0, 153]],
            [[0, 204, 0], [0, 184, 16], [0, 164, 36], [0, 148, 52], [0, 128, 72], [0, 100, 100], [0, 72, 128], [0, 52, 148], [0, 36, 164], [0, 16, 184], [0, 0, 204]]
        ])

        is_equal = True
        line = 0
        while is_equal and line < 5:
            is_equal = self.isEqualArrayLine(result_darker_palette[line], expected_darker_palette[line])
            line += 1

        self.assertTrue(is_equal)

    def testSimpleLighterColour(self):
        green = np.array([0, 255, 0])
        blue = np.array([0, 0, 255])

        palette = Palette(green, blue, 11)
        palette.mixingColours()
        palette.mixingColoursLighter()

        result_lighter_palette = palette.palette
        expected_lighter_palette = np.array(
            [
                [[51, 255, 51], [51, 255, 74], [51, 255, 97], [51, 236, 120], [51, 213, 143], [51, 178, 178], [51, 143, 213], [51, 120, 236], [51, 97, 255], [51, 74, 255], [51, 51, 255]],
                [[102, 255, 102], [102, 255, 125], [102, 255, 148], [102, 255, 171], [102, 255, 194], [102, 229, 229], [102, 194, 255], [102, 171, 255], [102, 148, 255], [102, 125, 255], [102, 102, 255]],
                [[153, 255, 153], [153, 255, 176], [153, 255, 199], [153, 255, 222], [153, 255, 245], [153, 255, 255], [153, 245, 255], [153, 222, 255], [153, 199, 255], [153, 176, 255], [153, 153, 255]],
                [[204, 255, 204], [204, 255, 227], [204, 255, 250], [204, 255, 255], [204, 255, 255], [204, 255, 255], [204, 255, 255], [204, 255, 255], [204, 250, 255], [204, 227, 255], [204, 204, 255]],
                [[255, 255, 255], [255, 255, 255], [255, 255, 255], [255, 255, 255], [255, 255, 255], [255, 255, 255], [255, 255, 255], [255, 255, 255], [255, 255, 255], [255, 255, 255], [255, 255, 255]]
            ]
        )

        is_equal = True
        line = 0
        while is_equal and line < 5:
            is_equal = self.isEqualArrayLine(expected_lighter_palette[line], result_lighter_palette[6 + line])
            line += 1

        self.assertTrue(is_equal)

    def testCreatePaletteSimple(self):
        green = np.array([0, 255, 0])
        blue = np.array([0, 0, 255])

        palette = Palette(green, blue, 11)
        palette.createPalette()

        result_palette = palette.palette

        expected_palette = np.array(
            [
                [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]],
                [[0, 51, 0], [0, 46, 4], [0, 41, 9], [0, 37, 13], [0, 32, 18], [0, 25, 25], [0, 18, 32], [0, 13, 37], [0, 9, 41], [0, 4, 46], [0, 0, 51]],
                [[0, 102, 0], [0, 92, 8], [0, 82, 18], [0, 74, 26], [0, 64, 36], [0, 50, 50], [0, 36, 64], [0, 26, 74], [0, 18, 82], [0, 8, 92], [0, 0, 102]],
                [[0, 153, 0], [0, 138, 12], [0, 123, 27], [0, 111, 39], [0, 96, 54], [0, 75, 75], [0, 54, 96], [0, 39, 111], [0, 27, 123], [0, 12, 138], [0, 0, 153]],
                [[0, 204, 0], [0, 184, 16], [0, 164, 36], [0, 148, 52], [0, 128, 72], [0, 100, 100], [0, 72, 128], [0, 52, 148], [0, 36, 164], [0, 16, 184], [0, 0, 204]],

                [[0, 255, 0], [0, 231, 23], [0, 208, 46], [0, 185, 69], [0, 162, 92], [0, 127, 127], [0, 92, 162], [0, 69, 185], [0, 46, 208], [0, 23, 231], [0, 0, 255]],

                [[51, 255, 51], [51, 255, 74], [51, 255, 97], [51, 236, 120], [51, 213, 143], [51, 178, 178], [51, 143, 213], [51, 120, 236], [51, 97, 255], [51, 74, 255], [51, 51, 255]],
                [[102, 255, 102], [102, 255, 125], [102, 255, 148], [102, 255, 171], [102, 255, 194], [102, 229, 229], [102, 194, 255], [102, 171, 255], [102, 148, 255], [102, 125, 255], [102, 102, 255]],
                [[153, 255, 153], [153, 255, 176], [153, 255, 199], [153, 255, 222], [153, 255, 245], [153, 255, 255], [153, 245, 255], [153, 222, 255], [153, 199, 255], [153, 176, 255], [153, 153, 255]],
                [[204, 255, 204], [204, 255, 227], [204, 255, 250], [204, 255, 255], [204, 255, 255], [204, 255, 255], [204, 255, 255], [204, 255, 255], [204, 250, 255], [204, 227, 255], [204, 204, 255]],

                [[255, 255, 255], [255, 255, 255], [255, 255, 255], [255, 255, 255], [255, 255, 255], [255, 255, 255], [255, 255, 255], [255, 255, 255], [255, 255, 255], [255, 255, 255], [255, 255, 255]]
            ]
        )

        is_equal = True
        line = 0
        while is_equal and line < 11:
            is_equal = self.isEqualArrayLine(expected_palette[line], result_palette[line])
            line += 1

        self.assertTrue(is_equal)

    def test(self):
        red = np.array([255, 0, 0])
        blue = np.array([0, 0, 255])

        palette = Palette(red, blue, 5)
        palette.createPalette()
        result_palette = palette.palette

        palette.generatePalette().show()


