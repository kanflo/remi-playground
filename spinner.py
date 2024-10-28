#!/usr/bin/env python

"""Demonstrate usage of the spinner widget"""

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
        spinner = gui.Spinner(size = 32, color = "#f00")
        container.append([spinner])
        return container

if __name__ == "__main__":
    remitools.start(MyApp, "A remi Spinner demo app", "Spinner!")
