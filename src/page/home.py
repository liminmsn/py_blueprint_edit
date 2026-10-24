import dearpygui.dearpygui as dpg
import tkinter as tk
from tkinter import filedialog
from src.enums import PageType
from src.util import root_dir

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from src.application import Application

icons = [
    ("\ue2c7", "打开项目"),
    ("\ue887", "帮助"),
    ("\ue879", "退出"),
]

def home(app: 'Application', tag):
    with dpg.font_registry():
        font_size = int(app.scale_factor * 22)
        icon_font = dpg.add_font(
            root_dir("resources", "font", "MaterialIcons-Regular.ttf"),
            font_size,
        )
        title_font = dpg.add_font(
            r"C:\Windows\Fonts\msyh.ttc",
            int(app.scale_factor * 32),
        )

    def on_click(sender, app_data, user_data):
        label = user_data

        if label == "打开项目":
            root = tk.Tk()
            root.withdraw()
            folder_path = filedialog.askdirectory()
            root.destroy()
            if folder_path:
                load_fn = getattr(app, "load_project", None)
                if callable(load_fn):
                    load_fn(folder_path)
                else:
                    print(f"[warn] Application 没有 load_project 方法")

        elif label == "帮助":
            app.router(app=app, path_type=PageType.Edit)

        elif label == "退出":
            dpg.stop_dearpygui()

    with dpg.window(tag=tag):
        with dpg.child_window(tag="center_win", width=250, height=350, show=True, border=False):
            with dpg.theme() as hover_theme:
                with dpg.theme_component(dpg.mvSelectable):
                    dpg.add_theme_color(dpg.mvThemeCol_HeaderHovered, (60, 60, 60, 255))
                    dpg.add_theme_style(dpg.mvStyleVar_FramePadding, 10, 10)
            with dpg.theme() as blue_bg_theme:
                with dpg.theme_component(dpg.mvChildWindow):
                    dpg.add_theme_color(dpg.mvThemeCol_ChildBg, (30, 100, 200, 255))
                    dpg.add_theme_color(dpg.mvThemeCol_Text,    (255, 255, 255, 255))
                    # 左右 12px，上下 8px
                    dpg.add_theme_style(dpg.mvStyleVar_WindowPadding, 24, 12)

            with dpg.group(horizontal=True):
                with dpg.child_window(tag="blue_banner",width=40,auto_resize_x=True, auto_resize_y=True, border=False):
                                title_item = dpg.add_text("Ts")
                                dpg.bind_item_font(title_item, title_font)
                                dpg.bind_item_theme("blue_banner", blue_bg_theme)
                dpg.add_text("蓝图编辑器")

            dpg.add_spacer(height=30)

            for icon_code, label in icons:
                with dpg.group(horizontal=True):
                    icon_item = dpg.add_text(icon_code)
                    dpg.bind_item_font(icon_item, icon_font)
                    item = dpg.add_selectable(
                        label=f"  {label}",
                        user_data=label,
                        callback=on_click,
                    )
                    dpg.bind_item_theme(item, hover_theme)