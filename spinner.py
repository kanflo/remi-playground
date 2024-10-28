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
    if "-h" in sys.argv or "--help" in sys.argv:
        print(f"Usage: {sys.argv[0]} [-d] [-v] [-b]")
        print(" -d  Set REMI log level to debug")
        print(" -v  Set application log level to debug")
        print(" -b  Open application in browser")
        sys.exit(0)

    remi_debug: bool = "-d" in sys.argv
    app_debug: bool = "-d" in sys.argv
    fmt: str = "%(asctime)s %(name)-20s [%(lineno)4d] | %(message)s"
    coloredlogs.install(level = logging.DEBUG if app_debug else logging.INFO, fmt=fmt)
    start(MyApp, debug = remi_debug, address = "127.0.0.1", port = 8888, start_browser = "-b" in sys.argv)
