from kivy.app import App
from kivy.lang import Builder


class Converter(App):
    def build(self):
        self.title = "Converter"
        self.root = Builder.load_file('converter.kv')
        return self.root

    def handle_calculate(self, text):
        """ handle calculation (could be button press or other call), output result to label widget """
        try:
            value = float(text)
            result = value / 0.62137
            self.root.ids.label_text.text = str(result)
        except ValueError:
            self.root.ids.label_text.text = "Error"

    def handle_increment(self, increment):
        value = int(self.root.ids.input_number.text) + increment
        self.root.ids.input_number.text = str(value)
        self.handle_calculate(value)

Converter().run()