"""
CP1404/CP5632 Practical
Convert miles to kilometres using a Kivy GUI.
"""

from kivy.app import App
from kivy.lang import Builder
from kivy.core.window import Window

MILES_TO_KM = 1.609344

class MilesToKmApp(App):
    """Kivy App for converting miles to kilometres."""

    def build(self):
        """Build the Kivy app from the kv file."""
        Window.size = (600, 200)
        self.title = "Convert Miles to Kilometres"
        self.root = Builder.load_file("convert_miles_km.kv")
        return self.root

MilesToKmApp().run()