import dearpygui.dearpygui as dpg
import ctypes
import os
from typing import cast
from .enums import PageType
from .util.layout import on_viewport_resize
from .util import root_dir
from .store import store
from src.page import edit, home

class Application:
    def __init__(self):
        self.title = "Typescript Blueprint Edit"
        self.window_width = 700
        self.window_height = 500
        self.min_window_width = self.window_width
        self.min_window_height = self.window_height
        self.current_page = PageType.Home
        pass
    def run(self):
        try:
            ctypes.windll.shcore.SetProcessDpiAwareness(2)
        except AttributeError:
            ctypes.windll.user32.SetProcessDPIAware()
        try:
            dpi = ctypes.windll.user32.GetDpiForSystem()
            self.scale_factor = dpi / 96.0
        except Exception:
            self.scale_factor = 1.0
        
        dpg.create_context()

        scale_factor=self.scale_factor
        print(f"系统缩放因子: {scale_factor:.2f}")
        base_font_size = 18
        pre_scale = 2
        font_path = r"C:\Windows\Fonts\msyh.ttc"
        if os.path.exists(font_path):
            with dpg.font_registry():
                with dpg.font(font_path, int(base_font_size * pre_scale)) as default_font:
                    pass 
            dpg.set_global_font_scale(scale_factor / pre_scale)
            dpg.bind_font(default_font)
        dpg.create_viewport(
            title=self.title,
            width=int(self.window_width * scale_factor),
            height=int(self.window_height * scale_factor),
            min_width=int(self.min_window_width * scale_factor),
            min_height=int(self.min_window_height * scale_factor)
            )
        dpg.set_viewport_large_icon(root_dir("resources","app.ico"))
        dpg.set_viewport_small_icon(root_dir("resources","app.ico"))
        dpg.setup_dearpygui()

        history = cast(list,store["project_history"])
        if store["top_project"] & history.__len__() > 0:
            self.router(app=self,path_type=PageType.Edit)
        else:
            self.router(app=self,path_type=self.current_page)
        dpg.set_viewport_resize_callback(on_viewport_resize)
        dpg.show_viewport()
        dpg.start_dearpygui()
        dpg.destroy_context()
        pass
    @staticmethod
    def router(app:'Application', path_type: 'PageType'):
        dpg.delete_item(app.current_page.name)
        app.current_page = path_type

        tag = path_type.name
        if path_type == PageType.Edit:
            edit(app, tag)
        elif path_type == PageType.Home:
            home(app, tag)

        on_viewport_resize()
        dpg.set_primary_window(tag, True)
        pass