import os

import kivy
kivy.require("2.0.0")

from kivy.lang import Builder
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

# icon
from mylittlego.core.utils import find_package_resource, PATHS
from kivy.config import Config
from kivy.utils import platform

ICON = find_package_resource("mylittlego/img/icon.ico")
Config.set("kivy", "window_icon", ICON)


class MyLittleGoGui(Screen):
    pass

class MyLittleGoApp(MDApp):
    def __init__(self):
        super().__init__()

    def build(self):
        self.icon = ICON

        self.title = f"{PROGRAM} v{VERSION}"
        self.theme_cls.theme_style = "Dark"

        kv_file = find_package_resource("mylittlego/gui.kv")
        Builder.load_file(kv_file)

        self.gui = MyLittleGoGui()
        return self.gui


def run_app():
    app = MyLittleGoApp()
    app.run()

if __name__ == "__main__":
    run_app()

