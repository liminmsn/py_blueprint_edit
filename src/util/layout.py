import dearpygui.dearpygui as dpg

def center_item(item_id):
    """计算并设置item在视口中的居中位置"""
    vp_width = dpg.get_viewport_client_width()
    vp_height = dpg.get_viewport_client_height()
    item_width = dpg.get_item_width(item_id)
    item_height = dpg.get_item_height(item_id)
    x = (vp_width - item_width) // 2
    y = (vp_height - item_height) // 2
    dpg.set_item_pos(item_id, [x, y])

def on_viewport_resize():
    if dpg.does_item_exist("center_win"):
        center_item("center_win")