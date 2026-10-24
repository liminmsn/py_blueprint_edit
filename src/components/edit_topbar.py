import dearpygui.dearpygui as dpg
import tkinter as tk
from tkinter import filedialog

def open_ts_project(sender, app_data, user_data):
    root = tk.Tk()
    root.withdraw()
    folder_path = filedialog.askdirectory()
    root.destroy()
    
    if folder_path:
        app = user_data
        if app.load_project:
                app.load_project(folder_path)
def exit_app():
       dpg.stop_dearpygui()
       pass

def edit_topbar(self):
        with dpg.menu_bar():
                with dpg.menu(label="项目"):
                        dpg.add_menu_item(label="打开Ts项目",callback=open_ts_project,user_data=self)
                        dpg.add_menu_item(label="退出",callback=exit_app)