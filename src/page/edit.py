import dearpygui.dearpygui as dpg
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from src.application import Application
from src.components import edit_blueprint, edit_log, edit_sidebar, edit_topbar
from types import SimpleNamespace
import dearpygui.dearpygui as dpg
def edit(app:"Application",tag:str):
    edit = SimpleNamespace(
        loadFile=None,
        addLog=None
    )

    with dpg.window(tag=tag):
        edit_topbar(app)
        with dpg.group(horizontal=True):
            with dpg.child_window(width=250, height=-1, resizable_x=True):
                edit_sidebar(app, edit)
            with dpg.child_window(width=-1, height=-1,border=False, tag="edit_content_area"):
                with dpg.group(horizontal=False):
                    edit_blueprint(app, edit)
                    edit_log(app, edit)