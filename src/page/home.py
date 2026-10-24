import dearpygui.dearpygui as dpg
import tkinter as tk
from tkinter import filedialog
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from src.application import Application
from src.util import root_dir

icons = [
    ("\ue2c7", "打开ts项目"),
    ("\ue887", "帮助"),
    ("\ue879", "退出"),
]

def callback(s,a,u):
    def open_ts_project(sender, app_data, app):
        root = tk.Tk()
        root.withdraw()
        folder_path = filedialog.askdirectory()
        root.destroy()
        
        if folder_path:
            if app.load_project:
                    app.load_project(folder_path)
        pass
    def exit_app(sender, app_data, user_data):
        dpg.stop_dearpygui()
        pass
    {"打开ts项目":open_ts_project,"退出":exit_app}[u](s,a,u)
    pass

def home(app: 'Application', tag):
    with dpg.font_registry():
        font_size = int(app.scale_factor * 22)
        icon_font = dpg.add_font(
            root_dir("resources", "font", "MaterialIcons-Regular.ttf"),
            font_size,
        )
    with dpg.window(tag=tag):
        with dpg.child_window(tag="center_win", width=350, height=350, show=True):
            with dpg.theme() as hover_theme:
                with dpg.theme_component(dpg.mvSelectable):
                    dpg.add_theme_color(dpg.mvThemeCol_HeaderHovered, (60, 60, 60, 255))
                    dpg.add_theme_style(dpg.mvStyleVar_FramePadding, 10, 10)

            for icon_code, label in icons:
                with dpg.group(horizontal=True):
                    icon_item = dpg.add_text(icon_code)
                    dpg.bind_item_font(icon_item, icon_font)
                    item = dpg.add_selectable(label=f"  {label}",user_data=label,callback=callback)
                    dpg.bind_item_theme(item, hover_theme)