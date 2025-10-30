import time
from blinkable import Blinkable
from smiley import Smiley


class Angry(Smiley, Blinkable):
    """A Smiley subclass showing an angry red face."""

    def __init__(self):
        super().__init__()
        self.draw_eyes()
        self.draw_mouth()

    def complexion(self):
        """Return a red face color for anger."""
        return self.RED

    def draw_eyes(self, wide_open=True):
        """
        Draws angry slanted eyes (like > <)
        :param wide_open: If False, draws 'closed' angry eyes.
        """
        left_eye = [9, 18]    # tilted down
        right_eye = [14, 21]  # tilted down
        eye_color = self.BLANK if wide_open else self.complexion()
        for pixel in left_eye + right_eye:
            self.pixels[pixel] = eye_color

    def draw_mouth(self):
        """
        Draws the mouth feature on a smiley
        """
        mouth = [49, 54, 42, 43, 44, 45]
        for pixel in mouth:
            self.pixels[pixel] = self.BLANK

    def blink(self, delay=0.5):
        """Blinks once, using the Blinkable interface."""
        self.draw_eyes(wide_open=False)
        self.show()
        time.sleep(delay)
        self.draw_eyes(wide_open=True)
        self.show()
