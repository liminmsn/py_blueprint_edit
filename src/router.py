import dearpygui.dearpygui as dpg
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from src.application import Application
import dearpygui.dearpygui as dpg
from src.page import edit, home
from enum import Enum

class PageType(Enum):
    Home = 1
    Edit = 2

def router(app:"Application", path_type: PageType):
    tag = path_type.name
    
    if dpg.does_item_exist(tag):
        dpg.delete_item(tag)
    if path_type == PageType.Edit:
        edit(app, tag)
    elif path_type == PageType.Home:
        home(app, tag)
    dpg.set_primary_window(tag, True)