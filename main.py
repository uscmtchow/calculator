# 11/29/2022
# Created by Max Chow

from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.config import Config

Config.set('graphics', 'resizable', 1)


# used to solve the equation
class CalcGridLayout(GridLayout):
    def calculate(self, calculation):
        if calculation:
            try:
                self.display.text = str(eval(calculation))
            except Exception:
                self.display.text = "Error"


class CalculatorApp(App):
    def build(self):
        return CalcGridLayout()

# runs the code
calcApp = CalculatorApp()
calcApp.run()
