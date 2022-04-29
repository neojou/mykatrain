import os

import kivy
kivy.require("2.0.0")

from kivy.uix.screenmanager import Screen
from kivy.uix.widget import Widget
from kivymd.app import MDApp
from kivymd.uix.screen import MDScreen
from kivymd.uix.button import MDRectangleFlatButton

import sys
sys.path.append("../")
from mylittlego.core.constants import (
    PROGRAM,
    VERSION,
)

class MyLittleGo(MDApp):
    def __init__(self):
        super().__init__()

    def build(self):
        self.title = f"{PROGRAM} v{VERSION}"
        self.theme_cls.theme_style = "Dark"
        screen = MDScreen()
        screen.add_widget(
            MDRectangleFlatButton(
                text="Hello, World",
                pos_hint={"center_x": 0.5, "center_y": 0.5},
            )
        )
        return screen


def run_app():
    app = MyLittleGo()
    app.run()

if __name__ == "__main__":
    run_app()

