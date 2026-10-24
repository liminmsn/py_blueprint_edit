import dearpygui.dearpygui as dpg
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from src.application import Application
from src.components import edit_blueprint, edit_log, edit_sidebar, edit_topbar
import dearpygui.dearpygui as dpg
def edit(app:"Application",tag:str):
    with dpg.window(tag=tag):
        edit_topbar(app)
        with dpg.group(horizontal=True):
            with dpg.child_window(width=250, height=-1):
                edit_sidebar(app)
            with dpg.child_window(width=-1, height=-1, border=False):
                with dpg.child_window(width=-1, height=-220, border=False):
                    edit_blueprint(app)
                with dpg.child_window(width=-1, height=-1):
                    edit_log(app)