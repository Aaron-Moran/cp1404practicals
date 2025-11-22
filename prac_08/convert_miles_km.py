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
        self.title = "Convert Miles to Kilometres"
        self.root = Builder.load_file("convert_miles_km.kv")
        return self.root

    def handle_convert(self):
        """Handle converting miles to kilometres and updating the label."""
        miles = self.get_valid_miles()
        kilometres = miles * MILES_TO_KM
        self.root.ids.output_label.text = f"{kilometres:.5f}"

    def handle_change(self, change: float):
        """Handle pressing Up or Down to change the miles value."""
        miles = self.get_valid_miles() + change
        self.root.ids.input_miles.text = str(miles)

    def get_valid_miles(self):
        """Return the input miles value or 0.0 if the input is invalid."""
        try:
            return float(self.root.ids.input_miles.text)
        except ValueError:
            return 0.0

MilesToKmApp().run()