import dearpygui.dearpygui as dpg

def clear_log_callback(sender, app_data, user_data):
    dpg.delete_item("log_container", children_only=True)

def add_log(message, color=(0, 255, 0)):
    if dpg.does_item_exist("log_container"):
        dpg.add_text(message, color=color, parent="log_container")
        dpg.set_y_scroll("log_container", -1.0)

def edit_log(app,edit):
    edit.add_log = add_log
    with dpg.group(horizontal=True):
        dpg.add_text("日志", color=(200, 200, 200))
        dpg.add_button(label="清空", callback=clear_log_callback)   
    dpg.add_separator()
    with dpg.child_window(width=-1, height=250, border=False, tag="log_container"):
        # for i in range(100):
        #     dpg.add_text(f"控制台日志输出 {i+1}...", color=(0, 255, 0))
        dpg.set_y_scroll("log_container", -1.0)