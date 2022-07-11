import os

import kivy
kivy.require("2.0.0")
from kivy.config import Config
from kivy.utils import platform

from kivy.base import ExceptionHandler, ExceptionManager
from kivy.app import App
from kivy.core.clipboard import Clipboard
from kivy.lang import Builder
from kivy.resources import resource_add_path
from kivy.uix.popup import Popup
from kivy.uix.screenmanager import Screen
from kivy.core.window import Window
from kivy.uix.widget import Widget
from kivy.resources import resource_find
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import NumericProperty, ObjectProperty, StringProperty
from kivy.clock import Clock
from kivy.metrics import dp
from kivy.uix.screenmanager import Screen
from kivy.uix.widget import Widget

from kivymd.app import MDApp
from kivymd.theming import ThemableBehavior
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.list import OneLineIconListItem, MDList

import sys
sys.path.append("../")
from mylittlego.core.constants import (
    PROGRAM,
    VERSION,
)

# icon
from mylittlego.core.utils import find_package_resource, PATHS

ICON = find_package_resource("mylittlego/img/icon.ico")
Config.set("kivy", "window_icon", ICON)

class ContentNavigationDrawer(MDBoxLayout):
    screen_manager = ObjectProperty()
    nav_drawer = ObjectProperty()

class DrawerList(ThemableBehavior, MDList):
    def set_color_item(self, instance_item):
        '''Called when tap on a menu item.'''

        # Set the color of the icon and text for the menu item.
        for item in self.children:
            if item.text_color == self.theme_cls.primary_color:
                item.text_color = self.theme_cls.text_color
                break
        instance_item.text_color = self.theme_cls.primary_color

def on_start(self):
    icons_item = {
        "folder": "My files",
        "account-multiple": "Shared with me",
        "star": "Starred",
        "history": "Recent",
        "checkbox-marked": "Shared with me",
        "upload": "Upload",
    }
    for icon_name in icons_item.keys():
        self.root.ids.content_drawer.ids.md_list.add_widget(
            ItemDrawer(icon=icon_name, text=icons_item[icon_name])
        )

class MyLittleGoGui(Screen):
    zen = NumericProperty(0)
    controls = ObjectProperty(None)

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
    
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

