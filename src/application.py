import dearpygui.dearpygui as dpg
import ctypes
import os
from .util.layout import on_viewport_resize
from .router import PageType, router
from .util import root_dir

class Application:
    def __init__(self):
        self.title = "Typescript"
        self.window_width = 700
        self.window_height = 600
        try:
            ctypes.windll.shcore.SetProcessDpiAwareness(2)
        except AttributeError:
            ctypes.windll.user32.SetProcessDPIAware()
        try:
            dpi = ctypes.windll.user32.GetDpiForSystem()
            self.scale_factor = dpi / 96.0
        except Exception:
            self.scale_factor = 1.0
    def run(self):
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
        dpg.create_viewport(title=self.title,width=int(self.window_width * scale_factor),height=int(self.window_height * scale_factor))
        dpg.set_viewport_large_icon(root_dir("resources","app.ico"))
        dpg.set_viewport_small_icon(root_dir("resources","app.ico"))
        dpg.setup_dearpygui()
        # 路由页面
        router(app=self,path_type=PageType.Home)
        dpg.set_viewport_resize_callback(on_viewport_resize)
        dpg.show_viewport()
        dpg.start_dearpygui()
        dpg.destroy_context()