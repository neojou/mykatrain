import os

import kivy
kivy.require("2.0.0")

from kivymd.app import MDApp

import sys
sys.path.append("../")
from mylittlego.core.constants import (
    PROGRAM,
    VERSION,
)

class KaTrainApp(MDApp):
    def __init__(self):
        super().__init__()

    def build(self):
        self.title = f"{PROGRAM} v{VERSION}"


def run_app():
    app = KaTrainApp()
    app.run()

if __name__ == "__main__":
    run_app()

