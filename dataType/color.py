import re


class ColorRGB(object):
    """
    Class for handling color in rgb format

    to use a pre-defined color:
    red = ColorRGB.red()
    print(red.r, red.g, red.b)

    to define a custom color, put rgb code as arguments:
    my_color = ColorRGB(112, 24, 200)
    """

    def __init__(self, r, g, b):
        try:
            r = int(r)
            g = int(g)
            b = int(b)

            value_range = range(0, 256)

            for channel in [r, g, b]:
                if channel not in value_range:
                    raise ValueError

        except ValueError:
            raise ValueError(
                "please enter integer value from 0 to 255 for rgb code"
            )

        self._r = r
        self._g = g
        self._b = b

    def __str__(self):
        return '{}({}, {}, {})'.format(
            self.__class__.__name__,
            self.r,
            self.g,
            self.b
        )

    @classmethod
    def from_hex(cls, hexcode='#000000'):
        pattern = r'^#(?:[0-9a-fA-F]{3}){1,2}$'
        regex = re.compile(pattern)

        match = regex.search(hexcode)
        if not match:
            raise ValueError("not match")

        r = int(hexcode[1:3], 16)
        g = int(hexcode[3:5], 16)
        b = int(hexcode[5:], 16)
        return cls(r, g, b)

    @classmethod
    def red(cls):
        return cls(255, 0, 0)

    @classmethod
    def green(cls):
        return cls(0, 255, 0)

    @classmethod
    def blue(cls):
        return cls(0, 0, 255)

    @classmethod
    def white(cls):
        return cls(255, 255, 255)

    @classmethod
    def black(cls):
        return cls(0, 0, 0)

    @classmethod
    def gray(cls):
        return cls(128, 128, 128)

    @classmethod
    def cyan(cls):
        return cls(0, 255, 255)

    @classmethod
    def magenta(cls):
        return cls(255, 0, 255)

    @classmethod
    def yellow(cls):
        return cls(255, 255, 0)

    @classmethod
    def silver(cls):
        return cls(192, 192, 192)

    @classmethod
    def purple(cls):
        return cls(128, 0, 128)

    @property
    def r(self):
        return self._r

    @property
    def g(self):
        return self._g

    @property
    def b(self):
        return self._b

    @property
    def r_normalized(self):
        return self._r/255.00

    @property
    def g_normalized(self):
        return self._g/255.00

    @property
    def b_normalized(self):
        return self._b/255.00

    def blend(self, color='', percent=0.5):
        if not color:
            color = self.white()

        r = self.r * (1-percent) + color.r * percent
        g = self.g * (1-percent) + color.g * percent
        b = self.b * (1-percent) + color.b * percent

        return ColorRGB(r, g, b)

    @property
    def hexcode(self):
        return '#{r}{g}{b}'.format(
            r='{:x}'.format(self.r),
            g='{:x}'.format(self.g),
            b='{:x}'.format(self.b)
        )
