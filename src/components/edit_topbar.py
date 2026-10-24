import dearpygui.dearpygui as dpg
from src.enums import PageType
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from src.application import Application

def open_ts_project(sender, app_data, user_data:'Application'):
    user_data.router(app=user_data,path_type=PageType.Home)
def exit_app():
       dpg.stop_dearpygui()
       pass

def edit_topbar(self):
        with dpg.menu_bar():
                with dpg.menu(label="项目"):
                        dpg.add_menu_item(label="首页",callback=open_ts_project,user_data=self)
                        # dpg.add_menu_item(label="退出",callback=exit_app)