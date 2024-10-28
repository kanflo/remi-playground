#!/usr/bin/env python

"""Demonstrate usage of the spinner widget"""

import remi.gui as gui
from remi import start, App
import sys
import coloredlogs, logging

logger = logging.getLogger(__name__)

class MyApp(App):
    def __init__(self, *args):
        super(MyApp, self).__init__(*args)

    def main(self):
        container = gui.Container(width = 540, margin = '0px auto', style = {'display': 'block', 'overflow': 'hidden'})
        spinner = gui.Spinner(size = 32, color = "#f00")
        container.append([spinner])
        return container

if __name__ == "__main__":
    debug: bool = "-d" in sys.argv
    fmt: str = "%(asctime)s %(name)-20s | %(message)s"
    coloredlogs.install(level = logging.DEBUG if debug else logging.INFO, fmt=fmt)
    start(MyApp, address = "127.0.0.1", port = 8888, start_browser = "-b" in sys.argv)
