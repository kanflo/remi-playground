#!/usr/bin/env python

"""Demonstrate usage of the spinner widget and the rounded button"""

import logging

import remi.gui as gui
from remi import App

import remitools


logger = logging.getLogger(__name__)

class MyApp(App):
    def __init__(self, *args):
        super(MyApp, self).__init__(*args)

    def main(self):
        container = gui.Container(width = 540, margin = "0px auto", style = {"display": "block", "overflow": "hidden"})
        self.button = gui.RoundedButton("Start", width=100, height=30, margin="10px")
        self.button.onclick.do(self.on_button_pressed)
        self.spinner = gui.Spinner(size = 20, color = "#f00")
        container.append([self.spinner, self.button])
        return container

    def on_button_pressed(self, widget: gui.Widget):
        if widget == self.button:
            if self.spinner.is_spinning:
                self.spinner.stop()
            else:
                self.spinner.start()
            self.button.set_text('Stop' if self.spinner.is_spinning else "Start")

if __name__ == "__main__":
    remitools.start(MyApp, "A remi Spinner demo app", "Spinner!")
