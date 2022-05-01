import unittest2
import numpy as np

from source.colour_palette import Palette


class TestColourPalette(unittest2.TestCase):
    """"Test Class Doc"""
    def testSimpleColourRedGreen11(self):
        """"
        Unit Test :
        It mixes 11 tone of simple colours : red & green"""
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
        """"
        Unit Test :
        It mixes 11 tones of simple colours : red & blue"""
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
        """"
        Unit Test :
        It mixes 11 tones of simple colours : green & blue"""
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
        """"
        Unit Test :
        It mixes 11 tones of simple colours : green & blue, with a false expected palette"""
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
        """"
        Unit Test :
        It mixes 5 tones of simple colours : green & blue"""
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
        """
        Compare two arrays equality

        Parameters
        ----------
        array_line1 : np.ndarray
            Array containing data, here colors represented as [red, green, blue] (red, green, blue = int)
        array_line2 : np.ndarray
            Array containing data, here colors represented as [red, green, blue] (red, green, blue = int)

        Returns
        -------
        bool
            The equality answer
        """
        return np.array_equal(array_line1, array_line2)

    def testSimpleDarkerColour(self):
        """"
        Unit Test :
        It mixes 11 tones of simple colours and create 11 shades of their darker tones: green & blue"""

        green = np.array([0, 255, 0])
        blue = np.array([0, 0, 255])

        palette = Palette(green, blue, 11)
        palette.mixingColours()
        palette.mixingColoursDarker()

        result_darker_palette = palette.palette
        expected_darker_palette = np.array([
            [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]],
            [[0, 51, 0], [0, 46, 4], [0, 41, 9], [0, 37, 13], [0, 32, 18], [0, 25, 25], [0, 18, 32], [0, 13, 37], [0, 9, 41], [0, 4, 46], [0, 0, 51]],
            [[0, 102, 0], [0, 92, 9], [0, 83, 18], [0, 74, 27], [0, 64, 36], [0, 50, 50], [0, 36, 64], [0, 27, 74], [0, 18, 83], [0, 9, 92], [0, 0, 102]],
            [[0, 153, 0], [0, 138, 13], [0, 124, 27], [0, 111, 41], [0, 97, 55], [0, 76, 76], [0, 55, 97], [0, 41, 111], [0, 27, 124], [0, 13, 138], [0, 0, 153]],
            [[0, 204, 0], [0, 184, 18], [0, 166, 36], [0, 148, 55], [0, 129, 73], [0, 101, 101], [0, 73, 129], [0, 55, 148], [0, 36, 166], [0, 18, 184], [0, 0, 204]]
        ])

        is_equal = True
        line = 0
        while is_equal and line < 5:
            is_equal = self.isEqualArrayLine(result_darker_palette[line], expected_darker_palette[line])
            line += 1

        self.assertTrue(is_equal)

    def testSimpleLighterColour(self):
        """"
        Unit Test :
        It mixes 11 tones of simple colours and create 11 shades of their lighter tones: green & blue"""
        green = np.array([0, 255, 0])
        blue = np.array([0, 0, 255])

        palette = Palette(green, blue, 11)
        palette.mixingColours()
        palette.mixingColoursLighter()

        result_lighter_palette = palette.palette
        expected_lighter_palette = np.array(
            [
                [[51, 255, 51], [51, 235, 69], [51, 217, 87], [51, 199, 106], [51, 180, 124], [51, 152, 152], [51, 124, 180], [51, 106, 199], [51, 87, 217], [51, 69, 235], [51, 51, 255]],
                [[102, 255, 102], [102, 240, 115], [102, 226, 129], [102, 213, 143], [102, 199, 157], [102, 178, 178], [102, 157, 199], [102, 143, 213], [102, 129, 226], [102, 115, 240], [102, 102, 255]],
                [[153, 255, 153], [153, 245, 162], [153, 236, 171], [153, 227, 180], [153, 217, 189], [153, 203, 203], [153, 189, 217], [153, 180, 227], [153, 171, 236], [153, 162, 245], [153, 153, 255]],
                [[204, 255, 204], [204, 250, 208], [204, 245, 213], [204, 241, 217], [204, 236, 222], [204, 229, 229], [204, 222, 236], [204, 217, 241], [204, 213, 245], [204, 208, 250], [204, 204, 255]],
                [[255, 255, 255], [255, 255, 255], [255, 255, 255], [255, 255, 255], [255, 255, 255], [255, 255, 255], [255, 255, 255], [255, 255, 255], [255, 255, 255], [255, 255, 255], [255, 255, 255]]
            ])

        is_equal = True
        line = 0
        while is_equal and line < 5:
            is_equal = self.isEqualArrayLine(expected_lighter_palette[line], result_lighter_palette[6 + line])
            line += 1
        self.assertTrue(is_equal)

    def testCreatePaletteSimple(self):
        """"
        Unit Test :
        It mixes 11 tones of simple colours and make 11 shades of their darker & lighter tones to create the all palette: green & blue"""
        green = np.array([0, 255, 0])
        blue = np.array([0, 0, 255])

        palette = Palette(green, blue, 11)
        palette.createPalette()

        result_palette = palette.palette

        expected_palette = np.array(
            [
                [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]],
                [[0, 51, 0], [0, 46, 4], [0, 41, 9], [0, 37, 13], [0, 32, 18], [0, 25, 25], [0, 18, 32], [0, 13, 37], [0, 9, 41], [0, 4, 46], [0, 0, 51]],
                [[0, 102, 0], [0, 92, 9], [0, 83, 18], [0, 74, 27], [0, 64, 36], [0, 50, 50], [0, 36, 64], [0, 27, 74], [0, 18, 83], [0, 9, 92], [0, 0, 102]],
                [[0, 153, 0], [0, 138, 13], [0, 124, 27], [0, 111, 41], [0, 97, 55], [0, 76, 76], [0, 55, 97], [0, 41, 111], [0, 27, 124], [0, 13, 138], [0, 0, 153]],
                [[0, 204, 0], [0, 184, 18], [0, 166, 36], [0, 148, 55], [0, 129, 73], [0, 101, 101], [0, 73, 129], [0, 55, 148], [0, 36, 166], [0, 18, 184], [0, 0, 204]],

                [[0, 255, 0], [0, 231, 23], [0, 208, 46], [0, 185, 69], [0, 162, 92], [0, 127, 127], [0, 92, 162], [0, 69, 185], [0, 46, 208], [0, 23, 231], [0, 0, 255]],

                [[51, 255, 51], [51, 235, 69], [51, 217, 87], [51, 199, 106], [51, 180, 124], [51, 152, 152], [51, 124, 180], [51, 106, 199], [51, 87, 217], [51, 69, 235], [51, 51, 255]],
                [[102, 255, 102], [102, 240, 115], [102, 226, 129], [102, 213, 143], [102, 199, 157], [102, 178, 178], [102, 157, 199], [102, 143, 213], [102, 129, 226], [102, 115, 240], [102, 102, 255]],
                [[153, 255, 153], [153, 245, 162], [153, 236, 171], [153, 227, 180], [153, 217, 189], [153, 203, 203], [153, 189, 217], [153, 180, 227], [153, 171, 236], [153, 162, 245], [153, 153, 255]],
                [[204, 255, 204], [204, 250, 208], [204, 245, 213], [204, 241, 217], [204, 236, 222], [204, 229, 229], [204, 222, 236], [204, 217, 241], [204, 213, 245], [204, 208, 250], [204, 204, 255]],
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

        palette = Palette(red, blue, 21)
        palette.createPalette()
        result_palette = palette.palette

        palette.generatePalette().show()


